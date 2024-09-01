from django.urls import path

from . import views


app_name = 'ai'

urlpatterns = [
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug:slug>/', views.hospital_view, name='hospital_view'),

    # Модель
    path('download_model/<str:filename>/', views.download_model, name='download_model'),
]

