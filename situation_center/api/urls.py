from django.urls import path

from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


app_name = 'api'

urlpatterns = [
    path('hospital/<slug:slug>/', HospitalDetailAPIView.as_view(), name='hospital-detail-api'),
    path('study/<slug:slug>/', StudyDetailAPIView.as_view(), name='study-detail-api'),

    # Динамическая схема
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Документация
    path('schema/redoc/', SpectacularRedocView.as_view(url='/api/schema/'), name='redoc'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url='/api/schema/'), name='swagger-ui'),
]
