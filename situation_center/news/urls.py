from django.urls import path

from . import views


app_name = 'news'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/<slug:news_slug>/', views.news_detail, name='news_detail'),
    path('news/page/<int:page>/', views.news, name='news_paginated'),
]
