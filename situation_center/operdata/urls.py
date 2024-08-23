from django.urls import path

from . import views


app_name = 'operdata'

urlpatterns = [
    # Промышленность
    path('operdata-industry/', views.industry, name='industry'),
    path('operdata-industry/<slug:slug>/', views.industry_detail, name='industry_detail'),
    # Сельское хозяйство
    path('operdata-agro/', views.agro, name='agro'),
    path('operdata-agro/<slug:slug>/', views.agro_detail, name='agro_detail'),
    # Строительство
    path('operdata-building/', views.building, name='building'),
    path('operdata-building/<slug:slug>/', views.building_detail, name='building_detail'),
    # Транспорт
    path('operdata-transport/', views.transport, name='transport'),
    path('operdata-transport/<slug:slug>/', views.transport_detail, name='transport_detail'),
    # Торговля
    path('operdata-trading/', views.trading, name='trading'),
    path('operdata-trading/<slug:slug>/', views.trading_detail, name='trading_detail'),
    # Услуги
    path('operdata-uslugi/', views.uslugi, name='uslugi'),
    path('operdata-uslugi/<slug:slug>/', views.uslugi_detail, name='uslugi_detail'),
    # Инвестиции
    path('operdata-investing/', views.investing, name='investing'),
    path('operdata-investing/<slug:slug>/', views.investing_detail, name='investing_detail'),
    # Финансы предприятий
    path('operdata-finpr/', views.finpr, name='finpr'),
    path('operdata-finpr/<slug:slug>/', views.finpr_detail, name='finpr_detail'),
    # Потребительские цены
    path('operdata-price/', views.price, name='price'),
    path('operdata-price/<slug:slug>/', views.price_detail, name='price_detail'),
    # Цены производителей
    path('operdata-prodprice/', views.prodprice, name='prodprice'),
    # Доходы
    path('operdata-revenue/', views.revenue, name='revenue'),
    # Зарплата
    path('operdata-salary/', views.salary, name='salary'),
    # Безработица
    path('operdata-joblessness/', views.joblessness, name='joblessness'),
    # Рынок труда
    path('operdata-jobmarket/', views.jobmarket, name='jobmarket'),
    # Малые и средние предприятия
    path('operdata-smcompany/', views.smcompany, name='smcompany'),
]
