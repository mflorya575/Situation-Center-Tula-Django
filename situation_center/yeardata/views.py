from django.shortcuts import render, get_object_or_404
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
import folium
from folium.plugins import MarkerCluster

from .models import *
from .forms import *


def population(request):
    # Получаем данные из базы данных и сортируем их по годам
    populations = Population.objects.all()

    context = {
        'populations': populations,
        'title': 'Население | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/population.html', context)


def population_detail(request, slug):
    population = get_object_or_404(Population, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = population.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{population.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{population.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{population.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{population.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = PopulationForm(request.GET or None, population_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'population': population,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/population_detail.html', context)


def levelhealth(request):
    # Получаем данные из базы данных и сортируем их по годам
    levelhealths = LevelHealth.objects.all()

    context = {
        'levelhealths': levelhealths,
        'title': 'Уровень жизни населения | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/levelhealth.html', context)


def levelhealth_detail(request, slug):
    levelhealth = get_object_or_404(LevelHealth, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = levelhealth.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{levelhealth.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{levelhealth.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{levelhealth.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{levelhealth.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = LevelHealthForm(request.GET or None, levelhealth_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'levelhealth': levelhealth,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/levelhealth_detail.html', context)


def hospital(request):
    # Получаем данные из базы данных и сортируем их по годам
    hospitals = Hospital.objects.all()

    context = {
        'hospitals': hospitals,
        'title': 'Здравоохранение | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/hospital.html', context)


def hospital_detail(request, slug):
    hospital = get_object_or_404(Hospital, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = hospital.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{hospital.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{hospital.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{hospital.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{hospital.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = HospitalForm(request.GET or None, hospital_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'hospital': hospital,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/hospital_detail.html', context)


def securenature(request):
    # Получаем данные из базы данных и сортируем их по годам
    securenatures = SecureNature.objects.all()

    context = {
        'securenatures': securenatures,
        'title': 'Охрана природы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/securenature.html', context)


def securenature_detail(request, slug):
    securenature = get_object_or_404(SecureNature, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = securenature.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{securenature.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{securenature.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{securenature.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{securenature.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = SecureNatureForm(request.GET or None, securenature_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'securenature': securenature,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/securenature_detail.html', context)


def capitalassets(request):
    # Получаем данные из базы данных и сортируем их по годам
    capitalassetses = CapitalAssets.objects.all()

    context = {
        'capitalassetses': capitalassetses,
        'title': 'Основные фонды | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/capitalassets.html', context)


def capitalassets_detail(request, slug):
    capitalassets = get_object_or_404(CapitalAssets, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = capitalassets.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{capitalassets.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{capitalassets.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{capitalassets.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{capitalassets.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = CapitalAssetsForm(request.GET or None, capitalassets_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'capitalassets': capitalassets,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/capitalassets_detail.html', context)


def organization(request):
    # Получаем данные из базы данных и сортируем их по годам
    organizations = Organization.objects.all()

    context = {
        'organizations': organizations,
        'title': 'Предприятия и организации | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/organization.html', context)


def organization_detail(request, slug):
    organization = get_object_or_404(Organization, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = organization.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{organization.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{organization.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{organization.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{organization.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = OrganizationForm(request.GET or None, organization_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'organization': organization,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/organization_detail.html', context)


def shlrr(request):
    # Получаем данные из базы данных и сортируем их по годам
    shlrrs = SHLRR.objects.all()

    context = {
        'shlrrs': shlrrs,
        'title': 'Сельское, лесное хозяйство, рыболовство и рыбоводство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/shlrr.html', context)


def shlrr_detail(request, slug):
    shlrr = get_object_or_404(SHLRR, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = shlrr.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{shlrr.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{shlrr.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{shlrr.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{shlrr.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = SHLRRForm(request.GET or None, shlrr_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'shlrr': shlrr,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/shlrr_detail.html', context)


def trading(request):
    # Получаем данные из базы данных и сортируем их по годам
    tradings = Trading.objects.all()

    context = {
        'tradings': tradings,
        'title': 'Торговля и услуги населению | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/trading.html', context)


def trading_detail(request, slug):
    trading = get_object_or_404(Trading, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = trading.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{trading.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{trading.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{trading.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{trading.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = TradingForm(request.GET or None, trading_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'trading': trading,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/trading_detail.html', context)


def infotechnology(request):
    # Получаем данные из базы данных и сортируем их по годам
    infotechnologies = InfoTechnology.objects.all()

    context = {
        'infotechnologies': infotechnologies,
        'title': 'Информационные и комунникационные технологии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/infotechnology.html', context)


def infotechnology_detail(request, slug):
    infotechnology = get_object_or_404(InfoTechnology, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = infotechnology.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{infotechnology.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{infotechnology.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{infotechnology.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{infotechnology.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = InfoTechnologyForm(request.GET or None, infotechnology_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'infotechnology': infotechnology,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/infotechnology_detail.html', context)


def finance(request):
    # Получаем данные из базы данных и сортируем их по годам
    finances = Finance.objects.all()

    context = {
        'finances': finances,
        'title': 'Финансы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/finance.html', context)


def finance_detail(request, slug):
    finance = get_object_or_404(Finance, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = finance.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{finance.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{finance.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{finance.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{finance.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = FinanceForm(request.GET or None, finance_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'finance': finance,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/finance_detail.html', context)


def foreigntrading(request):
    # Получаем данные из базы данных и сортируем их по годам
    foreigntradings = ForeignTrading.objects.all()

    context = {
        'foreigntradings': foreigntradings,
        'title': 'Внешняя торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/foreigntrading.html', context)


def foreigntrading_detail(request, slug):
    foreigntrading = get_object_or_404(ForeignTrading, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = foreigntrading.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{foreigntrading.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{foreigntrading.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{foreigntrading.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{foreigntrading.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = ForeignTradingForm(request.GET or None, foreigntrading_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'foreigntrading': foreigntrading,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/foreigntrading_detail.html', context)


def labour(request):
    # Получаем данные из базы данных и сортируем их по годам
    labours = Labour.objects.all()

    context = {
        'labours': labours,
        'title': 'Труд | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/labour.html', context)


def labour_detail(request, slug):
    labour = get_object_or_404(Labour, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = labour.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{labour.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{labour.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{labour.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{labour.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = LabourForm(request.GET or None, labour_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'labour': labour,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/labour_detail.html', context)


def study(request):
    # Получаем данные из базы данных и сортируем их по годам
    studies = Study.objects.all()

    context = {
        'studies': studies,
        'title': 'Образование | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/study.html', context)


def study_detail(request, slug):
    study = get_object_or_404(Study, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = study.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{study.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{study.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{study.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{study.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = StudyForm(request.GET or None, study_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'study': study,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/study_detail.html', context)


def culture(request):
    # Получаем данные из базы данных и сортируем их по годам
    cultures = Culture.objects.all()

    context = {
        'cultures': cultures,
        'title': 'Культура, отдых и туризм | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/culture.html', context)


def culture_detail(request, slug):
    culture = get_object_or_404(Culture, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = culture.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{culture.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{culture.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{culture.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{culture.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = CultureForm(request.GET or None, culture_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'culture': culture,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/culture_detail.html', context)


def vrp(request):
    # Получаем данные из базы данных и сортируем их по годам
    vrps = VRP.objects.all()

    context = {
        'vrps': vrps,
        'title': 'Валовой региональный продукт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/vrp.html', context)


def vrp_detail(request, slug):
    vrp = get_object_or_404(VRP, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = vrp.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{vrp.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{vrp.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{vrp.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{vrp.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = VRPForm(request.GET or None, vrp_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'vrp': vrp,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/vrp_detail.html', context)


def investing(request):
    # Получаем данные из базы данных и сортируем их по годам
    investings = Investing.objects.all()

    context = {
        'investings': investings,
        'title': 'Инвестиции | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/investing.html', context)


def investing_detail(request, slug):
    investing = get_object_or_404(Investing, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = investing.csv_file.path

    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_file_path)

        # Проверка на наличие столбца 'region'
        if 'region' not in df.columns:
            raise ValueError("Столбец 'region' не найден в CSV-файле.")

        # Фильтрация по выбранному региону
        selected_region = request.GET.get('region')
        if selected_region:
            df = df[df['region'] == selected_region]

        # Преобразование данных для графика
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Удаление всех типов пробелов и табуляций в столбце 'region'
        df['region'] = df['region'].str.strip()

        # Преобразование данных для таблицы
        table_html = df.to_html(index=False, classes='table table-striped')

        # Оборачиваем таблицу в div с классом
        table_html = f'<div class="table-container">{table_html}</div>'

        # Проверка наличия данных
        if df_melted.empty:
            combined_chart_linear = "Нет данных для отображения."
            map_chart_linear = "Нет данных для отображения на карте."
        else:
            # Создание комбинированного графика с линейной шкалой
            fig_linear = go.Figure()
            fig_linear.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{investing.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['data'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['data'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{investing.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество',
                yaxis_type='log'
            )
            combined_chart_log = fig_log.to_html(full_html=False)

            # Отображение карты для последнего доступного года
            latest_year = df_melted['year'].max()
            df_latest = df_melted[df_melted['year'] == latest_year]

            # Создание карты с линейной шкалой
            map_fig_linear = px.choropleth(df_latest,
                                           locations='region',
                                           locationmode='geojson-id',
                                           geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                           featureidkey="properties.name",
                                           color='data',
                                           hover_name='region',
                                           title=f'{investing.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='data',
                                        hover_name='region',
                                        title=f'{investing.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['data'].min(), df_latest['data'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Количество", ticks="outside", tickvals=[10, 100, 1000],
                                        ticktext=["10", "100", "1000"]))
            map_chart_log = map_fig_log.to_html(full_html=False)

    except Exception as e:
        # Если возникла ошибка, отобразить ее
        combined_chart_linear = f"Ошибка при обработке данных: {e}"
        combined_chart_log = f"Ошибка при обработке данных: {e}"
        map_chart_linear = "Ошибка при создании карты."
        map_chart_log = "Ошибка при создании карты."
        table_html = f"Ошибка при создании таблицы: {e}"

    # Создание формы для выбора региона
    region_form = InvestingForm(request.GET or None, investing_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'investing': investing,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/investing_detail.html', context)


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


def science(request):
    # Получаем данные из базы данных и сортируем их по годам
    sciences = Science.objects.all()

    context = {
        'sciences': sciences,
        'title': 'Наука и инновации | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/science.html', context)


def price(request):
    # Получаем данные из базы данных и сортируем их по годам
    prices = Price.objects.all()

    context = {
        'prices': prices,
        'title': 'Цены и тарифы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'yeardata/price.html', context)
