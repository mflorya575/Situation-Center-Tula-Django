from django.urls import path

from . import views


app_name = 'errors'

urlpatterns = [
    path('in-development/', views.in_development, name='development'),
]
