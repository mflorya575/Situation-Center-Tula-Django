from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Модель категорий с вложенностью
    """
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, verbose_name='URL категории', blank=True)
    description = models.TextField(verbose_name='Описание категории', max_length=300)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    map_html = models.TextField(verbose_name='Яндекс Карта', blank=True, null=True)  # HTML-код карты
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)

    class MPTTMeta:
        """
        Сортировка по вложенности
        """
        order_insertion_by = ('title',)

    class Meta:
        """
        Сортировка, название модели в админ панели, таблица с данными
        """
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        db_table = 'app_categories'

    def __str__(self):
        """
        Возвращение заголовка категории
        """
        return self.title
