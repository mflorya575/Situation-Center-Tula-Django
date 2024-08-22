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
