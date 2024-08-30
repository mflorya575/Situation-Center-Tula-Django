from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
import folium
from folium.plugins import MarkerCluster

from .models import *
from .forms import *


def industry(request):
    # Получаем данные из базы данных и сортируем их по годам
    industries = Industry.objects.all()

    context = {
        'industries': industries,
        'title': 'Промышленность | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/industry.html', context)


def industry_detail(request, slug):
    industry = get_object_or_404(Industry, slug=slug)
    cache_key = f'industry_detail_{slug}_{request.GET.get("region", "all")}'
    context = cache.get(cache_key)

    if context is None:
        # Изначально установим переменные для обработки ошибок
        combined_chart_linear = "Ошибка при обработке данных"
        combined_chart_log = "Ошибка при обработке данных"
        map_chart_linear = "Ошибка при создании карты"
        map_chart_log = "Ошибка при создании карты"
        table_html = "Ошибка при создании таблицы"

        csv_file_path = industry.csv_file.path

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
                    title=f'{industry.title} - Комбинированный график (Линейная шкала)',
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
                    title=f'{industry.title} - Комбинированный график (Логарифмическая шкала)',
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
                                               title=f'{industry.title} - {latest_year} (Линейная шкала)',
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
                                            title=f'{industry.title} - {latest_year} (Логарифмическая шкала)',
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
        region_form = IndustryForm(request.GET or None, industry_slug=slug)

        context = {
            'combined_chart_linear': combined_chart_linear,
            'combined_chart_log': combined_chart_log,
            'map_chart_linear': map_chart_linear,
            'map_chart_log': map_chart_log,
            'table_html': table_html,
            'industry': industry,
            'region_form': region_form,
            'selected_region': request.GET.get('region') or 'Не выбран',
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }

        # Кеширование результатов
        cache.set(cache_key, context, timeout=30*24*60*60)  # Кеширование на 30 дней

    return render(request, 'operdata/industry_detail.html', context)


def agro(request):
    # Получаем данные из базы данных и сортируем их по годам
    agros = Agro.objects.all()

    context = {
        'agros': agros,
        'title': 'Сельское хозяйство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/agro.html', context)


def agro_detail(request, slug):
    agro = get_object_or_404(Agro, slug=slug)

    # Создаем уникальный ключ для кэша
    cache_key = f'agro_detail_{slug}_{request.GET.get("region", "all")}'
    context = cache.get(cache_key)

    if context is None:
        # Изначально установим переменные для обработки ошибок
        combined_chart_linear = "Ошибка при обработке данных"
        combined_chart_log = "Ошибка при обработке данных"
        map_chart_linear = "Ошибка при создании карты"
        map_chart_log = "Ошибка при создании карты"
        table_html = "Ошибка при создании таблицы"

        csv_file_path = agro.csv_file.path

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
                    title=f'{agro.title} - Комбинированный график (Линейная шкала)',
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
                    title=f'{agro.title} - Комбинированный график (Логарифмическая шкала)',
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
                                               title=f'{agro.title} - {latest_year} (Линейная шкала)',
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
                                            title=f'{agro.title} - {latest_year} (Логарифмическая шкала)',
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
        region_form = AgroForm(request.GET or None, agro_slug=slug)

        context = {
            'combined_chart_linear': combined_chart_linear,
            'combined_chart_log': combined_chart_log,
            'map_chart_linear': map_chart_linear,
            'map_chart_log': map_chart_log,
            'table_html': table_html,
            'agro': agro,
            'region_form': region_form,
            'selected_region': request.GET.get('region') or 'Не выбран',
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        # Кэшируем результат на 1 месяц (30 дней)
        cache.set(cache_key, context, timeout=30*24*60*60)

    return render(request, 'operdata/agro_detail.html', context)


def building(request):
    # Получаем данные из базы данных и сортируем их по годам
    buildings = Building.objects.all()

    context = {
        'buildings': buildings,
        'title': 'Строительство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/building.html', context)


def building_detail(request, slug):
    building = get_object_or_404(Building, slug=slug)

    # Создаем уникальный ключ для кэша
    cache_key = f'agro_detail_{slug}_{request.GET.get("region", "all")}'
    context = cache.get(cache_key)

    if context is None:
        # Изначально установим переменные для обработки ошибок
        combined_chart_linear = "Ошибка при обработке данных"
        combined_chart_log = "Ошибка при обработке данных"
        map_chart_linear = "Ошибка при создании карты"
        map_chart_log = "Ошибка при создании карты"
        table_html = "Ошибка при создании таблицы"

        csv_file_path = building.csv_file.path

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
                    title=f'{building.title} - Комбинированный график (Линейная шкала)',
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
                    title=f'{building.title} - Комбинированный график (Логарифмическая шкала)',
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
                                               title=f'{building.title} - {latest_year} (Линейная шкала)',
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
                                            title=f'{building.title} - {latest_year} (Логарифмическая шкала)',
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
        region_form = BuildingForm(request.GET or None, building_slug=slug)

        context = {
            'combined_chart_linear': combined_chart_linear,
            'combined_chart_log': combined_chart_log,
            'map_chart_linear': map_chart_linear,
            'map_chart_log': map_chart_log,
            'table_html': table_html,
            'building': building,
            'region_form': region_form,
            'selected_region': request.GET.get('region') or 'Не выбран',
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        # Кэшируем результат на 1 месяц (30 дней)
        cache.set(cache_key, context, timeout=30*24*60*60)

    return render(request, 'operdata/building_detail.html', context)


def transport(request):
    # Получаем данные из базы данных и сортируем их по годам
    transports = Transport.objects.all()

    context = {
        'transports': transports,
        'title': 'Транспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/transport.html', context)


def transport_detail(request, slug):
    transport = get_object_or_404(Transport, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = transport.csv_file.path

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
                title=f'{transport.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{transport.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{transport.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{transport.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = TransportForm(request.GET or None, transport_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'transport': transport,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/transport_detail.html', context)


def trading(request):
    # Получаем данные из базы данных и сортируем их по годам
    tradings = Trading.objects.all()

    context = {
        'tradings': tradings,
        'title': 'Торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/trading.html', context)


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
    return render(request, 'operdata/trading_detail.html', context)


def uslugi(request):
    # Получаем данные из базы данных и сортируем их по годам
    uslugis = Uslugi.objects.all()

    context = {
        'uslugis': uslugis,
        'title': 'Услуги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/uslugi.html', context)


def uslugi_detail(request, slug):
    uslugi = get_object_or_404(Uslugi, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = uslugi.csv_file.path

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
                title=f'{uslugi.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{uslugi.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{uslugi.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{uslugi.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = UslugiForm(request.GET or None, uslugi_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'uslugi': uslugi,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/uslugi_detail.html', context)


def investing(request):
    # Получаем данные из базы данных и сортируем их по годам
    investings = Investing.objects.all()

    context = {
        'investings': investings,
        'title': 'Инвестиции | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/investing.html', context)


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
    return render(request, 'operdata/investing_detail.html', context)


def finpr(request):
    # Получаем данные из базы данных и сортируем их по годам
    finprs = FinPr.objects.all()

    context = {
        'finprs': finprs,
        'title': 'Финансы предприятий | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/finpr.html', context)


def finpr_detail(request, slug):
    finpr = get_object_or_404(FinPr, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = finpr.csv_file.path

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
                title=f'{finpr.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{finpr.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{finpr.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{finpr.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = FinPrForm(request.GET or None, finpr_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'finpr': finpr,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/finpr_detail.html', context)


def price(request):
    # Получаем данные из базы данных и сортируем их по годам
    prices = Price.objects.all()

    context = {
        'prices': prices,
        'title': 'Потребительские цены | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/price.html', context)


def price_detail(request, slug):
    price = get_object_or_404(Price, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = price.csv_file.path

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
                title=f'{price.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{price.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{price.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{price.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = PriceForm(request.GET or None, price_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'price': price,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/price_detail.html', context)


def prodprice(request):
    # Получаем данные из базы данных и сортируем их по годам
    prodprices = ProdPrice.objects.all()

    context = {
        'prodprices': prodprices,
        'title': 'Цены производителей | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/prodprice.html', context)


def prodprice_detail(request, slug):
    prodprice = get_object_or_404(ProdPrice, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = prodprice.csv_file.path

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
                title=f'{prodprice.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{prodprice.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{prodprice.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{prodprice.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = ProdPriceForm(request.GET or None, prodprice_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'prodprice': prodprice,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/prodprice_detail.html', context)


def revenue(request):
    # Получаем данные из базы данных и сортируем их по годам
    revenues = Revenue.objects.all()

    context = {
        'revenues': revenues,
        'title': 'Доходы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/revenue.html', context)


def revenue_detail(request, slug):
    revenue = get_object_or_404(Revenue, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = revenue.csv_file.path

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
                title=f'{revenue.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{revenue.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{revenue.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{revenue.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = RevenueForm(request.GET or None, revenue_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'revenue': revenue,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/revenue_detail.html', context)


def salary(request):
    # Получаем данные из базы данных и сортируем их по годам
    salaries = Salary.objects.all()

    context = {
        'salaries': salaries,
        'title': 'Зарплата | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/salary.html', context)


def salary_detail(request, slug):
    salary = get_object_or_404(Salary, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = salary.csv_file.path

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
                title=f'{salary.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{salary.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{salary.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{salary.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = SalaryForm(request.GET or None, salary_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'salary': salary,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/salary_detail.html', context)


def joblessness(request):
    # Получаем данные из базы данных и сортируем их по годам
    joblessnesses = Joblessness.objects.all()

    context = {
        'joblessnesses': joblessnesses,
        'title': 'Безработица | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/joblessness.html', context)


def joblessness_detail(request, slug):
    joblessness = get_object_or_404(Joblessness, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = joblessness.csv_file.path

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
                title=f'{joblessness.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{joblessness.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{joblessness.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{joblessness.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = JoblessnessForm(request.GET or None, joblessness_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'joblessness': joblessness,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/joblessness_detail.html', context)


def jobmarket(request):
    # Получаем данные из базы данных и сортируем их по годам
    jobmarkets = JobMarket.objects.all()

    context = {
        'jobmarkets': jobmarkets,
        'title': 'Рынок труда | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/jobmarket.html', context)


def jobmarket_detail(request, slug):
    jobmarket = get_object_or_404(JobMarket, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = jobmarket.csv_file.path

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
                title=f'{jobmarket.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{jobmarket.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{jobmarket.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{jobmarket.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = JobMarketForm(request.GET or None, jobmarket_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'jobmarket': jobmarket,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/jobmarket_detail.html', context)


def smcompany(request):
    # Получаем данные из базы данных и сортируем их по годам
    smcompanies = SmallMediumCompany.objects.all()

    context = {
        'smcompanies': smcompanies,
        'title': 'Малые и средние предприятия | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/smcompany.html', context)


def smcompany_detail(request, slug):
    smcompany = get_object_or_404(SmallMediumCompany, slug=slug)

    # Изначально установим переменные для обработки ошибок
    combined_chart_linear = "Ошибка при обработке данных"
    combined_chart_log = "Ошибка при обработке данных"
    map_chart_linear = "Ошибка при создании карты"
    map_chart_log = "Ошибка при создании карты"
    table_html = "Ошибка при создании таблицы"

    csv_file_path = smcompany.csv_file.path

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
                title=f'{smcompany.title} - Комбинированный график (Линейная шкала)',
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
                title=f'{smcompany.title} - Комбинированный график (Логарифмическая шкала)',
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
                                           title=f'{smcompany.title} - {latest_year} (Линейная шкала)',
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
                                        title=f'{smcompany.title} - {latest_year} (Логарифмическая шкала)',
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
    region_form = SMCompanyForm(request.GET or None, smcompany_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'combined_chart_log': combined_chart_log,
        'map_chart_linear': map_chart_linear,
        'map_chart_log': map_chart_log,
        'table_html': table_html,
        'smcompany': smcompany,
        'region_form': region_form,
        'selected_region': request.GET.get('region') or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/smcompany_detail.html', context)
