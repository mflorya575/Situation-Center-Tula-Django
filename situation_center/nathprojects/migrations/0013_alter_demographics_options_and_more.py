# Generated by Django 4.2.8 on 2024-07-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nathprojects', '0012_demographics_demographicsdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demographics',
            options={'verbose_name': 'Демография', 'verbose_name_plural': 'Демография'},
        ),
        migrations.AlterField(
            model_name='demographicsdata',
            name='index',
            field=models.FloatField(),
        ),
    ]
