from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from nathprojects.models import *
from .serializers import *
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


class HospitalDetailAPIView(APIView):
    def get(self, request, slug):
        hospital = get_object_or_404(Hospital, slug=slug)

        csv_file_path = hospital.csv_file.path

        try:
            # Загрузка данных из CSV
            df = pd.read_csv(csv_file_path)

            if 'region' not in df.columns:
                return Response({"error": "Столбец 'region' не найден в CSV-файле."}, status=status.HTTP_400_BAD_REQUEST)

            selected_region = request.GET.get('region')
            if selected_region:
                df = df[df['region'] == selected_region]

            df_melted = df.melt(id_vars=['region'], var_name='year', value_name='deaths')
            df['region'] = df['region'].str.strip()

            if df_melted.empty:
                combined_chart_linear = "Нет данных для отображения."
                map_chart_linear = "Нет данных для отображения на карте."
            else:
                fig_linear = go.Figure()
                fig_linear.add_trace(go.Scatter(x=df_melted['year'], y=df_melted['deaths'], mode='lines+markers', name='Линейный график'))
                fig_linear.add_trace(go.Bar(x=df_melted['year'], y=df_melted['deaths'], name='Столбчатая диаграмма'))
                fig_linear.update_layout(
                    title=f'{hospital.title} - Комбинированный график (Линейная шкала)',
                    xaxis_title='Годы',
                    yaxis_title='Смертей'
                )
                combined_chart_linear = fig_linear.to_html(full_html=False)

                fig_log = go.Figure()
                fig_log.add_trace(go.Scatter(x=df_melted['year'], y=df_melted['deaths'], mode='lines+markers', name='Линейный график'))
                fig_log.add_trace(go.Bar(x=df_melted['year'], y=df_melted['deaths'], name='Столбчатая диаграмма'))
                fig_log.update_layout(
                    title=f'{hospital.title} - Комбинированный график (Логарифмическая шкала)',
                    xaxis_title='Годы',
                    yaxis_title='Смертей',
                    yaxis_type='log'
                )
                combined_chart_log = fig_log.to_html(full_html=False)

                latest_year = df_melted['year'].max()
                df_latest = df_melted[df_melted['year'] == latest_year]

                map_fig_linear = px.choropleth(df_latest,
                                               locations='region',
                                               geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                               featureidkey="properties.name",
                                               color='deaths',
                                               hover_name='region',
                                               title=f'{hospital.title} - {latest_year} (Линейная шкала)',
                                               color_continuous_scale='Reds')
                map_fig_linear.update_geos(fitbounds="locations", visible=False)
                map_chart_linear = map_fig_linear.to_html(full_html=False)

                map_fig_log = px.choropleth(df_latest,
                                            locations='region',
                                            geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson',
                                            featureidkey="properties.name",
                                            color='deaths',
                                            hover_name='region',
                                            title=f'{hospital.title} - {latest_year} (Логарифмическая шкала)',
                                            color_continuous_scale='Reds',
                                            range_color=[df_latest['deaths'].min(), df_latest['deaths'].max()],
                                            color_continuous_midpoint=0.1)
                map_fig_log.update_geos(fitbounds="locations", visible=False)
                map_chart_log = map_fig_log.to_html(full_html=False)

                table_html = df.to_html(index=False, classes='table table-striped')

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        data = {
            'id': hospital.id,
            'title': hospital.title,
            'slug': hospital.slug,
            'combined_chart_linear': combined_chart_linear,
            'combined_chart_log': combined_chart_log,
            'map_chart_linear': map_chart_linear,
            'map_chart_log': map_chart_log,
            'table_html': table_html
        }
        return Response(data, status=status.HTTP_200_OK)
