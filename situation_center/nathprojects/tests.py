from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile
import pandas as pd
import tempfile


class HospitalDetailViewTests(TestCase):

    def setUp(self):
        # Создание временного CSV-файла с корректными данными
        csv_data = (
            "region,2018,2019,2020,2021,2022\n"
            "Российская Федерация,482.2,470,521.6,560,491.4\n"
            "Центральный федеральный округ,446.7,435.2,496.4,543.2,454\n"
            "Белгородская область,422.5,415.8,472.6,507.6,459.1\n"
        )
        self.temp_csv = tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode='w', newline='', encoding='utf-8')
        self.temp_csv.write(csv_data)
        self.temp_csv.close()

        self.hospital = Hospital.objects.create(
            title="Test Hospital",
            slug="test-hospital",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_hospital_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:hospital_detail', args=[self.hospital.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_hospital_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:hospital_detail', args=[self.hospital.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_hospital_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:hospital_detail', args=[self.hospital.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_hospital_detail_with_invalid_csv(self):
        self.hospital.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.hospital.save()

        client = Client()
        response = client.get(reverse('nathprojects:hospital_detail', args=[self.hospital.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")
