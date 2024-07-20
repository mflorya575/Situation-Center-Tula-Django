from django.contrib import admin

from .models import Hospital, HospitalData


class HospitalDataInline(admin.TabularInline):
    model = HospitalData
    extra = 1


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [HospitalDataInline]


class HospitalDataAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'year', 'deaths')
    list_filter = ('hospital', 'year')  # Фильтр по больнице и году
    search_fields = ('hospital__title', 'year')  # Поля для поиска
    ordering = ['hospital']

    def get_search_results(self, request, queryset, search_term):
        """
        Переопределение метода для улучшения поиска по полю hospital.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            # Фильтруем по названию hospital, если есть поисковый запрос
            queryset = queryset.filter(hospital__title__icontains=search_term)
        return queryset, use_distinct


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(HospitalData, HospitalDataAdmin)
