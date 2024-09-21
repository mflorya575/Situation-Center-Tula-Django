from django.shortcuts import render, get_object_or_404
from foresttrees.models import *
from .ai import process_csv_data, calculate_random_forest
from django.http import FileResponse, Http404
import os


def download_model(request, filename):
    file_path = os.path.join('models', filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
    else:
        raise Http404("File does not exist")


def hospital(request):
    hospitals = Hospital.objects.all()

    # Передаем данные в контекст
    context = {
        'hospitals': hospitals,
        'title': 'Здравоохранение | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/hospital.html', context)


def hospital_view(request, slug):
    hospital = get_object_or_404(Hospital, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(hospital.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "hospital": hospital,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            "model_filename": result["model_filename"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "ai/hospital_result.html", context)

    data = process_csv_data(hospital.csv_file.path)
    columns = data.columns

    return render(request, "ai/hospital_detail.html", {
        "hospital": hospital,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def study(request):
    studies = Study.objects.all()

    # Передаем данные в контекст
    context = {
        'studies': studies,
        'title': 'Образование | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/study.html', context)


def study_view(request, slug):
    study = get_object_or_404(Study, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(study.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "study": study,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            "model_filename": result["model_filename"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "ai/study_result.html", context)

    data = process_csv_data(study.csv_file.path)
    columns = data.columns

    return render(request, "ai/study_detail.html", {
        "study": study,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def demographics(request):
    demographicses = Demographics.objects.all()

    # Передаем данные в контекст
    context = {
        'demographicses': demographicses,
        'title': 'Демография | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/demographics.html', context)


def demographics_view(request, slug):
    demographics = get_object_or_404(Demographics, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(demographics.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "demographics": demographics,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            "model_filename": result["model_filename"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "ai/demographics_result.html", context)

    data = process_csv_data(demographics.csv_file.path)
    columns = data.columns

    return render(request, "ai/demographics_detail.html", {
        "demographics": demographics,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def culture(request):
    cultures = Culture.objects.all()

    # Передаем данные в контекст
    context = {
        'cultures': cultures,
        'title': 'Культура | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/culture.html', context)


def road(request):
    roads = Road.objects.all()

    # Передаем данные в контекст
    context = {
        'roads': roads,
        'title': 'Безопасные дороги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/road.html', context)


def science(request):
    sciences = Science.objects.all()

    # Передаем данные в контекст
    context = {
        'sciences': sciences,
        'title': 'Наука | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/science.html', context)


def ecology(request):
    ecologies = Ecology.objects.all()

    # Передаем данные в контекст
    context = {
        'ecologies': ecologies,
        'title': 'Экология | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/ecology.html', context)


def business(request):
    businesses = Business.objects.all()

    # Передаем данные в контекст
    context = {
        'businesses': businesses,
        'title': 'Предпринимательство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/business.html', context)


def turism(request):
    turisms = Turism.objects.all()

    # Передаем данные в контекст
    context = {
        'turisms': turisms,
        'title': 'Туризм | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/turism.html', context)


def house(request):
    houses = House.objects.all()

    # Передаем данные в контекст
    context = {
        'houses': houses,
        'title': 'Жилье | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/house.html', context)


def world(request):
    worlds = World.objects.all()

    # Передаем данные в контекст
    context = {
        'worlds': worlds,
        'title': 'Международная кооперация и экспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/world.html', context)


def labour(request):
    labours = Labour.objects.all()

    # Передаем данные в контекст
    context = {
        'labours': labours,
        'title': 'Труд | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/labour.html', context)


def atom(request):
    atoms = Atom.objects.all()

    # Передаем данные в контекст
    context = {
        'atoms': atoms,
        'title': 'Развитие технологий в области атомной энергии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/atom.html', context)


def econom(request):
    economs = Econom.objects.all()

    # Передаем данные в контекст
    context = {
        'economs': economs,
        'title': 'Экономика | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/econom.html', context)


def mainline(request):
    mainlines = Mainline.objects.all()

    # Передаем данные в контекст
    context = {
        'mainlines': mainlines,
        'title': 'Расширение магистральной инфраструктуры | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/mainline.html', context)


def industry(request):
    industries = Industry.objects.all()

    # Передаем данные в контекст
    context = {
        'industries': industries,
        'title': 'Промышленность | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/industry.html', context)


def agro(request):
    agros = Agro.objects.all()

    # Передаем данные в контекст
    context = {
        'agros': agros,
        'title': 'Сельское хозяйство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/agro.html', context)


def building(request):
    buildings = Building.objects.all()

    # Передаем данные в контекст
    context = {
        'buildings': buildings,
        'title': 'Строительство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/building.html', context)


def transport(request):
    transports = Transport.objects.all()

    # Передаем данные в контекст
    context = {
        'transports': transports,
        'title': 'Транспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/transport.html', context)


def trading(request):
    tradings = Trading.objects.all()

    # Передаем данные в контекст
    context = {
        'tradings': tradings,
        'title': 'Торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/trading.html', context)


def uslugi(request):
    uslugis = Uslugi.objects.all()

    # Передаем данные в контекст
    context = {
        'uslugis': uslugis,
        'title': 'Услуги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/uslugi.html', context)


def investing(request):
    investings = Investing.objects.all()

    # Передаем данные в контекст
    context = {
        'investings': investings,
        'title': 'Инвестиции | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/investing.html', context)


def finpr(request):
    finprs = FinPr.objects.all()

    # Передаем данные в контекст
    context = {
        'finprs': finprs,
        'title': 'Финансы предприятий | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/finpr.html', context)


def price(request):
    prices = Price.objects.all()

    # Передаем данные в контекст
    context = {
        'prices': prices,
        'title': 'Потребительские цены | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/price.html', context)


def prodprice(request):
    prodprices = ProdPrice.objects.all()

    # Передаем данные в контекст
    context = {
        'prodprices': prodprices,
        'title': 'Цены производителей | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/prodprice.html', context)


def revenue(request):
    revenues = Revenue.objects.all()

    # Передаем данные в контекст
    context = {
        'revenues': revenues,
        'title': 'Доходы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/revenue.html', context)


def salary(request):
    salaries = Salary.objects.all()

    # Передаем данные в контекст
    context = {
        'salaries': salaries,
        'title': 'Зарплата | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/salary.html', context)


def joblessness(request):
    joblessnesses = Joblessness.objects.all()

    # Передаем данные в контекст
    context = {
        'joblessnesses': joblessnesses,
        'title': 'Безработица | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/joblessness.html', context)


def jobmarket(request):
    jobmarkets = JobMarket.objects.all()

    # Передаем данные в контекст
    context = {
        'jobmarkets': jobmarkets,
        'title': 'Рынок труда | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/jobmarket.html', context)


def smcompany(request):
    smcompanies = SmallMediumCompany.objects.all()

    # Передаем данные в контекст
    context = {
        'smcompanies': smcompanies,
        'title': 'Малые и средние предприятия | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/smcompany.html', context)


def population(request):
    populations = Population.objects.all()

    # Передаем данные в контекст
    context = {
        'populations': populations,
        'title': 'Население | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/population.html', context)


def levelhealth(request):
    levelhealths = LevelHealth.objects.all()

    # Передаем данные в контекст
    context = {
        'levelhealths': levelhealths,
        'title': 'Уровень жизни населения | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/levelhealth.html', context)


def securenature(request):
    securenatures = SecureNature.objects.all()

    # Передаем данные в контекст
    context = {
        'securenatures': securenatures,
        'title': 'Охрана природы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/securenature.html', context)


def capitalassets(request):
    capitalassetses = CapitalAssets.objects.all()

    # Передаем данные в контекст
    context = {
        'capitalassetses': capitalassetses,
        'title': 'Основные фонды | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/capitalassets.html', context)


def organization(request):
    organizations = Organization.objects.all()

    # Передаем данные в контекст
    context = {
        'organizations': organizations,
        'title': 'Предприятия и организации | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/organization.html', context)


def shlrr(request):
    shlrrs = SHLRR.objects.all()

    # Передаем данные в контекст
    context = {
        'shlrrs': shlrrs,
        'title': 'С/х, лесное, рыболовство, рыбоводство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/shlrr.html', context)


def infotechnology(request):
    infotechnologies = InfoTechnology.objects.all()

    # Передаем данные в контекст
    context = {
        'infotechnologies': infotechnologies,
        'title': 'Информационные и коммуникационные технологии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/infotechnology.html', context)


def finance(request):
    finances = Finance.objects.all()

    # Передаем данные в контекст
    context = {
        'finances': finances,
        'title': 'Финансы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/finance.html', context)


def foreigntrading(request):
    foreigntradings = ForeignTrading.objects.all()

    # Передаем данные в контекст
    context = {
        'foreigntradings': foreigntradings,
        'title': 'Внешняя торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/foreigntrading.html', context)


def vrp(request):
    vrps = VRP.objects.all()

    # Передаем данные в контекст
    context = {
        'vrps': vrps,
        'title': 'Валовой региональный продукт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/vrp.html', context)


def industrialprod(request):
    industrialprods = IndustrialProd.objects.all()

    # Передаем данные в контекст
    context = {
        'industrialprods': industrialprods,
        'title': 'Промышленное производство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'ai/industrialprod.html', context)
