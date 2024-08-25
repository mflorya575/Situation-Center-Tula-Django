from django import forms
import pandas as pd

from .models import *


class PopulationForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        population_slug = kwargs.pop('population_slug')
        super(PopulationForm, self).__init__(*args, **kwargs)

        try:
            # Найти население по slug и загрузить CSV
            population = Population.objects.get(slug=population_slug)
            csv_file_path = population.csv_file.path
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


class LevelHealthForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        levelhealth_slug = kwargs.pop('levelhealth_slug')
        super(LevelHealthForm, self).__init__(*args, **kwargs)

        try:
            # Найти уровень жизни населения по slug и загрузить CSV
            levelhealth = LevelHealth.objects.get(slug=levelhealth_slug)
            csv_file_path = levelhealth.csv_file.path
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


class HospitalForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        hospital_slug = kwargs.pop('hospital_slug')
        super(HospitalForm, self).__init__(*args, **kwargs)

        try:
            # Найти здравоохранение по slug и загрузить CSV
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


class SecureNatureForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        securenature_slug = kwargs.pop('securenature_slug')
        super(SecureNatureForm, self).__init__(*args, **kwargs)

        try:
            # Найти охрану природы по slug и загрузить CSV
            securenature = SecureNature.objects.get(slug=securenature_slug)
            csv_file_path = securenature.csv_file.path
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


class CapitalAssetsForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        capitalassets_slug = kwargs.pop('capitalassets_slug')
        super(CapitalAssetsForm, self).__init__(*args, **kwargs)

        try:
            # Найти основные фонды по slug и загрузить CSV
            capitalassets = CapitalAssets.objects.get(slug=capitalassets_slug)
            csv_file_path = capitalassets.csv_file.path
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


class OrganizationForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        organization_slug = kwargs.pop('organization_slug')
        super(OrganizationForm, self).__init__(*args, **kwargs)

        try:
            # Найти организации по slug и загрузить CSV
            organization = Organization.objects.get(slug=organization_slug)
            csv_file_path = organization.csv_file.path
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


class SHLRRForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        shlrr_slug = kwargs.pop('shlrr_slug')
        super(SHLRRForm, self).__init__(*args, **kwargs)

        try:
            # Найти с/х и т.д. по slug и загрузить CSV
            shlrr = SHLRR.objects.get(slug=shlrr_slug)
            csv_file_path = shlrr.csv_file.path
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


class TradingForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        trading_slug = kwargs.pop('trading_slug')
        super(TradingForm, self).__init__(*args, **kwargs)

        try:
            # Найти торговлю по slug и загрузить CSV
            trading = Trading.objects.get(slug=trading_slug)
            csv_file_path = trading.csv_file.path
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


class InfoTechnologyForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        infotechnology_slug = kwargs.pop('infotechnology_slug')
        super(InfoTechnologyForm, self).__init__(*args, **kwargs)

        try:
            # Найти информационные технологии по slug и загрузить CSV
            infotechnology = InfoTechnology.objects.get(slug=infotechnology_slug)
            csv_file_path = infotechnology.csv_file.path
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
