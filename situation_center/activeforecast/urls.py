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
    # Культура
    path('culture/', views.culture, name='culture'),
    # Дороги
    path('road/', views.road, name='road'),
    # Наука
    path('science/', views.science, name='science'),
    # Экология
    path('ecology/', views.ecology, name='ecology'),
    # Предпринимательство
    path('business/', views.business, name='business'),
    # Туризм
    path('turism/', views.turism, name='turism'),
    # Жилье и городская среда
    path('house/', views.house, name='house'),
    # Международная кооперация и экспорт
    path('world/', views.world, name='world'),
    # Труд
    path('labour/', views.labour, name='labour'),
    # Атомка
    path('atom/', views.atom, name='atom'),
    # Цифровая экономика РФ
    path('econom/', views.econom, name='econom'),
    # Расширение магистральной инфраструктуры
    path('mainline/', views.mainline, name='mainline'),
    # Промышленность
    path('industry/', views.industry, name='industry'),
    # Сельское хозяйство
    path('agro/', views.agro, name='agro'),
    # Строительство
    path('building/', views.building, name='building'),
    # Транспорт
    path('transport/', views.transport, name='transport'),
    # Торговля
    path('trading/', views.trading, name='trading'),
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
]
