from django.shortcuts import render
from .analysis import cluster_documents


def clustering_view(request):
    num_clusters = int(request.GET.get('num_clusters', 5))
    clusters, error = cluster_documents(num_clusters)

    if error:
        return render(request, 'clustering/error.html', {'error': error})

    # Передаем данные в шаблон
    return render(request, 'clustering/results.html', {'clusters': clusters})
