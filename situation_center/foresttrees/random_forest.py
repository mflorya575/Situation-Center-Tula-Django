import csv
import plotly.express as px
import plotly.io as pio
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import export_text


def process_csv_data(csv_file_path):
    # Чтение данных из CSV
    data = pd.read_csv(csv_file_path)

    # Удаление строк с пропусками (NaN)
    data = data.dropna()
    return data


def calculate_random_forest(data, target_column, feature_columns):
    X = data[feature_columns]
    y = data[target_column]

    # Проверка количества данных
    if len(X) < 2:
        raise ValueError("Недостаточно данных для разделения на обучающую и тестовую выборки.")

    # Разделение данных на обучающую и тестовую выборки
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    except ValueError as e:
        # Вывод сообщения о проблеме
        raise ValueError(f"Ошибка при разделении данных: {e}")

    # Обучение модели случайного леса
    model = RandomForestRegressor(n_estimators=89, random_state=42)
    model.fit(X_train, y_train)

    # Предсказания
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Коэффициент детерминации и метрики ошибки
    train_r2_score = r2_score(y_train, y_pred_train)
    test_r2_score = r2_score(y_test, y_pred_test)
    train_mse = mean_squared_error(y_train, y_pred_train)
    test_mse = mean_squared_error(y_test, y_pred_test)

    # Значимость факторных переменных
    feature_importances = model.feature_importances_

    # Визуализация важности признаков
    feature_importances_df = pd.DataFrame({
        'Feature': feature_columns,
        'Importance': feature_importances
    })
    fig = px.bar(feature_importances_df, x='Feature', y='Importance', title='Feature Importance in Random Forest Model')
    fig_html = pio.to_html(fig, full_html=False)

    # Список деревьев
    trees = []
    for tree in model.estimators_:
        tree_rules = export_text(tree, feature_names=feature_columns)
        trees.append(tree_rules)

    return {
        "train_r2_score": train_r2_score,
        "test_r2_score": test_r2_score,
        "train_mse": train_mse,
        "test_mse": test_mse,
        "feature_importances": feature_importances,
        "trees": trees,
        "feature_importances_plot": fig_html
    }
