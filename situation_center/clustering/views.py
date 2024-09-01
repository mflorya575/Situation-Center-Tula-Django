from django.shortcuts import render
from .analysis import cluster_documents


def clustering_view(request):
    num_clusters = int(request.GET.get('num_clusters', 5))
    clusters, error = cluster_documents(num_clusters)

    if error:
        return render(request, 'clustering/error.html', {'error': error})

    return render(request, 'clustering/clustering.html', {'clusters': clusters})
