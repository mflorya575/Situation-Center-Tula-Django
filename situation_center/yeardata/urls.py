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
    path('yeardata-infotechnology/<slug:slug>/', views.infotechnology_detail, name='infotechnology_detail'),
    # Финансы
    path('yeardata-finance/', views.finance, name='finance'),
    path('yeardata-finance/<slug:slug>/', views.finance_detail, name='finance_detail'),
    # Внешняя торговля
    path('yeardata-foreigntrading/', views.foreigntrading, name='foreigntrading'),
    path('yeardata-foreigntrading/<slug:slug>/', views.foreigntrading_detail, name='foreigntrading_detail'),
    # Труд
    path('yeardata-labour/', views.labour, name='labour'),
    path('yeardata-labour/<slug:slug>/', views.labour_detail, name='labour_detail'),
    # Образование
    path('yeardata-study/', views.study, name='study'),
    path('yeardata-study/<slug:slug>/', views.study_detail, name='study_detail'),
    # Культура
    path('yeardata-culture/', views.culture, name='culture'),
    path('yeardata-culture/<slug:slug>/', views.culture_detail, name='culture_detail'),
    # Валовой региональный продукт
    path('yeardata-vrp/', views.vrp, name='vrp'),
    path('yeardata-vrp/<slug:slug>/', views.vrp_detail, name='vrp_detail'),
    # Инвестиции
    path('yeardata-investing/', views.investing, name='investing'),
    path('yeardata-investing/<slug:slug>/', views.investing_detail, name='investing_detail'),
    # Промышленное производство
    path('yeardata-industrialprod/', views.industrialprod, name='industrialprod'),
    path('yeardata-industrialprod/<slug:slug>/', views.industrialprod_detail, name='industrialprod_detail'),
    # Строительство
    path('yeardata-building/', views.building, name='building'),
    path('yeardata-building/<slug:slug>/', views.building_detail, name='building_detail'),
    # Транспорт
    path('yeardata-transport/', views.transport, name='transport'),
    path('yeardata-transport/<slug:slug>/', views.transport_detail, name='transport_detail'),
    # Наука
    path('yeardata-science/', views.science, name='science'),
    # Цены и тарифы
    path('yeardata-price/', views.price, name='price'),
]
