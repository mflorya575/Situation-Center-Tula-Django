# Generated by Django 4.2.8 on 2024-08-14 14:12

from django.db import migrations, models
import nathprojects.models


class Migration(migrations.Migration):

    dependencies = [
        ('nathprojects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to=nathprojects.models.csv_upload_to, verbose_name='CSV файл'),
        ),
        migrations.DeleteModel(
            name='HospitalData',
        ),
    ]