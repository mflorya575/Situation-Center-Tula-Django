from django.contrib import admin
from .models import *


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'txt_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
