from django.shortcuts import render

from news.models import News


def index(request):
    news = News.objects.all()[:3]

    context = {
        'news': news,
        'title': 'СЦ РЭУ филиал им. Г.В. Плеханова',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'main/about.html', context)


def contact(request):
    context = {
        'title': 'Контакты | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'main/contact.html', context)


def policy_privacy(request):
    context = {
        'title': 'Политика конфиденциальности | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'main/policy_privacy.html', context)
