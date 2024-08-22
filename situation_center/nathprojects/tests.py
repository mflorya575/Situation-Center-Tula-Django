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
        response = client.get(reverse('nathprojects:study_detail', args=[self.study.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_study_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:study_detail', args=[self.study.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_study_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:study_detail', args=[self.study.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_study_detail_with_invalid_csv(self):
        self.study.csv_file = SimpleUploadedFile("test2.csv", b"invalid,data")
        self.study.save()

        client = Client()
        response = client.get(reverse('nathprojects:study_detail', args=[self.study.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class DemographicsDetailViewTests(TestCase):

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

        self.demographics = Demographics.objects.create(
            title="Test Demographics",
            slug="test-demographics",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_study_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:demographics_detail', args=[self.demographics.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_demographics_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:demographics_detail', args=[self.demographics.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_demographics_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:demographics_detail', args=[self.demographics.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_demographics_detail_with_invalid_csv(self):
        self.demographics.csv_file = SimpleUploadedFile("test3.csv", b"invalid,data")
        self.demographics.save()

        client = Client()
        response = client.get(reverse('nathprojects:demographics_detail', args=[self.demographics.slug]))
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
        response = client.get(reverse('nathprojects:culture_detail', args=[self.culture.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_culture_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:culture_detail', args=[self.culture.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_culture_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:culture_detail', args=[self.culture.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_culture_detail_with_invalid_csv(self):
        self.culture.csv_file = SimpleUploadedFile("test4.csv", b"invalid,data")
        self.culture.save()

        client = Client()
        response = client.get(reverse('nathprojects:culture_detail', args=[self.culture.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class RoadDetailViewTests(TestCase):

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

        self.road = Road.objects.create(
            title="Test Road",
            slug="test-road",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_road_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:road_detail', args=[self.road.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_road_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:road_detail', args=[self.road.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_road_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:road_detail', args=[self.road.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_road_detail_with_invalid_csv(self):
        self.road.csv_file = SimpleUploadedFile("test5.csv", b"invalid,data")
        self.road.save()

        client = Client()
        response = client.get(reverse('nathprojects:road_detail', args=[self.road.slug]))
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
        response = client.get(reverse('nathprojects:science_detail', args=[self.science.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_science_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:science_detail', args=[self.science.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_science_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:science_detail', args=[self.science.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_science_detail_with_invalid_csv(self):
        self.science.csv_file = SimpleUploadedFile("test6.csv", b"invalid,data")
        self.science.save()

        client = Client()
        response = client.get(reverse('nathprojects:science_detail', args=[self.science.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class EcologyDetailViewTests(TestCase):

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

        self.ecology = Ecology.objects.create(
            title="Test Ecology",
            slug="test-ecology",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_ecology_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:ecology_detail', args=[self.ecology.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_ecology_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:ecology_detail', args=[self.ecology.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_ecology_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:ecology_detail', args=[self.ecology.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_ecology_detail_with_invalid_csv(self):
        self.ecology.csv_file = SimpleUploadedFile("test7.csv", b"invalid,data")
        self.ecology.save()

        client = Client()
        response = client.get(reverse('nathprojects:ecology_detail', args=[self.ecology.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class BusinessDetailViewTests(TestCase):

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

        self.business = Business.objects.create(
            title="Test Business",
            slug="test-business",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_business_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:business_detail', args=[self.business.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_business_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:business_detail', args=[self.business.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_business_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:business_detail', args=[self.business.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_business_detail_with_invalid_csv(self):
        self.business.csv_file = SimpleUploadedFile("test8.csv", b"invalid,data")
        self.business.save()

        client = Client()
        response = client.get(reverse('nathprojects:business_detail', args=[self.business.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class TurismDetailViewTests(TestCase):

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

        self.turism = Turism.objects.create(
            title="Test Turism",
            slug="test-turism",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_turism_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:turism_detail', args=[self.turism.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_turism_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:turism_detail', args=[self.turism.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_turism_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:turism_detail', args=[self.turism.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_turism_detail_with_invalid_csv(self):
        self.turism.csv_file = SimpleUploadedFile("test9.csv", b"invalid,data")
        self.turism.save()

        client = Client()
        response = client.get(reverse('nathprojects:turism_detail', args=[self.turism.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class HouseDetailViewTests(TestCase):

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

        self.house = House.objects.create(
            title="Test House",
            slug="test-house",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_house_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:house_detail', args=[self.house.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_house_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:house_detail', args=[self.house.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_house_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:house_detail', args=[self.house.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_house_detail_with_invalid_csv(self):
        self.house.csv_file = SimpleUploadedFile("test10.csv", b"invalid,data")
        self.house.save()

        client = Client()
        response = client.get(reverse('nathprojects:house_detail', args=[self.house.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class WorldDetailViewTests(TestCase):

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

        self.world = World.objects.create(
            title="Test World",
            slug="test-world",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_world_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:world_detail', args=[self.world.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_world_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:world_detail', args=[self.world.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_world_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:world_detail', args=[self.world.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_world_detail_with_invalid_csv(self):
        self.world.csv_file = SimpleUploadedFile("test11.csv", b"invalid,data")
        self.world.save()

        client = Client()
        response = client.get(reverse('nathprojects:world_detail', args=[self.world.slug]))
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
        response = client.get(reverse('nathprojects:labour_detail', args=[self.labour.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_labour_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:labour_detail', args=[self.labour.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_labour_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:labour_detail', args=[self.labour.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_labour_detail_with_invalid_csv(self):
        self.labour.csv_file = SimpleUploadedFile("test12.csv", b"invalid,data")
        self.labour.save()

        client = Client()
        response = client.get(reverse('nathprojects:labour_detail', args=[self.labour.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class AtomDetailViewTests(TestCase):

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

        self.atom = Atom.objects.create(
            title="Test Atom",
            slug="test-atom",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_atom_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:atom_detail', args=[self.atom.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_atom_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:atom_detail', args=[self.atom.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_atom_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:atom_detail', args=[self.atom.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_atom_detail_with_invalid_csv(self):
        self.atom.csv_file = SimpleUploadedFile("test13.csv", b"invalid,data")
        self.atom.save()

        client = Client()
        response = client.get(reverse('nathprojects:atom_detail', args=[self.atom.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class EconomDetailViewTests(TestCase):

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

        self.econom = Econom.objects.create(
            title="Test Econom",
            slug="test-econom",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_econom_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:econom_detail', args=[self.econom.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_econom_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:econom_detail', args=[self.econom.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_econom_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:econom_detail', args=[self.econom.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_econom_detail_with_invalid_csv(self):
        self.econom.csv_file = SimpleUploadedFile("test14.csv", b"invalid,data")
        self.econom.save()

        client = Client()
        response = client.get(reverse('nathprojects:econom_detail', args=[self.econom.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")


class MainlineDetailViewTests(TestCase):

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

        self.mainline = Mainline.objects.create(
            title="Test Mainline",
            slug="test-mainline",
            csv_file=SimpleUploadedFile("test.csv", open(self.temp_csv.name, 'rb').read())
        )

    def tearDown(self):
        self.temp_csv.close()

    # Тест успешного получения страницы
    def test_mainline_detail_success(self):
        client = Client()
        response = client.get(reverse('nathprojects:mainline_detail', args=[self.mainline.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Российская Федерация")

    # Тест с выбранным регионом
    def test_mainline_detail_with_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:mainline_detail', args=[self.mainline.slug]),
                              {'region': 'Белгородская область'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Белгородская область")

    # Тест, если регион не найден
    def test_mainline_detail_with_nonexistent_region(self):
        client = Client()
        response = client.get(reverse('nathprojects:mainline_detail', args=[self.mainline.slug]),
                              {'region': 'Nonexistent Region'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Нет данных для отображения.")

    # Тест обработки ошибок с некорректным CSV-файлом
    def test_mainline_detail_with_invalid_csv(self):
        self.mainline.csv_file = SimpleUploadedFile("test15.csv", b"invalid,data")
        self.mainline.save()

        client = Client()
        response = client.get(reverse('nathprojects:mainline_detail', args=[self.mainline.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ошибка при обработке данных")
