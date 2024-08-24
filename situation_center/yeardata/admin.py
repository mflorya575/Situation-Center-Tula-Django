from django.contrib import admin

from .models import *


@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(LevelHealth)
class LevelHealthAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


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


@admin.register(SecureNature)
class SecureNatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(CapitalAssets)
class CapitalAssetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(SHLRR)
class SHLRRAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Trading)
class TradingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(InfoTechnology)
class InfoTechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(ForeignTrading)
class ForeignTradingAdmin(admin.ModelAdmin):
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


@admin.register(VRP)
class VRPAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Investing)
class InvestingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(IndustrialProd)
class IndustrialProdAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
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


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )
