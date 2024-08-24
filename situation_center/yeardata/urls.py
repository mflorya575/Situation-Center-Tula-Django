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
]
