from django.contrib import admin
from .models import *


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
