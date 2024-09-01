import os
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


def txt_upload_to(instance, filename):
    return os.path.join('txt_datasets', f'{instance.slug}', filename)


class Document(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    txt_file = models.FileField(upload_to=txt_upload_to, verbose_name='TXT файл', blank=True, null=True)
    content = models.TextField(verbose_name='Содержимое текста', blank=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def clean(self):
        if self.txt_file:
            ext = os.path.splitext(self.txt_file.name)[-1].lower()
            if ext != '.txt':
                raise ValidationError('Загруженный файл должен быть в формате .txt')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title or os.path.splitext(self.txt_file.name)[0])

    def __str__(self):
        return self.title if self.title else 'Без названия'
