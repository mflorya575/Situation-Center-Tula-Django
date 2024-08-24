from django.urls import path

from . import views


app_name = 'yeardata'

urlpatterns = [
    path('yeardata-population/', views.population, name='population'),
]
