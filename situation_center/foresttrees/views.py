from django.shortcuts import render
from .models import Hospital
from .random_forest import process_csv_data, calculate_random_forest


def regression_view(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)

    if request.method == "POST":
        target_column = request.POST.get("target_column")
        feature_columns = request.POST.getlist("feature_columns")

        data = process_csv_data(hospital.csv_file.path)

        result = calculate_random_forest(data, target_column, feature_columns)

        context = {
            "hospital": hospital,
            "r2_score": result["r2_score"],
            "feature_importances": zip(feature_columns, result["feature_importances"]),
            "trees": result["trees"]
        }
        return render(request, "foresttrees/hospital_result.html", context)

    # Предполагаем, что названия колонок совпадают с именами в файле CSV
    data = process_csv_data(hospital.csv_file.path)
    columns = data.columns

    return render(request, "foresttrees/hospital.html", {
        "hospital": hospital,
        "columns": columns
    })
