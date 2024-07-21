from django.db import models
from django.utils.text import slugify


REGION_CHOICES = [
    ('tula', 'Тульская область'),
    ('moscow', 'Московская область'),
]


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
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по смертности'
        verbose_name_plural = 'Данные по смертности'
        ordering = ['hospital']

    def __str__(self):
        return f"{self.year} - {self.deaths} смертей"


class Study(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class StudyData(models.Model):
    study = models.ForeignKey(Study, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    pupil = models.IntegerField()

    class Meta:
        verbose_name = 'Данные по образованию'
        verbose_name_plural = 'Данные по образованию'
        ordering = ['study']

    def __str__(self):
        return f"{self.year} - {self.pupil} учащихся"
