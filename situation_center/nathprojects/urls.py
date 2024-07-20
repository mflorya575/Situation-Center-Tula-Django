from django.urls import path

from . import views


app_name = 'nathprojects'

urlpatterns = [
    path('project-hospital/', views.hospital, name='hospital'),
    path('project-hospital/<slug:slug>/', views.hospital_detail, name='hospital_detail'),
]
