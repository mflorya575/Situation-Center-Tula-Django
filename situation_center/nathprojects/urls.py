from django.urls import path

from . import views


app_name = 'nathprojects'

urlpatterns = [
    path('project-hospital/', views.hospital, name='hospital'),
]
