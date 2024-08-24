from django.urls import path

from . import views


app_name = 'yeardata'

urlpatterns = [
    # Население
    path('yeardata-population/', views.population, name='population'),
    # Уровень жизни населения
    path('yeardata-levelhealth/', views.levelhealth, name='levelhealth'),
    # Здравоохранение
    path('yeardata-hospital/', views.hospital, name='hospital'),
    # Охрана природы
    path('yeardata-securenature/', views.securenature, name='securenature'),
    # Основные фонды
    path('yeardata-capitalassets/', views.capitalassets, name='capitalassets'),
    # Предприятия и организации
    path('yeardata-organization/', views.organization, name='organization'),
    # С/X и т.д.
    path('yeardata-shlrr/', views.shlrr, name='shlrr'),
    # Торговля
    path('yeardata-trading/', views.trading, name='trading'),
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
]
