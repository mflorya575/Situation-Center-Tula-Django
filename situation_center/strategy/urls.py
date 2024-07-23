from django.urls import path

from . import views


app_name = 'strategy'

urlpatterns = [
    # Стратегия 1
    path('strategy-1/', views.strategy1, name='strategy1'),
]
