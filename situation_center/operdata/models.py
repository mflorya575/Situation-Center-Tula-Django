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


class Transport(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Trading(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Торговля'
        verbose_name_plural = 'Торговля'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Uslugi(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Investing(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Инвестиции'
        verbose_name_plural = 'Инвестиции'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class FinPr(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Финансы предприятий'
        verbose_name_plural = 'Финансы предприятий'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Price(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Потребительские цены'
        verbose_name_plural = 'Потребительские цены'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class ProdPrice(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Цены производителей'
        verbose_name_plural = 'Цены производителей'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Revenue(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Доходы'
        verbose_name_plural = 'Доходы'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Salary(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Зарплата'
        verbose_name_plural = 'Зарплата'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Joblessness(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Безработица'
        verbose_name_plural = 'Безработица'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class JobMarket(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Рынок труда'
        verbose_name_plural = 'Рынок труда'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class SmallMediumCompany(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Малые и средние предприятия'
        verbose_name_plural = 'Малые и средние предприятия'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'

