# Generated by Django 4.2.8 on 2024-08-22 20:35

from django.db import migrations, models
import operdata.models


class Migration(migrations.Migration):

    dependencies = [
        ('operdata', '0007_investing'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinPr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('csv_file', models.FileField(blank=True, null=True, upload_to=operdata.models.csv_upload_to, verbose_name='CSV файл')),
            ],
            options={
                'verbose_name': 'Финансы предприятий',
                'verbose_name_plural': 'Финансы предприятий',
            },
        ),
    ]
