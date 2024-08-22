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
