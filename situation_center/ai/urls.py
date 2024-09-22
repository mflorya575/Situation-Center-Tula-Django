from django.urls import path

from . import views


app_name = 'ai'

urlpatterns = [
    # Атомка
    path('atom/', views.atom, name='atom'),
    path('atom/<slug:slug>/', views.atom_view, name='atom_view'),
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
    # Экономика
    path('econom/', views.econom, name='econom'),
    path('econom/<slug:slug>/', views.econom_view, name='econom_view'),
    # Расширение магистральной инфраструктуры
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
    # Инвестиции
    path('investing/', views.investing, name='investing'),
    # Финансы предприятий
    path('finpr/', views.finpr, name='finpr'),
    # Потребительские цены
    path('price/', views.price, name='price'),
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

    # Модель
    path('download_model/<str:filename>/', views.download_model, name='download_model'),
]

