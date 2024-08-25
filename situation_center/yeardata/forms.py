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


class FinanceForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        finance_slug = kwargs.pop('finance_slug')
        super(FinanceForm, self).__init__(*args, **kwargs)

        try:
            # Найти финансы по slug и загрузить CSV
            finance = Finance.objects.get(slug=finance_slug)
            csv_file_path = finance.csv_file.path
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


class ForeignTradingForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        foreigntrading_slug = kwargs.pop('foreigntrading_slug')
        super(ForeignTradingForm, self).__init__(*args, **kwargs)

        try:
            # Найти внешнюю торговлю по slug и загрузить CSV
            foreigntrading = ForeignTrading.objects.get(slug=foreigntrading_slug)
            csv_file_path = foreigntrading.csv_file.path
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


class LabourForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        labour_slug = kwargs.pop('labour_slug')
        super(LabourForm, self).__init__(*args, **kwargs)

        try:
            # Найти труд по slug и загрузить CSV
            labour = Labour.objects.get(slug=labour_slug)
            csv_file_path = labour.csv_file.path
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
            # Найти образование по slug и загрузить CSV
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
            # Найти культуру по slug и загрузить CSV
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


class VRPForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        vrp_slug = kwargs.pop('vrp_slug')
        super(VRPForm, self).__init__(*args, **kwargs)

        try:
            # Найти валовой региональный продукт по slug и загрузить CSV
            vrp = VRP.objects.get(slug=vrp_slug)
            csv_file_path = vrp.csv_file.path
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


class InvestingForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        investing_slug = kwargs.pop('investing_slug')
        super(InvestingForm, self).__init__(*args, **kwargs)

        try:
            # Найти инвестиции по slug и загрузить CSV
            investing = Investing.objects.get(slug=investing_slug)
            csv_file_path = investing.csv_file.path
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


class IndustrialProdForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        industrialprod_slug = kwargs.pop('industrialprod_slug')
        super(IndustrialProdForm, self).__init__(*args, **kwargs)

        try:
            # Найти промышленное производство по slug и загрузить CSV
            industrialprod = IndustrialProd.objects.get(slug=industrialprod_slug)
            csv_file_path = industrialprod.csv_file.path
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


class BuildingForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        building_slug = kwargs.pop('building_slug')
        super(BuildingForm, self).__init__(*args, **kwargs)

        try:
            # Найти строителство по slug и загрузить CSV
            building = Building.objects.get(slug=building_slug)
            csv_file_path = building.csv_file.path
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


class TransportForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        transport_slug = kwargs.pop('transport_slug')
        super(TransportForm, self).__init__(*args, **kwargs)

        try:
            # Найти транспорт по slug и загрузить CSV
            transport = Transport.objects.get(slug=transport_slug)
            csv_file_path = transport.csv_file.path
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


class ScienceForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        science_slug = kwargs.pop('science_slug')
        super(ScienceForm, self).__init__(*args, **kwargs)

        try:
            # Найти науку по slug и загрузить CSV
            science = Science.objects.get(slug=science_slug)
            csv_file_path = science.csv_file.path
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


class PriceForm(forms.Form):
    region = forms.ChoiceField(
        choices=[],  # Начальное значение, будет заменено в __init__
        label='Выберите регион',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        # Получаем slug больницы из kwargs
        price_slug = kwargs.pop('price_slug')
        super(PriceForm, self).__init__(*args, **kwargs)

        try:
            # Найти цену по slug и загрузить CSV
            price = Price.objects.get(slug=price_slug)
            csv_file_path = price.csv_file.path
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
