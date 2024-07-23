from django.contrib import admin

from .models import Hospital, HospitalData, Study, StudyData, Demographics, DemographicsData, Culture, CultureData, \
    Road, RoadData, Science, ScienceData, Ecology, EcologyData, Business, BusinessData


class HospitalDataInline(admin.TabularInline):
    model = HospitalData
    extra = 1


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description',)  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [HospitalDataInline]


class HospitalDataAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'year', 'deaths', 'region')
    list_filter = ('hospital', 'year', 'region')  # Фильтр по больнице и году
    search_fields = ('hospital__title', 'year', 'region')  # Поля для поиска
    ordering = ['hospital']

    def get_search_results(self, request, queryset, search_term):
        """
        Переопределение метода для улучшения поиска по полю study.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            # Фильтруем по названию hospital, если есть поисковый запрос
            queryset = queryset.filter(hospital__title__icontains=search_term)
        return queryset, use_distinct


class StudyDataInline(admin.TabularInline):
    model = StudyData
    extra = 1


class StudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [StudyDataInline]


class StudyDataAdmin(admin.ModelAdmin):
    list_display = ('study', 'year', 'pupil', 'region')
    list_filter = ('study', 'year', 'region')  # Фильтр по больнице и году
    search_fields = ('study__title', 'year', 'region')  # Поля для поиска
    ordering = ['study']

    def get_search_results(self, request, queryset, search_term):
        """
        Переопределение метода для улучшения поиска по полю hospital.
        """
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            # Фильтруем по названию hospital, если есть поисковый запрос
            queryset = queryset.filter(study__title__icontains=search_term)
        return queryset, use_distinct


class DemographicsDataInline(admin.TabularInline):
    model = DemographicsData
    extra = 1


class DemographicsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [DemographicsDataInline]


class DemographicsDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'index', 'region')
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


class CultureDataInline(admin.TabularInline):
    model = CultureData
    extra = 1


class CultureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [CultureDataInline]


class CultureDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'people', 'region')
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


class RoadDataInline(admin.TabularInline):
    model = RoadData
    extra = 1


class RoadAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [RoadDataInline]


class RoadDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'quantity', 'region')
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


class ScienceDataInline(admin.TabularInline):
    model = ScienceData
    extra = 1


class ScienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [ScienceDataInline]


class ScienceDataAdmin(admin.ModelAdmin):
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


class EcologyDataInline(admin.TabularInline):
    model = EcologyData
    extra = 1


class EcologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [EcologyDataInline]


class EcologyDataAdmin(admin.ModelAdmin):
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


class BusinessDataInline(admin.TabularInline):
    model = BusinessData
    extra = 1


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)  # Фильтр по названию
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ['title']  # Сортировка по умолчанию
    inlines = [BusinessDataInline]


class BusinessDataAdmin(admin.ModelAdmin):
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


# Здравоохранение


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(HospitalData, HospitalDataAdmin)

# Образование


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(StudyData, StudyDataAdmin)


# Демография

@admin.register(Demographics)
class DemographicsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(DemographicsData, DemographicsDataAdmin)


# Культура

@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CultureData, CultureDataAdmin)


# Дороги

@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(RoadData, RoadDataAdmin)


# Наука

@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ScienceData, ScienceDataAdmin)


# Экология

@admin.register(Ecology)
class EcologyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(EcologyData, EcologyDataAdmin)


# Предпринимательство

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BusinessData, BusinessDataAdmin)
