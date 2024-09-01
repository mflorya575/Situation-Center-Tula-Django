from django.urls import path

from . import views


app_name = 'clustering'

urlpatterns = [
    path('results/', views.clustering_view, name='clustering_results'),
]


