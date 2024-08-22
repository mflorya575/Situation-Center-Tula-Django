from django.urls import path

from . import views


app_name = 'operdata'

urlpatterns = [
    # Промышленность
    path('operdata-industry/', views.industry, name='industry'),
]
