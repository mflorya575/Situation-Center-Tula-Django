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
]
