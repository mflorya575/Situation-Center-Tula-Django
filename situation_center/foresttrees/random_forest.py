import csv
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import export_text


def process_csv_data(csv_file_path):
    data = pd.read_csv(csv_file_path)
    return data


def calculate_random_forest(data, target_column, feature_columns):
    X = data[feature_columns]
    y = data[target_column]

    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Обучение модели случайного леса
    model = RandomForestRegressor(n_estimators=89, random_state=42)
    model.fit(X_train, y_train)

    # Коэффициент детерминации
    r2_score = model.score(X_test, y_test)

    # Значимость факторных переменных
    feature_importances = model.feature_importances_

    # Список деревьев
    trees = []
    for tree in model.estimators_:
        tree_rules = export_text(tree, feature_names=feature_columns)
        trees.append(tree_rules)

    return {
        "r2_score": r2_score,
        "feature_importances": feature_importances,
        "trees": trees
    }
