from django.urls import path

from . import views


app_name = 'strategy'

urlpatterns = [
    # Стратегия 1
    path('strategy-1/', views.strategy1, name='strategy1'),
    # Стратегия 2
    path('strategy-2/', views.strategy2, name='strategy2'),
    # Стратегия 3
    path('strategy-3/', views.strategy3, name='strategy3'),
]
