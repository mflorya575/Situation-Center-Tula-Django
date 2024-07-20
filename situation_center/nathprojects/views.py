from django.shortcuts import render
import plotly.express as px
import pandas as pd

from .models import Hospital


def hospital(request):
    # Получаем данные из базы данных и сортируем их по годам
    hospital_data = Hospital.objects.all().order_by('year')

    # Преобразуем данные в DataFrame для удобства работы с Plotly
    df = pd.DataFrame(list(hospital_data.values()))

    # Проверяем, что данные корректно загружены
    print(df.head())  # Отладочный вывод, чтобы проверить данные

    # Создание графика с помощью Plotly Express
    fig = px.line(df, x='year', y='deaths', title='Mortality Over Years', markers=True)

    # Преобразование графика в HTML
    chart = fig.to_html(full_html=False)

    context = {
        'chart': chart,
        'title': f'Здравоохранение | ',
    }
    return render(request, 'nathprojects/hospital.html', context)
