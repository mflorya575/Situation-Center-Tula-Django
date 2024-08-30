from django.urls import path

from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


app_name = 'api'

urlpatterns = [
    path('hospital/<slug:slug>/', HospitalDetailAPIView.as_view(), name='hospital-detail-api'),
    path('study/<slug:slug>/', StudyDetailAPIView.as_view(), name='study-detail-api'),
    path('demographics/<slug:slug>/', DemographicsDetailAPIView.as_view(), name='demographics-detail-api'),
    path('culture/<slug:slug>/', CultureDetailAPIView.as_view(), name='culture-detail-api'),
    path('road/<slug:slug>/', RoadDetailAPIView.as_view(), name='road-detail-api'),
    path('science/<slug:slug>/', ScienceDetailAPIView.as_view(), name='science-detail-api'),

    # Динамическая схема
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Документация
    path('schema/redoc/', SpectacularRedocView.as_view(url='/api/schema/'), name='redoc'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url='/api/schema/'), name='swagger-ui'),
]
