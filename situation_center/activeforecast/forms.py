from django import forms
import pandas as pd

from foresttrees.models import *


class RegionForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        hospital_slug = kwargs.pop('hospital_slug')
        super(RegionForm, self).__init__(*args, **kwargs)

        try:
            # Найти больницу по slug и загрузить CSV
            hospital = Hospital.objects.get(slug=hospital_slug)
            csv_file_path = hospital.csv_file.path
            df = pd.read_csv(csv_file_path)

            # Проверьте, что столбец 'region' присутствует
            if 'region' not in df.columns:
                raise ValueError("Столбец 'region' не найден в CSV-файле.")

            # Получить уникальные регионы из CSV-файла
            unique_regions = df['region'].unique()

            # Обновить choices на основе данных из CSV
            self.fields['region'].choices = [(region, region) for region in unique_regions]

        except Exception as e:
            # Обработка ошибок чтения файла или поиска больницы
            print(f"Ошибка: {e}")
            self.fields['region'].choices = [('Ошибка', 'Ошибка загрузки данных')]


class StudyForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        study_slug = kwargs.pop('study_slug')
        super(StudyForm, self).__init__(*args, **kwargs)

        try:
            # Найти больницу по slug и загрузить CSV
            study = Study.objects.get(slug=study_slug)
            csv_file_path = study.csv_file.path
            df = pd.read_csv(csv_file_path)

            # Проверьте, что столбец 'region' присутствует
            if 'region' not in df.columns:
                raise ValueError("Столбец 'region' не найден в CSV-файле.")

            # Получить уникальные регионы из CSV-файла
            unique_regions = df['region'].unique()

            # Обновить choices на основе данных из CSV
            self.fields['region'].choices = [(region, region) for region in unique_regions]

        except Exception as e:
            # Обработка ошибок чтения файла или поиска больницы
            print(f"Ошибка: {e}")
            self.fields['region'].choices = [('Ошибка', 'Ошибка загрузки данных')]


class DemographicsForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        demographics_slug = kwargs.pop('demographics_slug')
        super(DemographicsForm, self).__init__(*args, **kwargs)

        try:
            # Найти больницу по slug и загрузить CSV
            demographics = Demographics.objects.get(slug=demographics_slug)
            csv_file_path = demographics.csv_file.path
            df = pd.read_csv(csv_file_path)

            # Проверьте, что столбец 'region' присутствует
            if 'region' not in df.columns:
                raise ValueError("Столбец 'region' не найден в CSV-файле.")

            # Получить уникальные регионы из CSV-файла
            unique_regions = df['region'].unique()

            # Обновить choices на основе данных из CSV
            self.fields['region'].choices = [(region, region) for region in unique_regions]

        except Exception as e:
            # Обработка ошибок чтения файла или поиска больницы
            print(f"Ошибка: {e}")
            self.fields['region'].choices = [('Ошибка', 'Ошибка загрузки данных')]


class CultureForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        culture_slug = kwargs.pop('culture_slug')
        super(CultureForm, self).__init__(*args, **kwargs)

        try:
            # Найти больницу по slug и загрузить CSV
            culture = Culture.objects.get(slug=culture_slug)
            csv_file_path = culture.csv_file.path
            df = pd.read_csv(csv_file_path)

            # Проверьте, что столбец 'region' присутствует
            if 'region' not in df.columns:
                raise ValueError("Столбец 'region' не найден в CSV-файле.")

            # Получить уникальные регионы из CSV-файла
            unique_regions = df['region'].unique()

            # Обновить choices на основе данных из CSV
            self.fields['region'].choices = [(region, region) for region in unique_regions]

        except Exception as e:
            # Обработка ошибок чтения файла или поиска больницы
            print(f"Ошибка: {e}")
            self.fields['region'].choices = [('Ошибка', 'Ошибка загрузки данных')]


class RoadForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        road_slug = kwargs.pop('road_slug')
        super(RoadForm, self).__init__(*args, **kwargs)

        try:
            # Найти больницу по slug и загрузить CSV
            road = Road.objects.get(slug=road_slug)
            csv_file_path = road.csv_file.path
            df = pd.read_csv(csv_file_path)

            # Проверьте, что столбец 'region' присутствует
            if 'region' not in df.columns:
                raise ValueError("Столбец 'region' не найден в CSV-файле.")

            # Получить уникальные регионы из CSV-файла
            unique_regions = df['region'].unique()

            # Обновить choices на основе данных из CSV
            self.fields['region'].choices = [(region, region) for region in unique_regions]

        except Exception as e:
            # Обработка ошибок чтения файла или поиска больницы
            print(f"Ошибка: {e}")
            self.fields['region'].choices = [('Ошибка', 'Ошибка загрузки данных')]
