# Generated by Django 4.2.8 on 2024-08-20 16:41

from django.db import migrations, models
import nathprojects.models


class Migration(migrations.Migration):

    dependencies = [
        ('nathprojects', '0004_alter_demographics_options_demographics_csv_file_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demographics',
            options={'verbose_name': 'Демография', 'verbose_name_plural': 'Демография'},
        ),
        migrations.AddField(
            model_name='culture',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to=nathprojects.models.csv_upload_to, verbose_name='CSV файл'),
        ),
        migrations.DeleteModel(
            name='CultureData',
        ),
    ]