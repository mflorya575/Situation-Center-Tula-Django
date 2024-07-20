from django.shortcuts import render, get_object_or_404
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from .models import Hospital, Study


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

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(hospital_data.values()))

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

    context = {
        'combined_chart': combined_chart,
        'hospital': hospital,
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
    hospital_data = study.data.all().order_by('year')

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(hospital_data.values()))

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
        yaxis_title='Обучающиеся'
    )

    # Преобразование графика в HTML
    combined_chart = fig.to_html(full_html=False)

    context = {
        'combined_chart': combined_chart,
        'study': study,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'nathprojects/study_detail.html', context)
