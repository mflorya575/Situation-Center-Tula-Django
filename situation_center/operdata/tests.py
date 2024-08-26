from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile
import pandas as pd
import tempfile


class IndustryDetailViewTests(TestCase):

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

        self.industry = Industry.objects.create(
            title="Test Industry",
            slug="test-industry",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_industry_detail_success(self):
        client = Client()
        response = client.get(reverse('operdata:industry_detail', args=[self.industry.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_industry_detail_with_region(self):
        client = Client()
        response = client.get(reverse('operdata:industry_detail', args=[self.industry.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_industry_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('operdata:industry_detail', args=[self.industry.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_industry_detail_with_invalid_csv(self):
        self.industry.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.industry.save()

        client = Client()
        response = client.get(reverse('operdata:industry_detail', args=[self.industry.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class AgroDetailViewTests(TestCase):

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

        self.agro = Agro.objects.create(
            title="Test Agro",
            slug="test-agro",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_agro_detail_success(self):
        client = Client()
        response = client.get(reverse('operdata:agro_detail', args=[self.agro.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_agro_detail_with_region(self):
        client = Client()
        response = client.get(reverse('operdata:agro_detail', args=[self.agro.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_agro_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('operdata:agro_detail', args=[self.agro.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_agro_detail_with_invalid_csv(self):
        self.agro.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.agro.save()

        client = Client()
        response = client.get(reverse('operdata:agro_detail', args=[self.agro.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class BuildingDetailViewTests(TestCase):

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

        self.building = Building.objects.create(
            title="Test Building",
            slug="test-building",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_building_detail_success(self):
        client = Client()
        response = client.get(reverse('operdata:building_detail', args=[self.building.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_building_detail_with_region(self):
        client = Client()
        response = client.get(reverse('operdata:building_detail', args=[self.building.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_building_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('operdata:building_detail', args=[self.building.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_building_detail_with_invalid_csv(self):
        self.building.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.building.save()

        client = Client()
        response = client.get(reverse('operdata:building_detail', args=[self.building.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class TransportDetailViewTests(TestCase):

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

        self.transport = Transport.objects.create(
            title="Test Transport",
            slug="test-transport",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_transport_detail_success(self):
        client = Client()
        response = client.get(reverse('operdata:transport_detail', args=[self.transport.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_transport_detail_with_region(self):
        client = Client()
        response = client.get(reverse('operdata:transport_detail', args=[self.transport.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_transport_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('operdata:transport_detail', args=[self.transport.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_transport_detail_with_invalid_csv(self):
        self.transport.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.transport.save()

        client = Client()
        response = client.get(reverse('operdata:transport_detail', args=[self.transport.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")
