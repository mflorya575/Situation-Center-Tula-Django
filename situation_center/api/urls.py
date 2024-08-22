from django.urls import path

from .views import *


app_name = 'api'

urlpatterns = [
    path('hospital/<slug:slug>/', HospitalDetailAPIView.as_view(), name='hospital-detail-api'),
]
