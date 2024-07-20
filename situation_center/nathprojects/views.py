from django.shortcuts import render, get_object_or_404
import plotly.express as px
import pandas as pd

from .models import Hospital


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

    # Создание графика с помощью Plotly Express
    fig = px.line(df, x='year', y='deaths', title=f'{hospital.title}', markers=True,
                  labels={'year': 'Годы', 'deaths': 'Смертей'})

    # Преобразование графика в HTML
    chart = fig.to_html(full_html=False)

    context = {
        'chart': chart,
        'hospital': hospital,
    }
    return render(request, 'nathprojects/project_detail.html', context)
