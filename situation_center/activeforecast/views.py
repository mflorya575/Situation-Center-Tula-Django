from django.shortcuts import render, get_object_or_404
from foresttrees.models import *
from .forms import *
import pandas as pd
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np


def hospital(request):
    # Получаем все объекты Hospital из базы данных
    hospitals = Hospital.objects.all()

    # Передаем данные в контекст
    context = {
        'hospitals': hospitals,
        'title': 'Здравоохранение | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/hospital.html', context)


def hospital_detail(request, slug):
    hospital = get_object_or_404(Hospital, slug=slug)
    csv_file_path = hospital.csv_file.path

    # Загрузка CSV-файла в DataFrame
    df = pd.read_csv(csv_file_path)

    # Проверка на наличие столбца 'region'
    if 'region' not in df.columns:
        raise ValueError("Столбец 'region' не найден в CSV-файле.")

    # Удаление пробелов в столбце 'region'
    df['region'] = df['region'].str.strip()

    # Фильтрация по выбранному региону
    selected_region = request.GET.get('region')
    if selected_region:
        df = df[df['region'] == selected_region]

    # Преобразование DataFrame в длинный формат для удобства обработки
    df_melted = df.melt(id_vars=['region'], var_name='year', value_name='deaths')

    # Преобразование столбцов 'year' и 'deaths' в числовой формат
    df_melted['year'] = pd.to_numeric(df_melted['year'])
    df_melted['deaths'] = pd.to_numeric(df_melted['deaths'])

    # Проверка наличия данных после фильтрации
    if df_melted.empty:
        combined_chart_linear = "Нет данных для отображения."
        map_chart_linear = "Нет данных для отображения на карте."
    else:
        # Подготовка данных для прогнозирования
        X = df_melted['year'].values.reshape(-1, 1)
        y = df_melted['deaths'].values

        # Создание и обучение модели
        model = LinearRegression()
        model.fit(X, y)

        # Прогноз на следующие 8 лет
        future_years = np.arange(df_melted['year'].max() + 1, df_melted['year'].max() + 9).reshape(-1, 1)
        future_predictions = model.predict(future_years)

        # Добавление прогнозных данных в DataFrame
        future_df = pd.DataFrame({
            'region': selected_region,
            'year': future_years.flatten(),
            'deaths': future_predictions
        })
        df_melted = pd.concat([df_melted, future_df])

        # Создание комбинированного графика с линейной шкалой
        fig_linear = go.Figure()
        fig_linear.add_trace(
            go.Scatter(x=df_melted['year'], y=df_melted['deaths'], mode='lines+markers', name='Линейный график')
        )
        fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['deaths'], name='Столбчатая диаграмма'))
        fig_linear.update_layout(
            title=f'{hospital.title} - Комбинированный график с прогнозом (Линейная шкала)',
            xaxis_title='Годы',
            yaxis_title='Смертей'
        )
        combined_chart_linear = fig_linear.to_html(full_html=False)

        # Создание формы для выбора региона
        region_form = RegionForm(request.GET or None, hospital_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'hospital': hospital,
        'region_form': region_form,
        'selected_region': selected_region or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/hospital_detail.html', context)
