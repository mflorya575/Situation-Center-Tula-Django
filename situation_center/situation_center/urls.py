"""
URL configuration for situation_center project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from news.sitemaps import NewsSitemap

from django.conf import settings


handler400 = 'errors.views.tr_handler400'
handler403 = 'errors.views.tr_handler403'
handler404 = 'errors.views.tr_handler404'
handler429 = 'errors.views.tr_handler429'
handler500 = 'errors.views.tr_handler500'
handler503 = 'errors.views.tr_handler503'

sitemaps = {
    'posts': NewsSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('', include('news.urls', namespace='news')),
    path('projects/', include('nathprojects.urls', namespace='nathprojects')),
    path('', include('errors.urls', namespace='errors')),
    path('', include('strategy.urls', namespace='strategy')),
    path('', include('userauth.urls', namespace='userauth')),
    path('api/', include('api.urls', namespace='api')),
    path('operdata/', include('operdata.urls', namespace='operdata')),

    # Карта сайта
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
