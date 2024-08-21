# Generated by Django 4.2.8 on 2024-08-21 13:37

from django.db import migrations, models
import nathprojects.models


class Migration(migrations.Migration):

    dependencies = [
        ('nathprojects', '0015_atom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('csv_file', models.FileField(blank=True, null=True, upload_to=nathprojects.models.csv_upload_to, verbose_name='CSV файл')),
            ],
            options={
                'verbose_name': 'Магистральная',
                'verbose_name_plural': 'Магистральная',
            },
        ),
    ]
