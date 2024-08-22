from django.contrib import admin

from .models import *


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Agro)
class AgroAdmin(admin.ModelAdmin):
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


@admin.register(Uslugi)
class UslugiAdmin(admin.ModelAdmin):
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


@admin.register(FinPr)
class FinPrAdmin(admin.ModelAdmin):
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


@admin.register(ProdPrice)
class ProdPriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(Joblessness)
class JoblessnessAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(JobMarket)
class JobMarketAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )


@admin.register(SmallMediumCompany)
class SmallMediumCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

    # Позволяет просматривать и загружать CSV файл
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'csv_file')
        }),
    )
