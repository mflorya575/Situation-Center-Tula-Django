# Generated by Django 4.2.8 on 2024-07-23 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nathprojects', '0017_ecology_ecologydata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Предпринимательство',
                'verbose_name_plural': 'Предпринимательство',
            },
        ),
        migrations.CreateModel(
            name='BusinessData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('data', models.FloatField()),
                ('region', models.CharField(blank=True, choices=[('tula', 'Тульская область'), ('moscow', 'Московская область'), ('spb', 'Санкт-Петербург'), ('saratov', 'Саратовская область'), ('novosibirsk', 'Новосибирская область'), ('yekaterinburg', 'Свердловская область'), ('krasnodar', 'Краснодарский край'), ('kazan', 'Республика Татарстан'), ('vladivostok', 'Приморский край'), ('krasnodar', 'Краснодарский край'), ('nizhny_novgorod', 'Нижегородская область'), ('rostov', 'Ростовская область')], max_length=50, verbose_name='Регион')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='nathprojects.business')),
            ],
            options={
                'verbose_name': 'Данные по предпринимательству',
                'verbose_name_plural': 'Данные по предпринимательству',
                'ordering': ['name'],
            },
        ),
    ]