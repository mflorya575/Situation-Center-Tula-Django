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


@admin.register(Turism)
class TurismAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Labour)
class LabourAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Atom)
class AtomAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Econom)
class EconomAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Mainline)
class MainlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )
