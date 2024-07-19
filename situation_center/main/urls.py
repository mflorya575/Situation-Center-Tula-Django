from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('policy-privacy/', views.policy_privacy, name='policy_privacy'),
]
