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
