from django.db import models
from django.utils.text import slugify
import os


def csv_upload_to(instance, filename):
    # Генерация пути для сохранения файла
    return os.path.join('csv_datasets_operdata', f'{instance.slug}', filename)


class Industry(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Промышленность'
        verbose_name_plural = 'Промышленность'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Agro(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Сельское хозяйство'
        verbose_name_plural = 'Сельское хозяйство'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Building(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Строительство'
        verbose_name_plural = 'Строительство'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'
