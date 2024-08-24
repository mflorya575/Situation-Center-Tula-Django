# Generated by Django 4.2.8 on 2024-08-24 09:44

from django.db import migrations, models
import yeardata.models


class Migration(migrations.Migration):

    dependencies = [
        ('yeardata', '0018_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('csv_file', models.FileField(blank=True, null=True, upload_to=yeardata.models.csv_upload_to, verbose_name='CSV файл')),
            ],
            options={
                'verbose_name': 'Транспорт',
                'verbose_name_plural': 'Транспорт',
            },
        ),
    ]
