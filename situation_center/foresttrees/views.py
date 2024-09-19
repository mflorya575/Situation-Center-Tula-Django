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


def building(request):
    buildings = Building.objects.all()

    # Передаем данные в контекст
    context = {
        'buildings': buildings,
        'title': 'Строительство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/building.html', context)


def transport(request):
    transports = Transport.objects.all()

    # Передаем данные в контекст
    context = {
        'transports': transports,
        'title': 'Транспорт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/transport.html', context)


def trading(request):
    tradings = Trading.objects.all()

    # Передаем данные в контекст
    context = {
        'tradings': tradings,
        'title': 'Торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/trading.html', context)


def uslugi(request):
    uslugis = Uslugi.objects.all()

    # Передаем данные в контекст
    context = {
        'uslugis': uslugis,
        'title': 'Услуги | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/uslugi.html', context)


def investing(request):
    investings = Investing.objects.all()

    # Передаем данные в контекст
    context = {
        'investings': investings,
        'title': 'Инвестиции | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/investing.html', context)


def finpr(request):
    finprs = FinPr.objects.all()

    # Передаем данные в контекст
    context = {
        'finprs': finprs,
        'title': 'Финансы предприятий | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/finpr.html', context)


def price(request):
    prices = Price.objects.all()

    # Передаем данные в контекст
    context = {
        'prices': prices,
        'title': 'Потребительские цены | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/price.html', context)


def prodprice(request):
    prodprices = ProdPrice.objects.all()

    # Передаем данные в контекст
    context = {
        'prodprices': prodprices,
        'title': 'Цены производителей | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/prodprice.html', context)


def revenue(request):
    revenues = Revenue.objects.all()

    # Передаем данные в контекст
    context = {
        'revenues': revenues,
        'title': 'Доходы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/revenue.html', context)


def salary(request):
    salaries = Salary.objects.all()

    # Передаем данные в контекст
    context = {
        'salaries': salaries,
        'title': 'Зарплата | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/salary.html', context)


def joblessness(request):
    joblessnesses = Joblessness.objects.all()

    # Передаем данные в контекст
    context = {
        'joblessnesses': joblessnesses,
        'title': 'Безработица | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/joblessness.html', context)


def jobmarket(request):
    jobmarkets = JobMarket.objects.all()

    # Передаем данные в контекст
    context = {
        'jobmarkets': jobmarkets,
        'title': 'Рынок труда | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/jobmarket.html', context)


def smcompany(request):
    smcompanies = SmallMediumCompany.objects.all()

    # Передаем данные в контекст
    context = {
        'smcompanies': smcompanies,
        'title': 'Малые и средние предприятия | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/smcompany.html', context)


def population(request):
    populations = Population.objects.all()

    # Передаем данные в контекст
    context = {
        'populations': populations,
        'title': 'Население | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/population.html', context)


def levelhealth(request):
    levelhealths = LevelHealth.objects.all()

    # Передаем данные в контекст
    context = {
        'levelhealths': levelhealths,
        'title': 'Уровень жизни населения | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/levelhealth.html', context)


def securenature(request):
    securenatures = SecureNature.objects.all()

    # Передаем данные в контекст
    context = {
        'securenatures': securenatures,
        'title': 'Охрана природы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/securenature.html', context)


def capitalassets(request):
    capitalassetses = CapitalAssets.objects.all()

    # Передаем данные в контекст
    context = {
        'capitalassetses': capitalassetses,
        'title': 'Основные фонды | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/capitalassets.html', context)


def organization(request):
    organizations = Organization.objects.all()

    # Передаем данные в контекст
    context = {
        'organizations': organizations,
        'title': 'Предприятия и организации | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/organization.html', context)


def shlrr(request):
    shlrrs = SHLRR.objects.all()

    # Передаем данные в контекст
    context = {
        'shlrrs': shlrrs,
        'title': 'С/х, лесное, рыболовство, рыбоводство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/shlrr.html', context)


def infotechnology(request):
    infotechnologies = InfoTechnology.objects.all()

    # Передаем данные в контекст
    context = {
        'infotechnologies': infotechnologies,
        'title': 'Информационные и коммуникационные технологии | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/infotechnology.html', context)


def finance(request):
    finances = Finance.objects.all()

    # Передаем данные в контекст
    context = {
        'finances': finances,
        'title': 'Финансы | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/finance.html', context)


def foreigntrading(request):
    foreigntradings = ForeignTrading.objects.all()

    # Передаем данные в контекст
    context = {
        'foreigntradings': foreigntradings,
        'title': 'Внешняя торговля | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/foreigntrading.html', context)


def vrp(request):
    vrps = VRP.objects.all()

    # Передаем данные в контекст
    context = {
        'vrps': vrps,
        'title': 'Валовой региональный продукт | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/vrp.html', context)


def industrialprod(request):
    industrialprods = IndustrialProd.objects.all()

    # Передаем данные в контекст
    context = {
        'industrialprods': industrialprods,
        'title': 'Промышленное производство | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'foresttrees/industrialprod.html', context)
