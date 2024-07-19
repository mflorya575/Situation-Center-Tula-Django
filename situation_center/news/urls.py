from django.urls import path

from . import views


app_name = 'news'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/<slug:news_slug>/', views.news_detail, name='news_detail'),
]
