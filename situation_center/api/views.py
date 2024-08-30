import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from nathprojects.models import *
# from operdata.models import *
# from yeardata.models import *


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


class StudyDetailAPIView(APIView):
    def get(self, request, slug):
        study = get_object_or_404(Study, slug=slug)

        # Чтение CSV файла
        csv_file_path = study.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": study.id,
            "title": study.title,
            "slug": study.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class DemographicsDetailAPIView(APIView):
    def get(self, request, slug):
        demographics = get_object_or_404(Demographics, slug=slug)

        # Чтение CSV файла
        csv_file_path = demographics.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": demographics.id,
            "title": demographics.title,
            "slug": demographics.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class CultureDetailAPIView(APIView):
    def get(self, request, slug):
        culture = get_object_or_404(Culture, slug=slug)

        # Чтение CSV файла
        csv_file_path = culture.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": culture.id,
            "title": culture.title,
            "slug": culture.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class RoadDetailAPIView(APIView):
    def get(self, request, slug):
        road = get_object_or_404(Road, slug=slug)

        # Чтение CSV файла
        csv_file_path = road.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": road.id,
            "title": road.title,
            "slug": road.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class ScienceDetailAPIView(APIView):
    def get(self, request, slug):
        science = get_object_or_404(Science, slug=slug)

        # Чтение CSV файла
        csv_file_path = science.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": science.id,
            "title": science.title,
            "slug": science.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class EcologyDetailAPIView(APIView):
    def get(self, request, slug):
        ecology = get_object_or_404(Ecology, slug=slug)

        # Чтение CSV файла
        csv_file_path = ecology.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": ecology.id,
            "title": ecology.title,
            "slug": ecology.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class BusinessDetailAPIView(APIView):
    def get(self, request, slug):
        business = get_object_or_404(Business, slug=slug)

        # Чтение CSV файла
        csv_file_path = business.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": business.id,
            "title": business.title,
            "slug": business.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class TurismDetailAPIView(APIView):
    def get(self, request, slug):
        turism = get_object_or_404(Turism, slug=slug)

        # Чтение CSV файла
        csv_file_path = turism.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": turism.id,
            "title": turism.title,
            "slug": turism.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class HouseDetailAPIView(APIView):
    def get(self, request, slug):
        house = get_object_or_404(House, slug=slug)

        # Чтение CSV файла
        csv_file_path = house.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": house.id,
            "title": house.title,
            "slug": house.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class WorldDetailAPIView(APIView):
    def get(self, request, slug):
        world = get_object_or_404(World, slug=slug)

        # Чтение CSV файла
        csv_file_path = world.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": world.id,
            "title": world.title,
            "slug": world.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class LabourDetailAPIView(APIView):
    def get(self, request, slug):
        labour = get_object_or_404(Labour, slug=slug)

        # Чтение CSV файла
        csv_file_path = labour.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": labour.id,
            "title": labour.title,
            "slug": labour.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class AtomDetailAPIView(APIView):
    def get(self, request, slug):
        atom = get_object_or_404(Atom, slug=slug)

        # Чтение CSV файла
        csv_file_path = atom.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": atom.id,
            "title": atom.title,
            "slug": atom.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class EconomDetailAPIView(APIView):
    def get(self, request, slug):
        econom = get_object_or_404(Econom, slug=slug)

        # Чтение CSV файла
        csv_file_path = econom.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": econom.id,
            "title": econom.title,
            "slug": econom.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)


class MainlineDetailAPIView(APIView):
    def get(self, request, slug):
        mainline = get_object_or_404(Mainline, slug=slug)

        # Чтение CSV файла
        csv_file_path = mainline.csv_file.path
        df = pd.read_csv(csv_file_path)

        # Преобразование данных
        df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

        # Формирование данных для API
        years = df.columns[1:]  # Первый столбец — region, остальные — года
        data_data = df[df['region'] == 'Российская Федерация'].iloc[0, 1:].tolist()  # Пример для одного региона

        data = {
            "years": years.tolist(),
            "data": data_data
        }

        charts = {
            "linear": {
                "type": "line",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Смертность", "data": data_data}
                ]
            },
            "bar": {
                "type": "bar",
                "labels": years.tolist(),
                "datasets": [
                    {"label": "Количество", "data": data_data}
                ]
            }
        }

        # Формирование ответа
        response = {
            "id": mainline.id,
            "title": mainline.title,
            "slug": mainline.slug,
            "data": data,
            "charts": charts
        }
        return Response(response)
