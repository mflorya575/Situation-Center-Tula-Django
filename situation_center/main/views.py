from django.shortcuts import render


def index(request):

    context = {
        'title': 'Главная - Ситуационный центр',
    }

    return render(request, 'main/index.html', context)


def about(request):

    context = {
        'title': 'О нас - Ситуационный центр',
    }

    return render(request, 'main/about.html', context)
