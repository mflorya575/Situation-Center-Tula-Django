from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache

from news.models import News


def index(request):
    # Попробуйте получить данные из кэша
    news = cache.get('latest_news')

    if not news:
        # Если данные не найдены в кэше, получите их из базы данных
        news = News.objects.all()[:3]
        # Сохраните данные в кэше на 15 минут
        cache.set('latest_news', news, timeout=60*60)

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
