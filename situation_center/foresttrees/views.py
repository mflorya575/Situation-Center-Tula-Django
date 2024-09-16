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
