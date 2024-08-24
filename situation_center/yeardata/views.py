from django.shortcuts import render, get_object_or_404
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
import folium
from folium.plugins import MarkerCluster

from .models import *


def population(request):
    # Получаем данные из базы данных и сортируем их по годам
    populations = Population.objects.all()

    context = {
        'populations': populations,
        'title': 'Население | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/population.html', context)


def levelhealth(request):
    # Получаем данные из базы данных и сортируем их по годам
    levelhealths = LevelHealth.objects.all()

    context = {
        'levelhealths': levelhealths,
        'title': 'Уровень жизни населения | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/levelhealth.html', context)


def hospital(request):
    # Получаем данные из базы данных и сортируем их по годам
    hospitals = Hospital.objects.all()

    context = {
        'hospitals': hospitals,
        'title': 'Здравоохранение | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/hospital.html', context)


def securenature(request):
    # Получаем данные из базы данных и сортируем их по годам
    securenatures = SecureNature.objects.all()

    context = {
        'securenatures': securenatures,
        'title': 'Охрана природы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/securenature.html', context)


def capitalassets(request):
    # Получаем данные из базы данных и сортируем их по годам
    capitalassetses = CapitalAssets.objects.all()

    context = {
        'capitalassetses': capitalassetses,
        'title': 'Основные фонды | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/capitalassets.html', context)


def organization(request):
    # Получаем данные из базы данных и сортируем их по годам
    organizations = Organization.objects.all()

    context = {
        'organizations': organizations,
        'title': 'Предприятия и организации | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/organization.html', context)


def shlrr(request):
    # Получаем данные из базы данных и сортируем их по годам
    shlrrs = SHLRR.objects.all()

    context = {
        'shlrrs': shlrrs,
        'title': 'Сельское, лесное хозяйство, рыболовство и рыбоводство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/shlrr.html', context)


def trading(request):
    # Получаем данные из базы данных и сортируем их по годам
    tradings = Trading.objects.all()

    context = {
        'tradings': tradings,
        'title': 'Торговля и услуги населению | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/trading.html', context)


def infotechnology(request):
    # Получаем данные из базы данных и сортируем их по годам
    infotechnologies = InfoTechnology.objects.all()

    context = {
        'infotechnologies': infotechnologies,
        'title': 'Информационные и комунникационные технологии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/infotechnology.html', context)


def finance(request):
    # Получаем данные из базы данных и сортируем их по годам
    finances = Finance.objects.all()

    context = {
        'finances': finances,
        'title': 'Финансы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/finance.html', context)


def foreigntrading(request):
    # Получаем данные из базы данных и сортируем их по годам
    foreigntradings = ForeignTrading.objects.all()

    context = {
        'foreigntradings': foreigntradings,
        'title': 'Внешняя торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/foreigntrading.html', context)


def labour(request):
    # Получаем данные из базы данных и сортируем их по годам
    labours = Labour.objects.all()

    context = {
        'labours': labours,
        'title': 'Труд | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/labour.html', context)


def study(request):
    # Получаем данные из базы данных и сортируем их по годам
    studies = Study.objects.all()

    context = {
        'studies': studies,
        'title': 'Образование | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/study.html', context)


def culture(request):
    # Получаем данные из базы данных и сортируем их по годам
    cultures = Culture.objects.all()

    context = {
        'cultures': cultures,
        'title': 'Культура, отдых и туризм | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/culture.html', context)


def vrp(request):
    # Получаем данные из базы данных и сортируем их по годам
    vrps = VRP.objects.all()

    context = {
        'vrps': vrps,
        'title': 'Валовой региональный продукт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/vrp.html', context)


def investing(request):
    # Получаем данные из базы данных и сортируем их по годам
    investings = Investing.objects.all()

    context = {
        'investings': investings,
        'title': 'Инвестиции | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/investing.html', context)


def industrialprod(request):
    # Получаем данные из базы данных и сортируем их по годам
    industrialprods = IndustrialProd.objects.all()

    context = {
        'industrialprods': industrialprods,
        'title': 'Промышленное производство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/industrialprod.html', context)


def building(request):
    # Получаем данные из базы данных и сортируем их по годам
    buildings = Building.objects.all()

    context = {
        'buildings': buildings,
        'title': 'Строительство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/building.html', context)


def transport(request):
    # Получаем данные из базы данных и сортируем их по годам
    transports = Transport.objects.all()

    context = {
        'transports': transports,
        'title': 'Транспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/transport.html', context)
