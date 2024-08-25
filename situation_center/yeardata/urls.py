from django.urls import path

from . import views


app_name = 'yeardata'

urlpatterns = [
    # Население
    path('yeardata-population/', views.population, name='population'),
    path('yeardata-population/<slug:slug>/', views.population_detail, name='population_detail'),
    # Уровень жизни населения
    path('yeardata-levelhealth/', views.levelhealth, name='levelhealth'),
    path('yeardata-levelhealth/<slug:slug>/', views.levelhealth_detail, name='levelhealth_detail'),
    # Здравоохранение
    path('yeardata-hospital/', views.hospital, name='hospital'),
    path('yeardata-hospital/<slug:slug>/', views.hospital_detail, name='hospital_detail'),
    # Охрана природы
    path('yeardata-securenature/', views.securenature, name='securenature'),
    path('yeardata-securenature/<slug:slug>/', views.securenature_detail, name='securenature_detail'),
    # Основные фонды
    path('yeardata-capitalassets/', views.capitalassets, name='capitalassets'),
    path('yeardata-capitalassets/<slug:slug>/', views.capitalassets_detail, name='capitalassets_detail'),
    # Предприятия и организации
    path('yeardata-organization/', views.organization, name='organization'),
    path('yeardata-organization/<slug:slug>/', views.organization_detail, name='organization_detail'),
    # С/X и т.д.
    path('yeardata-shlrr/', views.shlrr, name='shlrr'),
    path('yeardata-shlrr/<slug:slug>/', views.shlrr_detail, name='shlrr_detail'),
    # Торговля
    path('yeardata-trading/', views.trading, name='trading'),
    path('yeardata-trading/<slug:slug>/', views.trading_detail, name='trading_detail'),
    # Информационные технологии
    path('yeardata-infotechnology/', views.infotechnology, name='infotechnology'),
    # Финансы
    path('yeardata-finance/', views.finance, name='finance'),
    # Внешняя торговля
    path('yeardata-foreigntrading/', views.foreigntrading, name='foreigntrading'),
    # Труд
    path('yeardata-labour/', views.labour, name='labour'),
    # Образование
    path('yeardata-study/', views.study, name='study'),
    # Культура
    path('yeardata-culture/', views.culture, name='culture'),
    # Валовой региональный продукт
    path('yeardata-vrp/', views.vrp, name='vrp'),
    # Инвестиции
    path('yeardata-investing/', views.investing, name='investing'),
    # Промышленное производство
    path('yeardata-industrialprod/', views.industrialprod, name='industrialprod'),
    # Строительство
    path('yeardata-building/', views.building, name='building'),
    # Транспорт
    path('yeardata-transport/', views.transport, name='transport'),
    # Наука
    path('yeardata-science/', views.science, name='science'),
    # Цены и тарифы
    path('yeardata-price/', views.price, name='price'),
]
