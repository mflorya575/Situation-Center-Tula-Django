from django.urls import path

from . import views


app_name = 'activeforecast'

urlpatterns = [
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug:slug>/', views.hospital_detail, name='hospital_detail'),
]
