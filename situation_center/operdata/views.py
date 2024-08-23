from django.shortcuts import render, get_object_or_404
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
    return render(request, 'operdata/agro_detail.html', context)


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


def smcompany(request):
    # Получаем данные из базы данных и сортируем их по годам
    smcompanies = SmallMediumCompany.objects.all()

    context = {
        'smcompanies': smcompanies,
        'title': 'Малые и средние предприятия | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'operdata/smcompany.html', context)
