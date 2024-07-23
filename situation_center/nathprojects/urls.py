from django.urls import path

from . import views


app_name = 'nathprojects'

urlpatterns = [
    # Здравоохранение
    path('project-hospital/', views.hospital, name='hospital'),
    path('project-hospital/<slug:slug>/', views.hospital_detail, name='hospital_detail'),
    # Образование
    path('project-study/', views.study, name='study'),
    path('project-study/<slug:slug>/', views.study_detail, name='study_detail'),
    # Демография
    path('project-demographics/', views.demographics, name='demographics'),
    path('project-demographics/<slug:slug>/', views.demographics_detail, name='demographics_detail'),
    # Культура
    path('project-culture/', views.culture, name='culture'),
    path('project-culture/<slug:slug>/', views.culture_detail, name='culture_detail'),
    # Дороги
    path('project-road/', views.road, name='road'),
    path('project-road/<slug:slug>/', views.road_detail, name='road_detail'),
    # Наука
    path('project-science/', views.science, name='science'),
    path('project-science/<slug:slug>/', views.science_detail, name='science_detail'),
    # Экология
    path('project-ecology/', views.ecology, name='ecology'),
    path('project-ecology/<slug:slug>/', views.ecology_detail, name='ecology_detail'),
    # Предпринимательство
    path('project-business/', views.business, name='business'),
    path('project-business/<slug:slug>/', views.business_detail, name='business_detail'),
    # Туризм
    path('project-turism/', views.turism, name='turism'),
    path('project-turism/<slug:slug>/', views.turism_detail, name='turism_detail'),
    # Жилье
    path('project-house/', views.house, name='house'),
    path('project-house/<slug:slug>/', views.house_detail, name='house_detail'),
    # Международка
    path('project-world/', views.world, name='world'),
    path('project-world/<slug:slug>/', views.world_detail, name='world_detail'),
    # Труд
    path('project-labour/', views.labour, name='labour'),
]
