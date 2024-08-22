from django.shortcuts import render, get_object_or_404
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
import folium
from folium.plugins import MarkerCluster

from .models import *


def industry(request):
    # Получаем данные из базы данных и сортируем их по годам
    industries = Industry.objects.all()

    context = {
        'industries': industries,
        'title': 'Промышленность | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/industry.html', context)


def agro(request):
    # Получаем данные из базы данных и сортируем их по годам
    agros = Agro.objects.all()

    context = {
        'agros': agros,
        'title': 'Сельское хозяйство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/agro.html', context)


def building(request):
    # Получаем данные из базы данных и сортируем их по годам
    buildings = Building.objects.all()

    context = {
        'buildings': buildings,
        'title': 'Строительство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/building.html', context)


def transport(request):
    # Получаем данные из базы данных и сортируем их по годам
    transports = Transport.objects.all()

    context = {
        'transports': transports,
        'title': 'Транспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/transport.html', context)


def trading(request):
    # Получаем данные из базы данных и сортируем их по годам
    tradings = Trading.objects.all()

    context = {
        'tradings': tradings,
        'title': 'Торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/trading.html', context)


def uslugi(request):
    # Получаем данные из базы данных и сортируем их по годам
    uslugis = Uslugi.objects.all()

    context = {
        'uslugis': uslugis,
        'title': 'Услуги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/uslugi.html', context)


def investing(request):
    # Получаем данные из базы данных и сортируем их по годам
    investings = Investing.objects.all()

    context = {
        'investings': investings,
        'title': 'Инвестиции | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/investing.html', context)


def finpr(request):
    # Получаем данные из базы данных и сортируем их по годам
    finprs = FinPr.objects.all()

    context = {
        'finprs': finprs,
        'title': 'Финансы предприятий | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/finpr.html', context)


def price(request):
    # Получаем данные из базы данных и сортируем их по годам
    prices = Price.objects.all()

    context = {
        'prices': prices,
        'title': 'Потребительские цены | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/price.html', context)


def prodprice(request):
    # Получаем данные из базы данных и сортируем их по годам
    prodprices = ProdPrice.objects.all()

    context = {
        'prodprices': prodprices,
        'title': 'Цены производителей | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/prodprice.html', context)


def revenue(request):
    # Получаем данные из базы данных и сортируем их по годам
    revenues = Revenue.objects.all()

    context = {
        'revenues': revenues,
        'title': 'Доходы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/revenue.html', context)


def salary(request):
    # Получаем данные из базы данных и сортируем их по годам
    salaries = Salary.objects.all()

    context = {
        'salaries': salaries,
        'title': 'Зарплата | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/salary.html', context)


def joblessness(request):
    # Получаем данные из базы данных и сортируем их по годам
    joblessnesses = Joblessness.objects.all()

    context = {
        'joblessnesses': joblessnesses,
        'title': 'Безработица | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/joblessness.html', context)


def jobmarket(request):
    # Получаем данные из базы данных и сортируем их по годам
    jobmarkets = JobMarket.objects.all()

    context = {
        'jobmarkets': jobmarkets,
        'title': 'Рынок труда | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/jobmarket.html', context)
