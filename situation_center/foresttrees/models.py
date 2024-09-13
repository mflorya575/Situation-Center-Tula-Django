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


class Business(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Предпринимательство'
        verbose_name_plural = 'Предпринимательство'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Turism(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Туризм'
        verbose_name_plural = 'Туризм'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class House(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Жилье'
        verbose_name_plural = 'Жилье'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class World(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Международка'
        verbose_name_plural = 'Международка'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Labour(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Труд'
        verbose_name_plural = 'Труд'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Atom(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Атомка'
        verbose_name_plural = 'Атомка'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Econom(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Экономика'
        verbose_name_plural = 'Экономика'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class Mainline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    csv_file = models.FileField(upload_to=csv_upload_to, verbose_name='CSV файл', blank=True, null=True)

    class Meta:
        verbose_name = 'Магистральная'
        verbose_name_plural = 'Магистральная'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


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
