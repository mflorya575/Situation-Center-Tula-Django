from django.urls import path

from . import views


app_name = 'ai'

urlpatterns = [
    # Атомка
    path('atom/', views.atom, name='atom'),
    # Здравоохранение
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug:slug>/', views.hospital_view, name='hospital_view'),
    # Образование
    path('study/', views.study, name='study'),
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
    # Жилье
    path('house/', views.house, name='house'),
    # Международная кооперация и экспорт
    path('world/', views.world, name='world'),
    # Труд
    path('labour/', views.labour, name='labour'),
    # Экономика
    path('econom/', views.econom, name='econom'),
    # Расширение магистральной инфраструктуры
    path('mainline/', views.mainline, name='mainline'),
    # Промышленность
    path('industry/', views.industry, name='industry'),
    # Сельское хозяйство
    path('agro/', views.agro, name='agro'),
    # Строительство
    path('building/', views.building, name='building'),
    # Транспорт
    path('transport/', views.transport, name='transport'),

    # Модель
    path('download_model/<str:filename>/', views.download_model, name='download_model'),
]

