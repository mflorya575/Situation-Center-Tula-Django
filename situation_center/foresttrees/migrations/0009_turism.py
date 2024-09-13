# Generated by Django 4.2.8 on 2024-09-13 09:13

from django.db import migrations, models
import foresttrees.models


class Migration(migrations.Migration):

    dependencies = [
        ('foresttrees', '0008_business'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('csv_file', models.FileField(blank=True, null=True, upload_to=foresttrees.models.csv_upload_to, verbose_name='CSV файл')),
            ],
            options={
                'verbose_name': 'Туризм',
                'verbose_name_plural': 'Туризм',
            },
        ),
    ]
