from django.contrib import admin

from .models import *


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Demographics)
class DemographicsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Ecology)
class EcologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


class TurismDataInline(admin.TabularInline):
    model = TurismData
    extra = 1


class TurismAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [TurismDataInline]


class TurismDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'data', 'region')
    list_filter = ('name', 'year', 'region')  # Фильтр по больнице и году
    search_fields = ('name__title', 'year', 'region')  # Поля для поиска
    ordering = ['name']

    def get_search_results(self, request, queryset, search_term):
        """
        Переопределение метода для улучшения поиска по полю name.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            # Фильтруем по названию hospital, если есть поисковый запрос
            queryset = queryset.filter(name__title__icontains=search_term)
        return queryset, use_distinct


class HouseDataInline(admin.TabularInline):
    model = HouseData
    extra = 1


class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [HouseDataInline]


class HouseDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'data', 'region')
    list_filter = ('name', 'year', 'region')  # Фильтр по больнице и году
    search_fields = ('name__title', 'year', 'region')  # Поля для поиска
    ordering = ['name']

    def get_search_results(self, request, queryset, search_term):
        """
        Переопределение метода для улучшения поиска по полю name.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            # Фильтруем по названию hospital, если есть поисковый запрос
            queryset = queryset.filter(name__title__icontains=search_term)
        return queryset, use_distinct


class WorldDataInline(admin.TabularInline):
    model = WorldData
    extra = 1


class WorldAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [WorldDataInline]


class WorldDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'data', 'region')
    list_filter = ('name', 'year', 'region')  # Фильтр по больнице и году
    search_fields = ('name__title', 'year', 'region')  # Поля для поиска
    ordering = ['name']

    def get_search_results(self, request, queryset, search_term):
        """
        Переопределение метода для улучшения поиска по полю name.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            # Фильтруем по названию hospital, если есть поисковый запрос
            queryset = queryset.filter(name__title__icontains=search_term)
        return queryset, use_distinct


class LabourDataInline(admin.TabularInline):
    model = LabourData
    extra = 1


class LabourAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [LabourDataInline]


class LabourDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'data', 'region')
    list_filter = ('name', 'year', 'region')  # Фильтр по больнице и году
    search_fields = ('name__title', 'year', 'region')  # Поля для поиска
    ordering = ['name']

    def get_search_results(self, request, queryset, search_term):
        """
        Переопределение метода для улучшения поиска по полю name.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            # Фильтруем по названию hospital, если есть поисковый запрос
            queryset = queryset.filter(name__title__icontains=search_term)
        return queryset, use_distinct


class EconomDataInline(admin.TabularInline):
    model = EconomData
    extra = 1


class EconomAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [EconomDataInline]


class EconomDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'data', 'region')
    list_filter = ('name', 'year', 'region')  # Фильтр по больнице и году
    search_fields = ('name__title', 'year', 'region')  # Поля для поиска
    ordering = ['name']

    def get_search_results(self, request, queryset, search_term):
        """
        Переопределение метода для улучшения поиска по полю name.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            # Фильтруем по названию hospital, если есть поисковый запрос
            queryset = queryset.filter(name__title__icontains=search_term)
        return queryset, use_distinct


# Туризм

@admin.register(Turism)
class TurismAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(TurismData, TurismDataAdmin)


# Жилье

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(HouseData, HouseDataAdmin)


# Международка

@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(WorldData, WorldDataAdmin)


# Труд

@admin.register(Labour)
class LabourAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(LabourData, LabourDataAdmin)


# Экономика

@admin.register(Econom)
class EconomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(EconomData, EconomDataAdmin)
