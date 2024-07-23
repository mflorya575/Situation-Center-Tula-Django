from django.db import models
from django.utils.text import slugify


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
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по образованию'
        verbose_name_plural = 'Данные по образованию'
        ordering = ['study']

    def __str__(self):
        return f"{self.year} - {self.pupil} учащихся"


class Demographics(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Демография'
        verbose_name_plural = 'Демография'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'Без названия'


class DemographicsData(models.Model):
    name = models.ForeignKey(Demographics, related_name='data', on_delete=models.CASCADE)
    year = models.IntegerField()
    index = models.FloatField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name='Регион', blank=True)

    class Meta:
        verbose_name = 'Данные по демографии'
        verbose_name_plural = 'Данные по демографии'
        ordering = ['name']

    def __str__(self):
        return f"{self.year} - {self.index} индекс"


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
