from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile
import pandas as pd
import tempfile


class PopulationDetailViewTests(TestCase):

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

        self.population = Population.objects.create(
            title="Test Population",
            slug="test-population",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_population_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:population_detail', args=[self.population.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_population_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:population_detail', args=[self.population.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_population_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:population_detail', args=[self.population.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_population_detail_with_invalid_csv(self):
        self.population.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.population.save()

        client = Client()
        response = client.get(reverse('yeardata:population_detail', args=[self.population.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class LevelHealthDetailViewTests(TestCase):

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

        self.levelhealth = LevelHealth.objects.create(
            title="Test LevelHealth",
            slug="test-levelhealth",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_levelhealth_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:levelhealth_detail', args=[self.levelhealth.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_levelhealth_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:levelhealth_detail', args=[self.levelhealth.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_levelhealth_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:levelhealth_detail', args=[self.levelhealth.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_levelhealth_detail_with_invalid_csv(self):
        self.levelhealth.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.levelhealth.save()

        client = Client()
        response = client.get(reverse('yeardata:levelhealth_detail', args=[self.levelhealth.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


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
            title="Test LevelHealth",
            slug="test-hospital",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_hospital_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:hospital_detail', args=[self.hospital.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_hospital_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:hospital_detail', args=[self.hospital.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_hospital_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:hospital_detail', args=[self.hospital.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_hospital_detail_with_invalid_csv(self):
        self.hospital.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.hospital.save()

        client = Client()
        response = client.get(reverse('yeardata:hospital_detail', args=[self.hospital.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class SecureNatureDetailViewTests(TestCase):

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

        self.securenature = SecureNature.objects.create(
            title="Test SecureNature",
            slug="test-securenature",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_securenature_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:securenature_detail', args=[self.securenature.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_securenature_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:securenature_detail', args=[self.securenature.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_securenature_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:securenature_detail', args=[self.securenature.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_securenature_detail_with_invalid_csv(self):
        self.securenature.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.securenature.save()

        client = Client()
        response = client.get(reverse('yeardata:securenature_detail', args=[self.securenature.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class CapitalAssetsDetailViewTests(TestCase):

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

        self.capitalassets = CapitalAssets.objects.create(
            title="Test CapitalAssets",
            slug="test-capitalassets",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_capitalassets_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:capitalassets_detail', args=[self.capitalassets.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_capitalassets_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:capitalassets_detail', args=[self.capitalassets.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_capitalassets_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:capitalassets_detail', args=[self.capitalassets.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_capitalassets_detail_with_invalid_csv(self):
        self.capitalassets.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.capitalassets.save()

        client = Client()
        response = client.get(reverse('yeardata:capitalassets_detail', args=[self.capitalassets.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class OrganizationDetailViewTests(TestCase):

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

        self.organization = Organization.objects.create(
            title="Test Organization",
            slug="test-organization",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_organization_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:organization_detail', args=[self.organization.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_organization_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:organization_detail', args=[self.organization.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_organization_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:organization_detail', args=[self.organization.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_organization_detail_with_invalid_csv(self):
        self.organization.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.organization.save()

        client = Client()
        response = client.get(reverse('yeardata:organization_detail', args=[self.organization.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class SHLRRDetailViewTests(TestCase):

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

        self.shlrr = SHLRR.objects.create(
            title="Test SHLRR",
            slug="test-shlrr",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_shlrr_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:shlrr_detail', args=[self.shlrr.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_shlrr_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:shlrr_detail', args=[self.shlrr.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_shlrr_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:shlrr_detail', args=[self.shlrr.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_shlrr_detail_with_invalid_csv(self):
        self.shlrr.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.shlrr.save()

        client = Client()
        response = client.get(reverse('yeardata:shlrr_detail', args=[self.shlrr.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class TradingDetailViewTests(TestCase):

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

        self.trading = Trading.objects.create(
            title="Test Trading",
            slug="test-trading",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_trading_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:trading_detail', args=[self.trading.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_trading_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:trading_detail', args=[self.trading.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_trading_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:trading_detail', args=[self.trading.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_trading_detail_with_invalid_csv(self):
        self.trading.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.trading.save()

        client = Client()
        response = client.get(reverse('yeardata:trading_detail', args=[self.trading.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class InfoTechnologyDetailViewTests(TestCase):

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

        self.infotechnology = InfoTechnology.objects.create(
            title="Test InfoTechnology",
            slug="test-infotechnology",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_infotechnology_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:infotechnology_detail', args=[self.infotechnology.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_infotechnology_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:infotechnology_detail', args=[self.infotechnology.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_infotechnology_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:infotechnology_detail', args=[self.infotechnology.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_infotechnology_detail_with_invalid_csv(self):
        self.infotechnology.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.infotechnology.save()

        client = Client()
        response = client.get(reverse('yeardata:infotechnology_detail', args=[self.infotechnology.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class FinanceDetailViewTests(TestCase):

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

        self.finance = Finance.objects.create(
            title="Test Finance",
            slug="test-finance",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_finance_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:finance_detail', args=[self.finance.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_finance_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:finance_detail', args=[self.finance.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_finance_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:finance_detail', args=[self.finance.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_finance_detail_with_invalid_csv(self):
        self.finance.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.finance.save()

        client = Client()
        response = client.get(reverse('yeardata:finance_detail', args=[self.finance.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class ForeignTradingDetailViewTests(TestCase):

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

        self.foreigntrading = ForeignTrading.objects.create(
            title="Test ForeignTrading",
            slug="test-foreigntrading",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_foreigntrading_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:foreigntrading_detail', args=[self.foreigntrading.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_foreigntrading_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:foreigntrading_detail', args=[self.foreigntrading.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_foreigntrading_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:foreigntrading_detail', args=[self.foreigntrading.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_foreigntrading_detail_with_invalid_csv(self):
        self.foreigntrading.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.foreigntrading.save()

        client = Client()
        response = client.get(reverse('yeardata:foreigntrading_detail', args=[self.foreigntrading.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class LabourDetailViewTests(TestCase):

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

        self.labour = Labour.objects.create(
            title="Test Labour",
            slug="test-labour",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_labour_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:labour_detail', args=[self.labour.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_labour_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:labour_detail', args=[self.labour.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_labour_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:labour_detail', args=[self.labour.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_labour_detail_with_invalid_csv(self):
        self.labour.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.labour.save()

        client = Client()
        response = client.get(reverse('yeardata:labour_detail', args=[self.labour.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class StudyDetailViewTests(TestCase):

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

        self.study = Study.objects.create(
            title="Test Study",
            slug="test-study",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_study_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:study_detail', args=[self.study.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_study_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:study_detail', args=[self.study.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_study_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:study_detail', args=[self.study.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_study_detail_with_invalid_csv(self):
        self.study.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.study.save()

        client = Client()
        response = client.get(reverse('yeardata:study_detail', args=[self.study.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class CultureDetailViewTests(TestCase):

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

        self.culture = Culture.objects.create(
            title="Test Culture",
            slug="test-culture",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_culture_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:culture_detail', args=[self.culture.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_culture_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:culture_detail', args=[self.culture.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_culture_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:culture_detail', args=[self.culture.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_culture_detail_with_invalid_csv(self):
        self.culture.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.culture.save()

        client = Client()
        response = client.get(reverse('yeardata:culture_detail', args=[self.culture.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class VRPDetailViewTests(TestCase):

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

        self.vrp = VRP.objects.create(
            title="Test VRP",
            slug="test-vrp",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_vrp_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:vrp_detail', args=[self.vrp.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_vrp_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:vrp_detail', args=[self.vrp.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_vrp_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:vrp_detail', args=[self.vrp.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_vrp_detail_with_invalid_csv(self):
        self.vrp.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.vrp.save()

        client = Client()
        response = client.get(reverse('yeardata:vrp_detail', args=[self.vrp.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class InvestingDetailViewTests(TestCase):

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

        self.investing = Investing.objects.create(
            title="Test Investing",
            slug="test-investing",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_investing_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:investing_detail', args=[self.investing.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_investing_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:investing_detail', args=[self.investing.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_investing_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:investing_detail', args=[self.investing.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_investing_detail_with_invalid_csv(self):
        self.investing.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.investing.save()

        client = Client()
        response = client.get(reverse('yeardata:investing_detail', args=[self.investing.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class IndustrialProdDetailViewTests(TestCase):

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

        self.industrialprod = IndustrialProd.objects.create(
            title="Test IndustrialProd",
            slug="test-industrialprod",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_industrialprod_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:industrialprod_detail', args=[self.industrialprod.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_industrialprod_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:industrialprod_detail', args=[self.industrialprod.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_industrialprod_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:industrialprod_detail', args=[self.industrialprod.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_industrialprod_detail_with_invalid_csv(self):
        self.industrialprod.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.industrialprod.save()

        client = Client()
        response = client.get(reverse('yeardata:industrialprod_detail', args=[self.industrialprod.slug]))
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
        response = client.get(reverse('yeardata:building_detail', args=[self.building.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_building_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:building_detail', args=[self.building.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_building_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:building_detail', args=[self.building.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_building_detail_with_invalid_csv(self):
        self.building.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.building.save()

        client = Client()
        response = client.get(reverse('yeardata:building_detail', args=[self.building.slug]))
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
        response = client.get(reverse('yeardata:transport_detail', args=[self.transport.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_transport_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:transport_detail', args=[self.transport.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_transport_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:transport_detail', args=[self.transport.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_transport_detail_with_invalid_csv(self):
        self.transport.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.transport.save()

        client = Client()
        response = client.get(reverse('yeardata:transport_detail', args=[self.transport.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class ScienceDetailViewTests(TestCase):

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

        self.science = Science.objects.create(
            title="Test Science",
            slug="test-science",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_science_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:science_detail', args=[self.science.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_science_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:science_detail', args=[self.science.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_science_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:science_detail', args=[self.science.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_science_detail_with_invalid_csv(self):
        self.science.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.science.save()

        client = Client()
        response = client.get(reverse('yeardata:science_detail', args=[self.science.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class PriceDetailViewTests(TestCase):

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

        self.price = Price.objects.create(
            title="Test Price",
            slug="test-price",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_price_detail_success(self):
        client = Client()
        response = client.get(reverse('yeardata:price_detail', args=[self.price.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_price_detail_with_region(self):
        client = Client()
        response = client.get(reverse('yeardata:price_detail', args=[self.price.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_price_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('yeardata:price_detail', args=[self.price.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_price_detail_with_invalid_csv(self):
        self.price.csv_file = SimpleUploadedFile("test.csv", b"invalid,data")
        self.price.save()

        client = Client()
        response = client.get(reverse('yeardata:price_detail', args=[self.price.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")
