import os
from django.utils.text import slugify
from django.db import models


def csv_upload_to(instance, filename):
    return os.path.join('csv_datasets', f'{instance.slug}', filename)


class Hospital(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Здравоохранение'
        verbose_name_plural = 'Здравоохранение'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Study(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Demographics(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Демография'
        verbose_name_plural = 'Демография'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Culture(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Культура'
        verbose_name_plural = 'Культура'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Road(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Дороги'
        verbose_name_plural = 'Дороги'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Science(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Наука'
        verbose_name_plural = 'Наука'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Ecology(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Экология'
        verbose_name_plural = 'Экология'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'
