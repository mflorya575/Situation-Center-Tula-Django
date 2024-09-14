from django.urls import path

from . import views


app_name = 'activeforecast'

urlpatterns = [
    # Здравоохранение
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug:slug>/', views.hospital_detail, name='hospital_detail'),
    # Образование
    path('study/', views.study, name='study'),
    path('study/<slug:slug>/', views.study_detail, name='study_detail'),
    # Демография
    path('demographics/', views.demographics, name='demographics'),
    # Культура
    path('culture/', views.culture, name='culture'),
    # Дороги
    path('road/', views.road, name='road'),
    # Наука
    path('science/', views.science, name='science'),
    # Экология
    path('ecology/', views.ecology, name='ecology'),
    # Предпринимательство
    path('business/', views.business, name='business'),
    # Туризм
    path('turism/', views.turism, name='turism'),
    # Жилье и городская среда
    path('house/', views.house, name='house'),
    # Международная кооперация и экспорт
    path('world/', views.world, name='world'),
]
