from django.shortcuts import render


def news(request):

    context = {
        'title': 'Новости | СЦ РЭУ филиал им. Г.В. Плеханова',
    }

    return render(request, 'news/news.html', context)
