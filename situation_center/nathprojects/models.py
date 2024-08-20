from django.db import models
from django.utils.text import slugify
import os


REGION_CHOICES = [
    ('tula', 'Тульская область'),
    ('moscow', 'Московская область'),
    ('spb', 'Санкт-Петербург'),
    ('saratov', 'Саратовская область'),
    ('novosibirsk', 'Новосибирская область'),
    ('yekaterinburg', 'Свердловская область'),
    ('krasnodar', 'Краснодарский край'),
    ('kazan', 'Республика Татарстан'),
    ('vladivostok', 'Приморский край'),
    ('krasnodar', 'Краснодарский край'),
    ('nizhny_novgorod', 'Нижегородская область'),
    ('rostov', 'Ростовская область'),
]


def csv_upload_to(instance, filename):
    # Генерация пути для сохранения файла
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

    class Meta:
        verbose_name = 'Культура'
        verbose_name_plural = 'Культура'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class CultureData(models.Model):
    name = models.ForeignKey(Culture, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    people = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по культуре'
        verbose_name_plural = 'Данные по культуре'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.people} людей"


class Road(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Безопас. дороги'
        verbose_name_plural = 'Безопас. дороги'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class RoadData(models.Model):
    name = models.ForeignKey(Road, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    quantity = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по дорогам'
        verbose_name_plural = 'Данные по дорогам'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.quantity} дороги"


class Science(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Наука'
        verbose_name_plural = 'Наука'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class ScienceData(models.Model):
    name = models.ForeignKey(Science, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    data = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по науке'
        verbose_name_plural = 'Данные по науке'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.data} науки"


class Ecology(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Экология'
        verbose_name_plural = 'Экология'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class EcologyData(models.Model):
    name = models.ForeignKey(Ecology, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    data = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по экологии'
        verbose_name_plural = 'Данные по экологии'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.data} экологии"


class Business(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Предпринимательство'
        verbose_name_plural = 'Предпринимательство'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class BusinessData(models.Model):
    name = models.ForeignKey(Business, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    data = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по предпринимательству'
        verbose_name_plural = 'Данные по предпринимательству'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.data} предпринимательства"


class Turism(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Туризм'
        verbose_name_plural = 'Туризм'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class TurismData(models.Model):
    name = models.ForeignKey(Turism, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    data = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по туризму'
        verbose_name_plural = 'Данные по туризму'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.data} туризма"


class House(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Жилье'
        verbose_name_plural = 'Жилье'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class HouseData(models.Model):
    name = models.ForeignKey(House, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    data = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по жилью'
        verbose_name_plural = 'Данные по жилью'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.data} жилья"


class World(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Международка'
        verbose_name_plural = 'Международка'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class WorldData(models.Model):
    name = models.ForeignKey(World, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    data = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по международке'
        verbose_name_plural = 'Данные по международке'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.data} международки"


class Labour(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Труд'
        verbose_name_plural = 'Труд'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class LabourData(models.Model):
    name = models.ForeignKey(Labour, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    data = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по труду'
        verbose_name_plural = 'Данные по труду'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.data} труда"


class Econom(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Экономика'
        verbose_name_plural = 'Экономика'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class EconomData(models.Model):
    name = models.ForeignKey(Econom, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    data = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по экономике'
        verbose_name_plural = 'Данные по экономике'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.data} экономики"
