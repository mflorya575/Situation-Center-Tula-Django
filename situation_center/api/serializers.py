from rest_framework import serializers

from nathprojects.models import *
# from operdata.models import *
# from yeardata.models import *


class HospitalDetailSerializer(serializers.ModelSerializer):
    combined_chart_linear = serializers.CharField()
    combined_chart_log = serializers.CharField()
    map_chart_linear = serializers.CharField()
    map_chart_log = serializers.CharField()
    table_html = serializers.CharField()

    class Meta:
        model = Hospital
        fields = ['id', 'title', 'slug', 'combined_chart_linear', 'combined_chart_log', 'map_chart_linear', 'map_chart_log', 'table_html']


class StudyDetailSerializer(serializers.ModelSerializer):
    combined_chart_linear = serializers.CharField()
    combined_chart_log = serializers.CharField()
    map_chart_linear = serializers.CharField()
    map_chart_log = serializers.CharField()
    table_html = serializers.CharField()

    class Meta:
        model = Study
        fields = ['id', 'title', 'slug', 'combined_chart_linear', 'combined_chart_log', 'map_chart_linear', 'map_chart_log', 'table_html']


class DemographicsDetailSerializer(serializers.ModelSerializer):
    combined_chart_linear = serializers.CharField()
    combined_chart_log = serializers.CharField()
    map_chart_linear = serializers.CharField()
    map_chart_log = serializers.CharField()
    table_html = serializers.CharField()

    class Meta:
        model = Demographics
        fields = ['id', 'title', 'slug', 'combined_chart_linear', 'combined_chart_log', 'map_chart_linear', 'map_chart_log', 'table_html']
