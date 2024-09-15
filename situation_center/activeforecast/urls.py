from django.urls import path

from . import views


app_name = 'activeforecast'

urlpatterns = [
    # Здравоохранение
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug:slug>/', views.hospital_detail, name='hospital_detail'),
    # Образование
    path('study/', views.study, name='study'),
    path('study/<slug:slug>/', views.study_detail, name='study_detail'),
    # Демография
    path('demographics/', views.demographics, name='demographics'),
    path('demographics/<slug:slug>/', views.demographics_detail, name='demographics_detail'),
    # Культура
    path('culture/', views.culture, name='culture'),
    path('culture/<slug:slug>/', views.culture_detail, name='culture_detail'),
    # Дороги
    path('road/', views.road, name='road'),
    path('road/<slug:slug>/', views.road_detail, name='road_detail'),
    # Наука
    path('science/', views.science, name='science'),
    path('science/<slug:slug>/', views.science_detail, name='science_detail'),
    # Экология
    path('ecology/', views.ecology, name='ecology'),
    path('ecology/<slug:slug>/', views.ecology_detail, name='ecology_detail'),
    # Предпринимательство
    path('business/', views.business, name='business'),
    path('business/<slug:slug>/', views.business_detail, name='business_detail'),
    # Туризм
    path('turism/', views.turism, name='turism'),
    path('turism/<slug:slug>/', views.turism_detail, name='turism_detail'),
    # Жилье и городская среда
    path('house/', views.house, name='house'),
    path('house/<slug:slug>/', views.house_detail, name='house_detail'),
    # Международная кооперация и экспорт
    path('world/', views.world, name='world'),
    path('world/<slug:slug>/', views.world_detail, name='world_detail'),
    # Труд
    path('labour/', views.labour, name='labour'),
    path('labour/<slug:slug>/', views.labour_detail, name='labour_detail'),
    # Атомка
    path('atom/', views.atom, name='atom'),
    path('atom/<slug:slug>/', views.atom_detail, name='atom_detail'),
    # Цифровая экономика РФ
    path('econom/', views.econom, name='econom'),
    path('econom/<slug:slug>/', views.econom_detail, name='econom_detail'),
    # Расширение магистральной инфраструктуры
    path('mainline/', views.mainline, name='mainline'),
    path('mainline/<slug:slug>/', views.mainline_detail, name='mainline_detail'),
    # Промышленность
    path('industry/', views.industry, name='industry'),
    path('industry/<slug:slug>/', views.industry_detail, name='industry_detail'),
    # Сельское хозяйство
    path('agro/', views.agro, name='agro'),
    path('agro/<slug:slug>/', views.agro_detail, name='agro_detail'),
    # Строительство
    path('building/', views.building, name='building'),
    path('building/<slug:slug>/', views.building_detail, name='building_detail'),
    # Транспорт
    path('transport/', views.transport, name='transport'),
    path('transport/<slug:slug>/', views.transport_detail, name='transport_detail'),
    # Торговля
    path('trading/', views.trading, name='trading'),
    path('trading/<slug:slug>/', views.trading_detail, name='trading_detail'),
    # Услуги
    path('uslugi/', views.uslugi, name='uslugi'),
    path('uslugi/<slug:slug>/', views.uslugi_detail, name='uslugi_detail'),
    # Инвестиции
    path('investing/', views.investing, name='investing'),
    path('investing/<slug:slug>/', views.investing_detail, name='investing_detail'),
    # Финансы предприятий
    path('finpr/', views.finpr, name='finpr'),
    path('finpr/<slug:slug>/', views.finpr_detail, name='finpr_detail'),
    # Потребительские цены
    path('price/', views.price, name='price'),
    path('price/<slug:slug>/', views.price_detail, name='price_detail'),
    # Цены производителей
    path('prodprice/', views.prodprice, name='prodprice'),
    # Доходы
    path('revenue/', views.revenue, name='revenue'),
    # Зарплата
    path('salary/', views.salary, name='salary'),
    # Безработица
    path('joblessness/', views.joblessness, name='joblessness'),
    # Рынок труда
    path('jobmarket/', views.jobmarket, name='jobmarket'),
    # Малые и средние предприятия
    path('smcompany/', views.smcompany, name='smcompany'),
    # Население
    path('population/', views.population, name='population'),
    # Уровень жизни населения
    path('levelhealth/', views.levelhealth, name='levelhealth'),
    # Охрана природы
    path('securenature/', views.securenature, name='securenature'),
    # Основные фонды
    path('capitalassets/', views.capitalassets, name='capitalassets'),
    # Предприятия и организации
    path('organization/', views.organization, name='organization'),
    # С/х, лесное, рыболовство, рыбоводство
    path('shlrr/', views.shlrr, name='shlrr'),
    # Информационные и коммуникационные технологии
    path('infotechnology/', views.infotechnology, name='infotechnology'),
    # Финансы
    path('finance/', views.finance, name='finance'),
    # Внешняя торговля
    path('foreigntrading/', views.foreigntrading, name='foreigntrading'),
    # Валовой региональный продукт
    path('vrp/', views.vrp, name='vrp'),
    # Промышленное производство
    path('industrialprod/', views.industrialprod, name='industrialprod'),
]
