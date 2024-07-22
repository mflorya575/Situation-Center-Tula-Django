from django.shortcuts import render, get_object_or_404
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from .models import Hospital, Study, REGION_CHOICES, Demographics
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
