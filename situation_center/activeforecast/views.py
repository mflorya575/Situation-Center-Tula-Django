from django.shortcuts import render, get_object_or_404
from foresttrees.models import *
from .forms import *
import pandas as pd
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np


def hospital(request):
    # Получаем все объекты Hospital из базы данных
    hospitals = Hospital.objects.all()

    # Передаем данные в контекст
    context = {
        'hospitals': hospitals,
        'title': 'Здравоохранение | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/hospital.html', context)


def hospital_detail(request, slug):
    hospital = get_object_or_404(Hospital, slug=slug)
    csv_file_path = hospital.csv_file.path

    # Загрузка CSV-файла в DataFrame
    df = pd.read_csv(csv_file_path)

    # Проверка на наличие столбца 'region'
    if 'region' not in df.columns:
        raise ValueError("Столбец 'region' не найден в CSV-файле.")

    # Удаление пробелов в столбце 'region'
    df['region'] = df['region'].str.strip()

    # Фильтрация по выбранному региону
    selected_region = request.GET.get('region')
    if selected_region:
        df = df[df['region'] == selected_region]

    # Преобразование DataFrame в длинный формат для удобства обработки
    df_melted = df.melt(id_vars=['region'], var_name='year', value_name='deaths')

    # Преобразование столбцов 'year' и 'deaths' в числовой формат
    df_melted['year'] = pd.to_numeric(df_melted['year'])
    df_melted['deaths'] = pd.to_numeric(df_melted['deaths'])

    # Проверка наличия данных после фильтрации
    if df_melted.empty:
        combined_chart_linear = "Нет данных для отображения."
    else:
        # Подготовка данных для прогнозирования
        X = df_melted['year'].values.reshape(-1, 1)
        y = df_melted['deaths'].values

        # Создание и обучение модели
        model = LinearRegression()
        model.fit(X, y)

        # Прогноз на следующие 8 лет
        future_years = np.arange(df_melted['year'].max() + 1, df_melted['year'].max() + 9).reshape(-1, 1)
        future_predictions = model.predict(future_years)

        # Добавление прогнозных данных в DataFrame
        future_df = pd.DataFrame({
            'region': selected_region,
            'year': future_years.flatten(),
            'deaths': future_predictions
        })

        # Создаем отдельные DataFrame для фактических и прогнозных данных
        df_actual = df_melted[df_melted['year'] <= df_melted['year'].max()]
        df_forecast = future_df

        # Создание комбинированного графика с линейной шкалой
        fig_linear = go.Figure()

        # Линия для фактических данных
        fig_linear.add_trace(
            go.Scatter(x=df_actual['year'], y=df_actual['deaths'], mode='lines+markers', name='Фактические данные', line=dict(color='blue'))
        )
        # Линия для прогнозных данных
        fig_linear.add_trace(
            go.Scatter(x=df_forecast['year'], y=df_forecast['deaths'], mode='lines+markers', name='Прогноз', line=dict(color='red', dash='dash'))
        )
        # Столбчатая диаграмма для всех данных
        fig_linear.add_trace(
            go.Bar(x=df_melted['year'], y=df_melted['deaths'], name='Смерти')
        )

        fig_linear.update_layout(
            title=f'{hospital.title} - Комбинированный график с прогнозом (Линейная шкала)',
            xaxis_title='Годы',
            yaxis_title='Смертей'
        )
        combined_chart_linear = fig_linear.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = RegionForm(request.GET or None, hospital_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'hospital': hospital,
        'region_form': region_form,
        'selected_region': selected_region or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/hospital_detail.html', context)


def study(request):
    # Получаем все объекты Hospital из базы данных
    studies = Study.objects.all()

    # Передаем данные в контекст
    context = {
        'studies': studies,
        'title': 'Образование | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/study.html', context)


def study_detail(request, slug):
    study = get_object_or_404(Study, slug=slug)
    csv_file_path = study.csv_file.path

    # Загрузка CSV-файла в DataFrame
    df = pd.read_csv(csv_file_path)

    # Проверка на наличие столбца 'region'
    if 'region' not in df.columns:
        raise ValueError("Столбец 'region' не найден в CSV-файле.")

    # Удаление пробелов в столбце 'region'
    df['region'] = df['region'].str.strip()

    # Фильтрация по выбранному региону
    selected_region = request.GET.get('region')
    if selected_region:
        df = df[df['region'] == selected_region]

    # Преобразование DataFrame в длинный формат для удобства обработки
    df_melted = df.melt(id_vars=['region'], var_name='year', value_name='data')

    # Преобразование столбцов 'year' и 'deaths' в числовой формат
    df_melted['year'] = pd.to_numeric(df_melted['year'])
    df_melted['data'] = pd.to_numeric(df_melted['data'])

    # Проверка наличия данных после фильтрации
    if df_melted.empty:
        combined_chart_linear = "Нет данных для отображения."
    else:
        # Подготовка данных для прогнозирования
        X = df_melted['year'].values.reshape(-1, 1)
        y = df_melted['data'].values

        # Создание и обучение модели
        model = LinearRegression()
        model.fit(X, y)

        # Прогноз на следующие 8 лет
        future_years = np.arange(df_melted['year'].max() + 1, df_melted['year'].max() + 9).reshape(-1, 1)
        future_predictions = model.predict(future_years)

        # Добавление прогнозных данных в DataFrame
        future_df = pd.DataFrame({
            'region': selected_region,
            'year': future_years.flatten(),
            'data': future_predictions
        })

        # Создаем отдельные DataFrame для фактических и прогнозных данных
        df_actual = df_melted[df_melted['year'] <= df_melted['year'].max()]
        df_forecast = future_df

        # Создание комбинированного графика с линейной шкалой
        fig_linear = go.Figure()

        # Линия для фактических данных
        fig_linear.add_trace(
            go.Scatter(x=df_actual['year'], y=df_actual['data'], mode='lines+markers', name='Фактические данные', line=dict(color='blue'))
        )
        # Линия для прогнозных данных
        fig_linear.add_trace(
            go.Scatter(x=df_forecast['year'], y=df_forecast['data'], mode='lines+markers', name='Прогноз', line=dict(color='red', dash='dash'))
        )
        # Столбчатая диаграмма для всех данных
        fig_linear.add_trace(
            go.Bar(x=df_melted['year'], y=df_melted['data'], name='Количество')
        )

        fig_linear.update_layout(
            title=f'{study.title} - Комбинированный график с прогнозом (Линейная шкала)',
            xaxis_title='Годы',
            yaxis_title='Количество'
        )
        combined_chart_linear = fig_linear.to_html(full_html=False)

    # Создание формы для выбора региона
    region_form = StudyForm(request.GET or None, study_slug=slug)

    context = {
        'combined_chart_linear': combined_chart_linear,
        'study': study,
        'region_form': region_form,
        'selected_region': selected_region or 'Не выбран',
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/study_detail.html', context)


def demographics(request):
    demographicses = Demographics.objects.all()

    # Передаем данные в контекст
    context = {
        'demographicses': demographicses,
        'title': 'Демография | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/demographics.html', context)


def culture(request):
    cultures = Culture.objects.all()

    # Передаем данные в контекст
    context = {
        'cultures': cultures,
        'title': 'Культура | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/culture.html', context)


def road(request):
    roads = Road.objects.all()

    # Передаем данные в контекст
    context = {
        'roads': roads,
        'title': 'Безопасные дороги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/road.html', context)


def science(request):
    sciences = Science.objects.all()

    # Передаем данные в контекст
    context = {
        'sciences': sciences,
        'title': 'Наука | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/science.html', context)


def ecology(request):
    ecologies = Ecology.objects.all()

    # Передаем данные в контекст
    context = {
        'ecologies': ecologies,
        'title': 'Экология | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/ecology.html', context)


def business(request):
    businesses = Business.objects.all()

    # Передаем данные в контекст
    context = {
        'businesses': businesses,
        'title': 'Предпринимательство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/business.html', context)


def turism(request):
    turisms = Turism.objects.all()

    # Передаем данные в контекст
    context = {
        'turisms': turisms,
        'title': 'Туризм | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/turism.html', context)


def house(request):
    houses = House.objects.all()

    # Передаем данные в контекст
    context = {
        'houses': houses,
        'title': 'Жилье | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/house.html', context)


def world(request):
    worlds = World.objects.all()

    # Передаем данные в контекст
    context = {
        'worlds': worlds,
        'title': 'Международная кооперация и экспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/world.html', context)


def labour(request):
    labours = Labour.objects.all()

    # Передаем данные в контекст
    context = {
        'labours': labours,
        'title': 'Труд | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/labour.html', context)


def atom(request):
    atoms = Atom.objects.all()

    # Передаем данные в контекст
    context = {
        'atoms': atoms,
        'title': 'Развитие технологий в области атомной энергии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/atom.html', context)


def econom(request):
    economs = Econom.objects.all()

    # Передаем данные в контекст
    context = {
        'economs': economs,
        'title': 'Цифровая экономика РФ | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/econom.html', context)


def mainline(request):
    mainlines = Mainline.objects.all()

    # Передаем данные в контекст
    context = {
        'mainlines': mainlines,
        'title': 'Расширение магистральной инфраструктуры | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/mainline.html', context)


def industry(request):
    industries = Industry.objects.all()

    # Передаем данные в контекст
    context = {
        'industries': industries,
        'title': 'Промышленность | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/industry.html', context)


def agro(request):
    agros = Agro.objects.all()

    # Передаем данные в контекст
    context = {
        'agros': agros,
        'title': 'Сельское хозяйство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/agro.html', context)


def building(request):
    buildings = Building.objects.all()

    # Передаем данные в контекст
    context = {
        'buildings': buildings,
        'title': 'Строительство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/building.html', context)


def transport(request):
    transports = Transport.objects.all()

    # Передаем данные в контекст
    context = {
        'transports': transports,
        'title': 'Транспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/transport.html', context)


def trading(request):
    tradings = Trading.objects.all()

    # Передаем данные в контекст
    context = {
        'tradings': tradings,
        'title': 'Торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/trading.html', context)


def uslugi(request):
    uslugis = Uslugi.objects.all()

    # Передаем данные в контекст
    context = {
        'uslugis': uslugis,
        'title': 'Услуги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/uslugi.html', context)


def investing(request):
    investings = Investing.objects.all()

    # Передаем данные в контекст
    context = {
        'investings': investings,
        'title': 'Инвестиции | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/investing.html', context)


def finpr(request):
    finprs = FinPr.objects.all()

    # Передаем данные в контекст
    context = {
        'finprs': finprs,
        'title': 'Финансы предприятий | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/finpr.html', context)


def price(request):
    prices = Price.objects.all()

    # Передаем данные в контекст
    context = {
        'prices': prices,
        'title': 'Потребительские цены | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/price.html', context)


def prodprice(request):
    prodprices = ProdPrice.objects.all()

    # Передаем данные в контекст
    context = {
        'prodprices': prodprices,
        'title': 'Цены производителей | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/prodprice.html', context)


def revenue(request):
    revenues = Revenue.objects.all()

    # Передаем данные в контекст
    context = {
        'revenues': revenues,
        'title': 'Доходы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/revenue.html', context)


def salary(request):
    salaries = Salary.objects.all()

    # Передаем данные в контекст
    context = {
        'salaries': salaries,
        'title': 'Зарплата | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/salary.html', context)


def joblessness(request):
    joblessnesses = Joblessness.objects.all()

    # Передаем данные в контекст
    context = {
        'joblessnesses': joblessnesses,
        'title': 'Безработица | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/joblessness.html', context)


def jobmarket(request):
    jobmarkets = JobMarket.objects.all()

    # Передаем данные в контекст
    context = {
        'jobmarkets': jobmarkets,
        'title': 'Рынок труда | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/jobmarket.html', context)


def smcompany(request):
    smcompanies = SmallMediumCompany.objects.all()

    # Передаем данные в контекст
    context = {
        'smcompanies': smcompanies,
        'title': 'Малые и средние предприятия | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/smcompany.html', context)


def population(request):
    populations = Population.objects.all()

    # Передаем данные в контекст
    context = {
        'populations': populations,
        'title': 'Население | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/population.html', context)


def levelhealth(request):
    levelhealths = LevelHealth.objects.all()

    # Передаем данные в контекст
    context = {
        'levelhealths': levelhealths,
        'title': 'Уровень жизни населения | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/levelhealth.html', context)


def securenature(request):
    securenatures = SecureNature.objects.all()

    # Передаем данные в контекст
    context = {
        'securenatures': securenatures,
        'title': 'Охрана природы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/securenature.html', context)


def capitalassets(request):
    capitalassetses = CapitalAssets.objects.all()

    # Передаем данные в контекст
    context = {
        'capitalassetses': capitalassetses,
        'title': 'Основные фонды | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/capitalassets.html', context)


def organization(request):
    organizations = Organization.objects.all()

    # Передаем данные в контекст
    context = {
        'organizations': organizations,
        'title': 'Предприятия и организации | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/organization.html', context)


def shlrr(request):
    shlrrs = SHLRR.objects.all()

    # Передаем данные в контекст
    context = {
        'shlrrs': shlrrs,
        'title': 'С/х, лесное, рыболовство, рыбоводство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/shlrr.html', context)


def infotechnology(request):
    infotechnologies = InfoTechnology.objects.all()

    # Передаем данные в контекст
    context = {
        'infotechnologies': infotechnologies,
        'title': 'Информационные и коммуникационные технологии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/infotechnology.html', context)


def finance(request):
    finances = Finance.objects.all()

    # Передаем данные в контекст
    context = {
        'finances': finances,
        'title': 'Финансы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'activeforecast/finance.html', context)
