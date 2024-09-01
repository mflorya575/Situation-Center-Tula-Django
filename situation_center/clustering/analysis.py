from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from .models import Document


def cluster_documents(num_clusters=5):
    documents = Document.objects.all()
    texts = [doc.content for doc in documents if doc.content.strip()]

    if not texts:
        return None, "Нет текстов для анализа"

    # Ограничиваем количество кластеров количеством доступных текстов
    num_clusters = min(num_clusters, len(texts))

    # Преобразуем тексты в матрицу TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    # Применяем KMeans
    model = KMeans(n_clusters=num_clusters, random_state=42)
    model.fit(X)

    return list(zip(documents, model.labels_)), None