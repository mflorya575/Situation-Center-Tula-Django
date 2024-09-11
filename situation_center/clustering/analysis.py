from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from .models import Document

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import io
import base64
import networkx as nx


def generate_wordcloud(texts):
    text = " ".join(texts)
    wordcloud = WordCloud(stopwords='english', background_color='white').generate(text)

    # Сохраняем облако слов в объекте BytesIO
    buffer = io.BytesIO()
    wordcloud.to_image().save(buffer, format="PNG")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode()
    return img_str


def generate_word_graph(texts):
    text = " ".join(texts)
    words = text.split()
    word_freq = {word: words.count(word) for word in set(words)}

    # Создаем граф
    G = nx.Graph()
    for word, freq in word_freq.items():
        G.add_node(word, size=freq)

    for i, word1 in enumerate(word_freq):
        for word2 in list(word_freq)[i + 1:]:
            G.add_edge(word1, word2)

    # Визуализируем граф
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
    plt.title("Word Relationships")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="PNG")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode()
    return img_str


def cluster_documents(num_clusters=5):
    documents = Document.objects.all()
    texts = [doc.content for doc in documents if doc.content.strip()]

    if not texts:
        return None, "Нет текстов для анализа"

    num_clusters = min(num_clusters, len(texts))

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    model = KMeans(n_clusters=num_clusters, random_state=42)
    model.fit(X)

    clusters = {}
    for doc, label in zip(documents, model.labels_):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(doc)

    # Генерация визуализаций для каждого кластера
    cluster_visualizations = {}
    for cluster_id, cluster_docs in clusters.items():
        texts = [doc.content for doc in cluster_docs if doc.content.strip()]
        wordcloud_img = generate_wordcloud(texts)
        word_graph_img = generate_word_graph(texts)
        cluster_visualizations[cluster_id] = {
            'documents': cluster_docs,
            'wordcloud_img': wordcloud_img,
            'word_graph_img': word_graph_img
        }

    return cluster_visualizations, None
