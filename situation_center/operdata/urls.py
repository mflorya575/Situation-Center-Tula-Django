from django.urls import path

from . import views


app_name = 'operdata'

urlpatterns = [
    # Промышленность
    path('operdata-industry/', views.industry, name='industry'),
    # Сельское хозяйство
    path('operdata-agro/', views.agro, name='agro'),
    # Строительство
    path('operdata-building/', views.building, name='building'),
    # Транспорт
    path('operdata-transport/', views.transport, name='transport'),
    # Торговля
    path('operdata-trading/', views.trading, name='trading'),
    # Услуги
    path('operdata-uslugi/', views.uslugi, name='uslugi'),
    # Инвестиции
    path('operdata-investing/', views.investing, name='investing'),
    # Финансы предприятий
    path('operdata-finpr/', views.finpr, name='finpr'),
    # Потребительские цены
    path('operdata-price/', views.price, name='price'),
]
