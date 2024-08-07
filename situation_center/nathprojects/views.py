from django.shortcuts import render, get_object_or_404
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from .models import *
from .forms import RegionForm


def hospital(request):
    # Получаем данные из базы данных и сортируем их по годам
    hospitals = Hospital.objects.all()

    context = {
        'hospitals': hospitals,
        'title': 'Здравоохранение | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/hospital.html', context)


def hospital_detail(request, slug):
    # Получаем конкретную запись из базы данных по slug
    hospital = get_object_or_404(Hospital, slug=slug)
    hospital_data = hospital.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        hospital_data = hospital_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(hospital_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['deaths'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['deaths'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{hospital.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Смертей'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'hospital': hospital,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    study = get_object_or_404(Study, slug=slug)
    study_data = study.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        study_data = study_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(study_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['pupil'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['pupil'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{study.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Обучающихся'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'study': study,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    demographics = get_object_or_404(Demographics, slug=slug)
    demographics_data = demographics.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        demographics_data = demographics_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(demographics_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['index'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['index'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{demographics.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Коэффицент рождаемости'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'demographics': demographics,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    culture = get_object_or_404(Culture, slug=slug)
    culture_data = culture.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        culture_data = culture_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(culture_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['people'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['people'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{culture.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество людей'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'culture': culture,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    road = get_object_or_404(Road, slug=slug)
    road_data = road.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        road_data = road_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(road_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['quantity'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['quantity'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{road.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'road': road,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    science = get_object_or_404(Science, slug=slug)
    science_data = science.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        science_data = science_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(science_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['data'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['data'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{science.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'science': science,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    ecology = get_object_or_404(Ecology, slug=slug)
    ecology_data = ecology.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        ecology_data = ecology_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(ecology_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['data'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['data'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{ecology.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'ecology': ecology,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    business = get_object_or_404(Business, slug=slug)
    business_data = business.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        business_data = business_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(business_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['data'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['data'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{business.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'business': business,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    turism = get_object_or_404(Turism, slug=slug)
    turism_data = turism.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        turism_data = turism_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(turism_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['data'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['data'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{turism.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'turism': turism,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    house = get_object_or_404(House, slug=slug)
    house_data = house.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        house_data = house_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(house_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['data'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['data'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{house.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'house': house,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    world = get_object_or_404(World, slug=slug)
    world_data = world.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        world_data = world_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(world_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['data'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['data'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{world.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'world': world,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
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
    # Получаем конкретную запись из базы данных по slug
    labour = get_object_or_404(Labour, slug=slug)
    labour_data = labour.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        labour_data = labour_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(labour_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['data'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['data'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{labour.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'labour': labour,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/labour_detail.html', context)


def econom(request):
    # Получаем данные из базы данных и сортируем их по годам
    economs = Econom.objects.all()

    context = {
        'economs': economs,
        'title': 'Цифровая экономика | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/econom.html', context)


def econom_detail(request, slug):
    # Получаем конкретную запись из базы данных по slug
    econom = get_object_or_404(Econom, slug=slug)
    econom_data = econom.data.all().order_by('year')

    selected_region = request.GET.get('region')
    if selected_region:
        econom_data = econom_data.filter(region=selected_region)

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(econom_data.values()))

    # Проверка наличия данных
    if df.empty:
        combined_chart = "Нет данных для отображения."
    else:
        # Создание комбинированного графика
        fig = go.Figure()

        # Добавление линейного графика
        fig.add_trace(go.Scatter(x=df['year'], y=df['data'],
                                 mode='lines+markers',
                                 name='Линейный график'))

        # Добавление столбчатой диаграммы
        fig.add_trace(go.Bar(x=df['year'], y=df['data'],
                             name='Столбчатая диаграмма'))

        # Настройка осей и заголовка
        fig.update_layout(
            title=f'{econom.title} - Комбинированный график',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )

        # Преобразование графика в HTML
        combined_chart = fig.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None)

    context = {
        'combined_chart': combined_chart,
        'econom': econom,
        'region_form': region_form,
        'selected_region': dict(REGION_CHOICES).get(selected_region, 'Не выбран'),
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/econom_detail.html', context)
