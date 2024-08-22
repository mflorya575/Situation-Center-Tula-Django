import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from nathprojects.models import *


class HospitalDetailAPIView(APIView):
    def get(self, request, slug):
        hospital = get_object_or_404(Hospital, slug=slug)

        # Чтение CSV файла
        csv_file_path = hospital.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='deaths')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        deaths_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "deaths": deaths_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": deaths_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": deaths_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": hospital.id,
            "title": hospital.title,
            "slug": hospital.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)
