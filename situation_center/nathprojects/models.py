from django.db import models
from django.utils.text import slugify


class Hospital(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Здравоохранение'
        verbose_name_plural = 'Здравоохранение'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class HospitalData(models.Model):
    hospital = models.ForeignKey(Hospital, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    deaths = models.IntegerField()

    class Meta:
        verbose_name = 'Данные по смертности'
        verbose_name_plural = 'Данные по смертности'
        ordering = ['hospital']

    def __str__(self):
        return f"{self.year} - {self.deaths} смертей"
