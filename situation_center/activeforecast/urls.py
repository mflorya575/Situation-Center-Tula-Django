from django.urls import path

from . import views


app_name = 'activeforecast'

urlpatterns = [
    # Здравоохранение
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug:slug>/', views.hospital_detail, name='hospital_detail'),
    # Образование
    path('study/', views.study, name='study'),
]
