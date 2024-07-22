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
]
