from django import forms
import pandas as pd

from .models import *


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
