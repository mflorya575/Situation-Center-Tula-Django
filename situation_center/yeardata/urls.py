from django.urls import path

from . import views


app_name = 'yeardata'

urlpatterns = [
    # Население
    path('yeardata-population/', views.population, name='population'),
    # Уровень жизни населения
    path('yeardata-levelhealth/', views.levelhealth, name='levelhealth'),
    # Здравоохранение
    path('yeardata-hospital/', views.hospital, name='hospital'),
    # Охрана природы
    path('yeardata-securenature/', views.securenature, name='securenature'),
    # Основные фонды
    path('yeardata-capitalassets/', views.capitalassets, name='capitalassets'),
    # Предприятия и организации
    path('yeardata-organization/', views.organization, name='organization'),
    # С/X и т.д.
    path('yeardata-shlrr/', views.shlrr, name='shlrr'),
    # Торговля
    path('yeardata-trading/', views.trading, name='trading'),
    # Информационные технологии
    path('yeardata-infotechnology/', views.infotechnology, name='infotechnology'),
    # Финансы
    path('yeardata-finance/', views.finance, name='finance'),
]
