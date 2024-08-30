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
    path('ecology/<slug:slug>/', EcologyDetailAPIView.as_view(), name='ecology-detail-api'),
    path('business/<slug:slug>/', BusinessDetailAPIView.as_view(), name='business-detail-api'),
    path('turism/<slug:slug>/', TurismDetailAPIView.as_view(), name='turism-detail-api'),
    path('house/<slug:slug>/', HouseDetailAPIView.as_view(), name='house-detail-api'),
    path('world/<slug:slug>/', WorldDetailAPIView.as_view(), name='world-detail-api'),
    path('labour/<slug:slug>/', LabourDetailAPIView.as_view(), name='labour-detail-api'),
    path('atom/<slug:slug>/', AtomDetailAPIView.as_view(), name='atom-detail-api'),
    path('econom/<slug:slug>/', EconomDetailAPIView.as_view(), name='econom-detail-api'),
    path('mainline/<slug:slug>/', MainlineDetailAPIView.as_view(), name='mainline-detail-api'),

    # Динамическая схема
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Документация
    path('schema/redoc/', SpectacularRedocView.as_view(url='/api/schema/'), name='redoc'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url='/api/schema/'), name='swagger-ui'),
]
