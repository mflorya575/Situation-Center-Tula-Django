from django.shortcuts import render, get_object_or_404
from .models import *
from .random_forest import process_csv_data, calculate_random_forest


def hospital(request):
    # Получаем все объекты Hospital из базы данных
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
        # Получаем выбранные пользователем целевую и факторные переменные
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        print("Выбранные факторные переменные:", feature_columns)

        # Обрабатываем CSV файл и выполняем расчет случайного леса
        data = process_csv_data(hospital.csv_file.path)
        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "hospital": hospital,
            "r2_score": result["r2_score"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"]
        }
        return render(request, "foresttrees/hospital_result.html", context)

    # Если это GET-запрос, получаем названия колонок из CSV файла
    data = process_csv_data(hospital.csv_file.path)
    columns = data.columns

    # Передаем данные в контекст для отображения формы выбора переменных
    return render(request, "foresttrees/hospital_detail.html", {
        "hospital": hospital,
        "columns": columns
    })
