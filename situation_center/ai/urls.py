from django.urls import path

from . import views


app_name = 'ai'

urlpatterns = [
    # Здравоохранение
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug:slug>/', views.hospital_view, name='hospital_view'),
    # Образование
    path('study/', views.study, name='study'),

    # Модель
    path('download_model/<str:filename>/', views.download_model, name='download_model'),
]

