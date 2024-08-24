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
