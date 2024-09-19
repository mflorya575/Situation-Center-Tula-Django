from django.shortcuts import render, get_object_or_404
from .models import *
from .random_forest import process_csv_data, calculate_random_forest


def hospital(request):
    hospitals = Hospital.objects.all()

    # Передаем данные в контекст
    context = {
        'hospitals': hospitals,
        'title': 'Здравоохранение | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/hospital.html', context)


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
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/hospital_result.html", context)

    data = process_csv_data(hospital.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/hospital_detail.html", {
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
    return render(request, 'foresttrees/study.html', context)


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
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/study_result.html", context)

    data = process_csv_data(study.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/study_detail.html", {
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
    return render(request, 'foresttrees/demographics.html', context)


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
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/demographics_result.html", context)

    data = process_csv_data(demographics.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/demographics_detail.html", {
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
    return render(request, 'foresttrees/culture.html', context)


def culture_view(request, slug):
    culture = get_object_or_404(Culture, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(culture.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "culture": culture,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/culture_result.html", context)

    data = process_csv_data(culture.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/culture_detail.html", {
        "culture": culture,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def road(request):
    roads = Road.objects.all()

    # Передаем данные в контекст
    context = {
        'roads': roads,
        'title': 'Безопасные дороги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/road.html', context)


def road_view(request, slug):
    road = get_object_or_404(Road, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(road.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "road": road,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/road_result.html", context)

    data = process_csv_data(road.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/road_detail.html", {
        "road": road,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def science(request):
    sciences = Science.objects.all()

    # Передаем данные в контекст
    context = {
        'sciences': sciences,
        'title': 'Наука | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/science.html', context)


def science_view(request, slug):
    science = get_object_or_404(Science, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(science.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "science": science,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/science_result.html", context)

    data = process_csv_data(science.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/science_detail.html", {
        "science": science,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def ecology(request):
    ecologies = Ecology.objects.all()

    # Передаем данные в контекст
    context = {
        'ecologies': ecologies,
        'title': 'Экология | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/ecology.html', context)


def ecology_view(request, slug):
    ecology = get_object_or_404(Ecology, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(ecology.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "ecology": ecology,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/ecology_result.html", context)

    data = process_csv_data(ecology.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/ecology_detail.html", {
        "ecology": ecology,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def business(request):
    businesses = Business.objects.all()

    # Передаем данные в контекст
    context = {
        'businesses': businesses,
        'title': 'Предпринимательство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/business.html', context)


def business_view(request, slug):
    business = get_object_or_404(Business, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(business.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "business": business,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/business_result.html", context)

    data = process_csv_data(business.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/business_detail.html", {
        "business": business,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def turism(request):
    turisms = Turism.objects.all()

    # Передаем данные в контекст
    context = {
        'turisms': turisms,
        'title': 'Туризм | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/turism.html', context)


def turism_view(request, slug):
    turism = get_object_or_404(Turism, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(turism.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "turism": turism,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/turism_result.html", context)

    data = process_csv_data(turism.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/turism_detail.html", {
        "turism": turism,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def house(request):
    houses = House.objects.all()

    # Передаем данные в контекст
    context = {
        'houses': houses,
        'title': 'Жилье | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/house.html', context)


def house_view(request, slug):
    house = get_object_or_404(House, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(house.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "house": house,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/house_result.html", context)

    data = process_csv_data(house.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/house_detail.html", {
        "house": house,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def world(request):
    worlds = World.objects.all()

    # Передаем данные в контекст
    context = {
        'worlds': worlds,
        'title': 'Международная кооперация и экспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/world.html', context)


def world_view(request, slug):
    world = get_object_or_404(World, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(world.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "world": world,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/world_result.html", context)

    data = process_csv_data(world.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/world_detail.html", {
        "world": world,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def labour(request):
    labours = Labour.objects.all()

    # Передаем данные в контекст
    context = {
        'labours': labours,
        'title': 'Труд | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/labour.html', context)


def labour_view(request, slug):
    labour = get_object_or_404(Labour, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(labour.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "labour": labour,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/labour_result.html", context)

    data = process_csv_data(labour.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/labour_detail.html", {
        "labour": labour,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def atom(request):
    atoms = Atom.objects.all()

    # Передаем данные в контекст
    context = {
        'atoms': atoms,
        'title': 'Развитие технологий в области атомной энергии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/atom.html', context)


def atom_view(request, slug):
    atom = get_object_or_404(Atom, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(atom.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "atom": atom,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/atom_result.html", context)

    data = process_csv_data(atom.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/atom_detail.html", {
        "atom": atom,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def econom(request):
    economs = Econom.objects.all()

    # Передаем данные в контекст
    context = {
        'economs': economs,
        'title': 'Экономика | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/econom.html', context)


def econom_view(request, slug):
    econom = get_object_or_404(Econom, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(econom.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "econom": econom,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/econom_result.html", context)

    data = process_csv_data(econom.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/econom_detail.html", {
        "econom": econom,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def mainline(request):
    mainlines = Mainline.objects.all()

    # Передаем данные в контекст
    context = {
        'mainlines': mainlines,
        'title': 'Расширение магистральной инфраструктуры | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/mainline.html', context)


def mainline_view(request, slug):
    mainline = get_object_or_404(Mainline, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(mainline.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "mainline": mainline,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/mainline_result.html", context)

    data = process_csv_data(mainline.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/mainline_detail.html", {
        "mainline": mainline,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def industry(request):
    industries = Industry.objects.all()

    # Передаем данные в контекст
    context = {
        'industries': industries,
        'title': 'Промышленность | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/industry.html', context)


def industry_view(request, slug):
    industry = get_object_or_404(Industry, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(industry.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "industry": industry,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/industry_result.html", context)

    data = process_csv_data(industry.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/industry_detail.html", {
        "industry": industry,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def agro(request):
    agros = Agro.objects.all()

    # Передаем данные в контекст
    context = {
        'agros': agros,
        'title': 'Сельское хозяйство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/agro.html', context)


def agro_view(request, slug):
    agro = get_object_or_404(Agro, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(agro.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "agro": agro,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/agro_result.html", context)

    data = process_csv_data(agro.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/agro_detail.html", {
        "agro": agro,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def building(request):
    buildings = Building.objects.all()

    # Передаем данные в контекст
    context = {
        'buildings': buildings,
        'title': 'Строительство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/building.html', context)


def building_view(request, slug):
    building = get_object_or_404(Building, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(building.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "building": building,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/building_result.html", context)

    data = process_csv_data(building.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/building_detail.html", {
        "building": building,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def transport(request):
    transports = Transport.objects.all()

    # Передаем данные в контекст
    context = {
        'transports': transports,
        'title': 'Транспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/transport.html', context)


def transport_view(request, slug):
    transport = get_object_or_404(Transport, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(transport.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "transport": transport,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/transport_result.html", context)

    data = process_csv_data(transport.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/transport_detail.html", {
        "transport": transport,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def trading(request):
    tradings = Trading.objects.all()

    # Передаем данные в контекст
    context = {
        'tradings': tradings,
        'title': 'Торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/trading.html', context)


def trading_view(request, slug):
    trading = get_object_or_404(Trading, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(trading.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "trading": trading,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/trading_result.html", context)

    data = process_csv_data(trading.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/trading_detail.html", {
        "trading": trading,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def uslugi(request):
    uslugis = Uslugi.objects.all()

    # Передаем данные в контекст
    context = {
        'uslugis': uslugis,
        'title': 'Услуги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/uslugi.html', context)


def uslugi_view(request, slug):
    uslugi = get_object_or_404(Uslugi, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(uslugi.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "uslugi": uslugi,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/uslugi_result.html", context)

    data = process_csv_data(uslugi.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/uslugi_detail.html", {
        "uslugi": uslugi,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def investing(request):
    investings = Investing.objects.all()

    # Передаем данные в контекст
    context = {
        'investings': investings,
        'title': 'Инвестиции | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/investing.html', context)


def investing_view(request, slug):
    investing = get_object_or_404(Investing, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(investing.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "investing": investing,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/investing_result.html", context)

    data = process_csv_data(investing.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/investing_detail.html", {
        "investing": investing,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def finpr(request):
    finprs = FinPr.objects.all()

    # Передаем данные в контекст
    context = {
        'finprs': finprs,
        'title': 'Финансы предприятий | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/finpr.html', context)


def finpr_view(request, slug):
    finpr = get_object_or_404(FinPr, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(finpr.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "finpr": finpr,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/finpr_result.html", context)

    data = process_csv_data(finpr.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/finpr_detail.html", {
        "finpr": finpr,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def price(request):
    prices = Price.objects.all()

    # Передаем данные в контекст
    context = {
        'prices': prices,
        'title': 'Потребительские цены | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/price.html', context)


def price_view(request, slug):
    price = get_object_or_404(Price, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(price.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "price": price,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/price_result.html", context)

    data = process_csv_data(price.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/price_detail.html", {
        "price": price,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def prodprice(request):
    prodprices = ProdPrice.objects.all()

    # Передаем данные в контекст
    context = {
        'prodprices': prodprices,
        'title': 'Цены производителей | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/prodprice.html', context)


def prodprice_view(request, slug):
    prodprice = get_object_or_404(ProdPrice, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(prodprice.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "prodprice": prodprice,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/prodprice_result.html", context)

    data = process_csv_data(prodprice.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/prodprice_detail.html", {
        "prodprice": prodprice,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def revenue(request):
    revenues = Revenue.objects.all()

    # Передаем данные в контекст
    context = {
        'revenues': revenues,
        'title': 'Доходы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/revenue.html', context)


def revenue_view(request, slug):
    revenue = get_object_or_404(Revenue, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(revenue.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "revenue": revenue,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/revenue_result.html", context)

    data = process_csv_data(revenue.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/revenue_detail.html", {
        "revenue": revenue,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def salary(request):
    salaries = Salary.objects.all()

    # Передаем данные в контекст
    context = {
        'salaries': salaries,
        'title': 'Зарплата | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/salary.html', context)


def salary_view(request, slug):
    salary = get_object_or_404(Salary, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(salary.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "salary": salary,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/salary_result.html", context)

    data = process_csv_data(salary.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/salary_detail.html", {
        "salary": salary,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def joblessness(request):
    joblessnesses = Joblessness.objects.all()

    # Передаем данные в контекст
    context = {
        'joblessnesses': joblessnesses,
        'title': 'Безработица | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/joblessness.html', context)


def joblessness_view(request, slug):
    joblessness = get_object_or_404(Joblessness, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(joblessness.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "joblessness": joblessness,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/joblessness_result.html", context)

    data = process_csv_data(joblessness.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/joblessness_detail.html", {
        "joblessness": joblessness,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def jobmarket(request):
    jobmarkets = JobMarket.objects.all()

    # Передаем данные в контекст
    context = {
        'jobmarkets': jobmarkets,
        'title': 'Рынок труда | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/jobmarket.html', context)


def jobmarket_view(request, slug):
    jobmarket = get_object_or_404(JobMarket, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(jobmarket.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "jobmarket": jobmarket,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/jobmarket_result.html", context)

    data = process_csv_data(jobmarket.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/jobmarket_detail.html", {
        "jobmarket": jobmarket,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def smcompany(request):
    smcompanies = SmallMediumCompany.objects.all()

    # Передаем данные в контекст
    context = {
        'smcompanies': smcompanies,
        'title': 'Малые и средние предприятия | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/smcompany.html', context)


def smcompany_view(request, slug):
    smcompany = get_object_or_404(SmallMediumCompany, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(smcompany.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "smcompany": smcompany,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/smcompany_result.html", context)

    data = process_csv_data(smcompany.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/smcompany_detail.html", {
        "smcompany": smcompany,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def population(request):
    populations = Population.objects.all()

    # Передаем данные в контекст
    context = {
        'populations': populations,
        'title': 'Население | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/population.html', context)


def population_view(request, slug):
    population = get_object_or_404(Population, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(population.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "population": population,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/population_result.html", context)

    data = process_csv_data(population.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/population_detail.html", {
        "population": population,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def levelhealth(request):
    levelhealths = LevelHealth.objects.all()

    # Передаем данные в контекст
    context = {
        'levelhealths': levelhealths,
        'title': 'Уровень жизни населения | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/levelhealth.html', context)


def levelhealth_view(request, slug):
    levelhealth = get_object_or_404(LevelHealth, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(levelhealth.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "levelhealth": levelhealth,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/levelhealth_result.html", context)

    data = process_csv_data(levelhealth.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/levelhealth_detail.html", {
        "levelhealth": levelhealth,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def securenature(request):
    securenatures = SecureNature.objects.all()

    # Передаем данные в контекст
    context = {
        'securenatures': securenatures,
        'title': 'Охрана природы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/securenature.html', context)


def securenature_view(request, slug):
    securenature = get_object_or_404(SecureNature, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(securenature.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "securenature": securenature,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/securenature_result.html", context)

    data = process_csv_data(securenature.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/securenature_detail.html", {
        "securenature": securenature,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def capitalassets(request):
    capitalassetses = CapitalAssets.objects.all()

    # Передаем данные в контекст
    context = {
        'capitalassetses': capitalassetses,
        'title': 'Основные фонды | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/capitalassets.html', context)


def capitalassets_view(request, slug):
    capitalassets = get_object_or_404(CapitalAssets, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(capitalassets.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "capitalassets": capitalassets,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/capitalassets_result.html", context)

    data = process_csv_data(capitalassets.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/capitalassets_detail.html", {
        "capitalassets": capitalassets,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def organization(request):
    organizations = Organization.objects.all()

    # Передаем данные в контекст
    context = {
        'organizations': organizations,
        'title': 'Предприятия и организации | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/organization.html', context)


def organization_view(request, slug):
    organization = get_object_or_404(Organization, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(organization.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "organization": organization,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/organization_result.html", context)

    data = process_csv_data(organization.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/organization_detail.html", {
        "organization": organization,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def shlrr(request):
    shlrrs = SHLRR.objects.all()

    # Передаем данные в контекст
    context = {
        'shlrrs': shlrrs,
        'title': 'С/х, лесное, рыболовство, рыбоводство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/shlrr.html', context)


def shlrr_view(request, slug):
    shlrr = get_object_or_404(SHLRR, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(shlrr.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "shlrr": shlrr,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/shlrr_result.html", context)

    data = process_csv_data(shlrr.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/shlrr_detail.html", {
        "shlrr": shlrr,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def infotechnology(request):
    infotechnologies = InfoTechnology.objects.all()

    # Передаем данные в контекст
    context = {
        'infotechnologies': infotechnologies,
        'title': 'Информационные и коммуникационные технологии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/infotechnology.html', context)


def infotechnology_view(request, slug):
    infotechnology = get_object_or_404(InfoTechnology, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(infotechnology.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "infotechnology": infotechnology,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/infotechnology_result.html", context)

    data = process_csv_data(infotechnology.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/infotechnology_detail.html", {
        "infotechnology": infotechnology,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def finance(request):
    finances = Finance.objects.all()

    # Передаем данные в контекст
    context = {
        'finances': finances,
        'title': 'Финансы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/finance.html', context)


def finance_view(request, slug):
    finance = get_object_or_404(Finance, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(finance.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "finance": finance,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/finance_result.html", context)

    data = process_csv_data(finance.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/finance_detail.html", {
        "finance": finance,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def foreigntrading(request):
    foreigntradings = ForeignTrading.objects.all()

    # Передаем данные в контекст
    context = {
        'foreigntradings': foreigntradings,
        'title': 'Внешняя торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/foreigntrading.html', context)


def foreigntrading_view(request, slug):
    foreigntrading = get_object_or_404(ForeignTrading, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(foreigntrading.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "foreigntrading": foreigntrading,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/foreigntrading_result.html", context)

    data = process_csv_data(foreigntrading.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/foreigntrading_detail.html", {
        "foreigntrading": foreigntrading,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def vrp(request):
    vrps = VRP.objects.all()

    # Передаем данные в контекст
    context = {
        'vrps': vrps,
        'title': 'Валовой региональный продукт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/vrp.html', context)


def vrp_view(request, slug):
    vrp = get_object_or_404(VRP, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(vrp.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "vrp": vrp,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/vrp_result.html", context)

    data = process_csv_data(vrp.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/vrp_detail.html", {
        "vrp": vrp,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })


def industrialprod(request):
    industrialprods = IndustrialProd.objects.all()

    # Передаем данные в контекст
    context = {
        'industrialprods': industrialprods,
        'title': 'Промышленное производство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/industrialprod.html', context)


def industrialprod_view(request, slug):
    industrialprod = get_object_or_404(IndustrialProd, slug=slug)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(industrialprod.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "industrialprod": industrialprod,
            "train_r2_score": result["train_r2_score"],
            "test_r2_score": result["test_r2_score"],
            "train_mse": result["train_mse"],
            "test_mse": result["test_mse"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"],
            "feature_importances_plot": result["feature_importances_plot"],
            'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
        }
        return render(request, "foresttrees/industrialprod_result.html", context)

    data = process_csv_data(industrialprod.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/industrialprod_detail.html", {
        "industrialprod": industrialprod,
        "columns": columns,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    })
