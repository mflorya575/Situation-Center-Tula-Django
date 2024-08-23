from django.shortcuts import render, get_object_or_404
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
import folium
from folium.plugins import MarkerCluster

from .models import *
from .forms import *


def hospital(request):
    # Получаем данные из базы данных и сортируем их по годам
    hospitals = Hospital.objects.all()

    context = {
        'hospitals': hospitals,
        'title': 'Здравоохранение | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/hospital.html', context)


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
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='deaths')

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
                go.Scatter(x=df_melted['year'], y=df_melted['deaths'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['deaths'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{hospital.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Смертей'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['deaths'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['deaths'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{hospital.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Смертей',
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
                                           color='deaths',
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
                                        color='deaths',
                                        hover_name='region',
                                        title=f'{hospital.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['deaths'].min(), df_latest['deaths'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Смертей", ticks="outside", tickvals=[10, 100, 1000],
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
    region_form = RegionForm(request.GET or None, hospital_slug=slug)

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
    return render(request, 'nathprojects/project_detail.html', context)


def study(request):
    # Получаем данные из базы данных и сортируем их по годам
    studys = Study.objects.all()

    context = {
        'studys': studys,
        'title': 'Образование | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/study.html', context)


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
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='students')

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
                go.Scatter(x=df_melted['year'], y=df_melted['students'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['students'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{study.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Обучающихся'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['students'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['students'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{study.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Обучающихся',
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
                                           color='students',
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
                                        color='students',
                                        hover_name='region',
                                        title=f'{study.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['students'].min(), df_latest['students'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Обучающихся", ticks="outside", tickvals=[10, 100, 1000],
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
    return render(request, 'nathprojects/study_detail.html', context)


def demographics(request):
    # Получаем данные из базы данных и сортируем их по годам
    demographicses = Demographics.objects.all()

    context = {
        'demographicses': demographicses,
        'title': 'Демография | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/demographics.html', context)


def demographics_detail(request, slug):
    demographics = get_object_or_404(Demographics, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = demographics.csv_file.path

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
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='quantity')

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
                go.Scatter(x=df_melted['year'], y=df_melted['quantity'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['quantity'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{demographics.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['quantity'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['quantity'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{demographics.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           color='quantity',
                                           hover_name='region',
                                           title=f'{demographics.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='quantity',
                                        hover_name='region',
                                        title=f'{demographics.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['quantity'].min(), df_latest['quantity'].max()],
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
    region_form = DemographicsForm(request.GET or None, demographics_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'demographics': demographics,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/demographics_detail.html', context)


def culture(request):
    # Получаем данные из базы данных и сортируем их по годам
    cultures = Culture.objects.all()

    context = {
        'cultures': cultures,
        'title': 'Культура | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/culture.html', context)


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
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='people')

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
                go.Scatter(x=df_melted['year'], y=df_melted['people'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['people'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{culture.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Людей'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['people'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['people'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{culture.title} - Комбинированный график (Логарифмическая шкала)',
                xaxis_title='Годы',
                yaxis_title='Людей',
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
                                           color='people',
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
                                        color='people',
                                        hover_name='region',
                                        title=f'{culture.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['people'].min(), df_latest['people'].max()],
                                        color_continuous_midpoint=0.1)
            map_fig_log.update_geos(fitbounds="locations", visible=False)
            map_fig_log.update_layout(
                coloraxis_colorbar=dict(title="Людей", ticks="outside", tickvals=[10, 100, 1000],
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
    return render(request, 'nathprojects/culture_detail.html', context)


def road(request):
    # Получаем данные из базы данных и сортируем их по годам
    roads = Road.objects.all()

    context = {
        'roads': roads,
        'title': 'Безопасные дороги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/road.html', context)


def road_detail(request, slug):
    road = get_object_or_404(Road, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = road.csv_file.path

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
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='quantity')

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
                go.Scatter(x=df_melted['year'], y=df_melted['quantity'], mode='lines+markers', name='Линейный график'))
            fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['quantity'], name='Столбчатая диаграмма'))
            fig_linear.update_layout(
                title=f'{road.title} - Комбинированный график (Линейная шкала)',
                xaxis_title='Годы',
                yaxis_title='Количество'
            )
            combined_chart_linear = fig_linear.to_html(full_html=False)

            # Создание комбинированного графика с логарифмической шкалой
            fig_log = go.Figure()
            fig_log.add_trace(
                go.Scatter(x=df_melted['year'], y=df_melted['quantity'], mode='lines+markers', name='Линейный график'))
            fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['quantity'], name='Столбчатая диаграмма'))
            fig_log.update_layout(
                title=f'{road.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           color='quantity',
                                           hover_name='region',
                                           title=f'{road.title} - {latest_year} (Линейная шкала)',
                                           color_continuous_scale='Reds')
            map_fig_linear.update_geos(fitbounds="locations", visible=False)
            map_chart_linear = map_fig_linear.to_html(full_html=False)

            # Создание карты с логарифмической шкалой
            map_fig_log = px.choropleth(df_latest,
                                        locations='region',
                                        locationmode='geojson-id',
                                        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                        featureidkey="properties.name",
                                        color='quantity',
                                        hover_name='region',
                                        title=f'{road.title} - {latest_year} (Логарифмическая шкала)',
                                        color_continuous_scale='Reds',
                                        range_color=[df_latest['quantity'].min(), df_latest['quantity'].max()],
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
    region_form = RoadForm(request.GET or None, road_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'road': road,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/road_detail.html', context)


def science(request):
    # Получаем данные из базы данных и сортируем их по годам
    sciences = Science.objects.all()

    context = {
        'sciences': sciences,
        'title': 'Наука и университеты | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/science.html', context)


def science_detail(request, slug):
    science = get_object_or_404(Science, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = science.csv_file.path

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
                title=f'{science.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{science.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{science.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{science.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = ScienceForm(request.GET or None, science_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'science': science,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/science_detail.html', context)


def ecology(request):
    # Получаем данные из базы данных и сортируем их по годам
    ecologys = Ecology.objects.all()

    context = {
        'ecologys': ecologys,
        'title': 'Экология | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/ecology.html', context)


def ecology_detail(request, slug):
    ecology = get_object_or_404(Ecology, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = ecology.csv_file.path

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
                title=f'{ecology.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{ecology.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{ecology.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{ecology.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = EcologyForm(request.GET or None, ecology_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'ecology': ecology,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/ecology_detail.html', context)


def business(request):
    # Получаем данные из базы данных и сортируем их по годам
    businesses = Business.objects.all()

    context = {
        'businesses': businesses,
        'title': 'Предпринимательство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/business.html', context)


def business_detail(request, slug):
    business = get_object_or_404(Business, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = business.csv_file.path

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
                title=f'{business.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{business.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{business.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{business.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = BusinessForm(request.GET or None, business_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'business': business,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/business_detail.html', context)


def turism(request):
    # Получаем данные из базы данных и сортируем их по годам
    turisms = Turism.objects.all()

    context = {
        'turisms': turisms,
        'title': 'Туризм | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/turism.html', context)


def turism_detail(request, slug):
    turism = get_object_or_404(Turism, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = turism.csv_file.path

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
                title=f'{turism.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{turism.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{turism.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{turism.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = TurismForm(request.GET or None, turism_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'turism': turism,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/turism_detail.html', context)


def house(request):
    # Получаем данные из базы данных и сортируем их по годам
    houses = House.objects.all()

    context = {
        'houses': houses,
        'title': 'Жилье и городская среда | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/house.html', context)


def house_detail(request, slug):
    house = get_object_or_404(House, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = house.csv_file.path

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
                title=f'{house.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{house.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{house.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{house.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = HouseForm(request.GET or None, house_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'house': house,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/house_detail.html', context)


def world(request):
    # Получаем данные из базы данных и сортируем их по годам
    worlds = World.objects.all()

    context = {
        'worlds': worlds,
        'title': 'Международная кооперация и экспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/world.html', context)


def world_detail(request, slug):
    world = get_object_or_404(World, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = world.csv_file.path

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
                title=f'{world.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{world.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{world.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{world.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = WorldForm(request.GET or None, world_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'world': world,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/world_detail.html', context)


def labour(request):
    # Получаем данные из базы данных и сортируем их по годам
    labours = Labour.objects.all()

    context = {
        'labours': labours,
        'title': 'Производительность труда | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/labour.html', context)


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
    return render(request, 'nathprojects/labour_detail.html', context)


def atom(request):
    # Получаем данные из базы данных и сортируем их по годам
    atoms = Atom.objects.all()

    context = {
        'atoms': atoms,
        'title': 'Развитие технологий в области атомной энергии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/atom.html', context)


def atom_detail(request, slug):
    atom = get_object_or_404(Atom, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = atom.csv_file.path

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
                title=f'{atom.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{atom.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{atom.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{atom.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = AtomForm(request.GET or None, atom_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'atom': atom,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/atom_detail.html', context)


def econom(request):
    # Получаем данные из базы данных и сортируем их по годам
    economs = Econom.objects.all()

    context = {
        'economs': economs,
        'title': 'Цифровая экономика | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/econom.html', context)


def econom_detail(request, slug):
    econom = get_object_or_404(Econom, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = econom.csv_file.path

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
                title=f'{econom.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{econom.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{econom.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{econom.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = EconomForm(request.GET or None, econom_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'econom': econom,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/econom_detail.html', context)


def mainline(request):
    # Получаем данные из базы данных и сортируем их по годам
    mainlines = Mainline.objects.all()

    context = {
        'mainlines': mainlines,
        'title': 'Расширение магистральной инфраструктуры | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/mainline.html', context)


def mainline_detail(request, slug):
    mainline = get_object_or_404(Mainline, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = mainline.csv_file.path

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
                title=f'{mainline.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{mainline.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{mainline.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{mainline.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = MainlineForm(request.GET or None, mainline_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'mainline': mainline,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/mainline_detail.html', context)
