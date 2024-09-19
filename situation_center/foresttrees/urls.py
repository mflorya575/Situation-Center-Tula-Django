from django.urls import path

from . import views


app_name = 'foresttrees'

urlpatterns = [
    # Здравоохранение
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug:slug>/', views.hospital_view, name='hospital_view'),
    # Образование
    path('study/', views.study, name='study'),
    path('study/<slug:slug>/', views.study_view, name='study_view'),
    # Демография
    path('demographics/', views.demographics, name='demographics'),
    path('demographics/<slug:slug>/', views.demographics_view, name='demographics_view'),
    # Культура
    path('culture/', views.culture, name='culture'),
    path('culture/<slug:slug>/', views.culture_view, name='culture_view'),
    # Дороги
    path('road/', views.road, name='road'),
    path('road/<slug:slug>/', views.road_view, name='road_view'),
    # Наука
    path('science/', views.science, name='science'),
    path('science/<slug:slug>/', views.science_view, name='science_view'),
    # Экология
    path('ecology/', views.ecology, name='ecology'),
    path('ecology/<slug:slug>/', views.ecology_view, name='ecology_view'),
    # Предпринимательство
    path('business/', views.business, name='business'),
    path('business/<slug:slug>/', views.business_view, name='business_view'),
    # Туризм
    path('turism/', views.turism, name='turism'),
    path('turism/<slug:slug>/', views.turism_view, name='turism_view'),
    # Жилье
    path('house/', views.house, name='house'),
    path('house/<slug:slug>/', views.house_view, name='house_view'),
    # Международная кооперация и экспорт
    path('world/', views.world, name='world'),
    path('world/<slug:slug>/', views.world_view, name='world_view'),
    # Труд
    path('labour/', views.labour, name='labour'),
    path('labour/<slug:slug>/', views.labour_view, name='labour_view'),
    # Атомка
    path('atom/', views.atom, name='atom'),
    path('atom/<slug:slug>/', views.atom_view, name='atom_view'),
    # Экономика
    path('econom/', views.econom, name='econom'),
    path('econom/<slug:slug>/', views.econom_view, name='econom_view'),
    # Магистральная
    path('mainline/', views.mainline, name='mainline'),
    path('mainline/<slug:slug>/', views.mainline_view, name='mainline_view'),
    # Промышленность
    path('industry/', views.industry, name='industry'),
    path('industry/<slug:slug>/', views.industry_view, name='industry_view'),
    # Сельское хозяйство
    path('agro/', views.agro, name='agro'),
    path('agro/<slug:slug>/', views.agro_view, name='agro_view'),
    # Строительство
    path('building/', views.building, name='building'),
    path('building/<slug:slug>/', views.building_view, name='building_view'),
    # Транспорт
    path('transport/', views.transport, name='transport'),
    path('transport/<slug:slug>/', views.transport_view, name='transport_view'),
    # Торговля
    path('trading/', views.trading, name='trading'),
    path('trading/<slug:slug>/', views.trading_view, name='trading_view'),
    # Услуги
    path('uslugi/', views.uslugi, name='uslugi'),
    path('uslugi/<slug:slug>/', views.uslugi_view, name='uslugi_view'),
    # Инвестиции
    path('investing/', views.investing, name='investing'),
    path('investing/<slug:slug>/', views.investing_view, name='investing_view'),
    # Финансы предприятий
    path('finpr/', views.finpr, name='finpr'),
    path('finpr/<slug:slug>/', views.finpr_view, name='finpr_view'),
    # Потребительские цены
    path('price/', views.price, name='price'),
    path('price/<slug:slug>/', views.price_view, name='price_view'),
    # Цены производителей
    path('prodprice/', views.prodprice, name='prodprice'),
    path('prodprice/<slug:slug>/', views.prodprice_view, name='prodprice_view'),
    # Доходы
    path('revenue/', views.revenue, name='revenue'),
    path('revenue/<slug:slug>/', views.revenue_view, name='revenue_view'),
    # Зарплата
    path('salary/', views.salary, name='salary'),
    path('salary/<slug:slug>/', views.salary_view, name='salary_view'),
    # Безработица
    path('joblessness/', views.joblessness, name='joblessness'),
    path('joblessness/<slug:slug>/', views.joblessness_view, name='joblessness_view'),
    # Рынок труда
    path('jobmarket/', views.jobmarket, name='jobmarket'),
    path('jobmarket/<slug:slug>/', views.jobmarket_view, name='jobmarket_view'),
    # Малые и средние предприятия
    path('smcompany/', views.smcompany, name='smcompany'),
    path('smcompany/<slug:slug>/', views.smcompany_view, name='smcompany_view'),
    # Население
    path('population/', views.population, name='population'),
    path('population/<slug:slug>/', views.population_view, name='population_view'),
    # Уровень жизни населения
    path('levelhealth/', views.levelhealth, name='levelhealth'),
    path('levelhealth/<slug:slug>/', views.levelhealth_view, name='levelhealth_view'),
    # Охрана природы
    path('securenature/', views.securenature, name='securenature'),
    path('securenature/<slug:slug>/', views.securenature_view, name='securenature_view'),
    # Основные фонды
    path('capitalassets/', views.capitalassets, name='capitalassets'),
    path('capitalassets/<slug:slug>/', views.capitalassets_view, name='capitalassets_view'),
    # Предприятия и организации
    path('organization/', views.organization, name='organization'),
    path('organization/<slug:slug>/', views.organization_view, name='organization_view'),
    # С/х, лесное, рыболовство, рыбоводство
    path('shlrr/', views.shlrr, name='shlrr'),
    path('shlrr/<slug:slug>/', views.shlrr_view, name='shlrr_view'),
    # Информационные и коммуникационные технологии
    path('infotechnology/', views.infotechnology, name='infotechnology'),
    path('infotechnology/<slug:slug>/', views.infotechnology_view, name='infotechnology_view'),
    # Финансы
    path('finance/', views.finance, name='finance'),
    path('finance/<slug:slug>/', views.finance_view, name='finance_view'),
    # Внешняя торговля
    path('foreigntrading/', views.foreigntrading, name='foreigntrading'),
    path('foreigntrading/<slug:slug>/', views.foreigntrading_view, name='foreigntrading_view'),
    # Валовой региональный продукт
    path('vrp/', views.vrp, name='vrp'),
    path('vrp/<slug:slug>/', views.vrp_view, name='vrp_view'),
    # Промышленное производство
    path('industrialprod/', views.industrialprod, name='industrialprod'),
    path('industrialprod/<slug:slug>/', views.industrialprod_view, name='industrialprod_view'),
]
