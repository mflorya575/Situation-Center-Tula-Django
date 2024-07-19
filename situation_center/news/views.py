from django.shortcuts import render, get_object_or_404

from .models import News


def news(request):
    context = {
        'title': 'Новости | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'news/news.html', context)


def news_detail(request, news_slug):
    news_item = get_object_or_404(News, slug=news_slug)

    context = {
        'news_item': news_item,
        'title': news_item.title,
    }

    return render(request, 'news/news_detail.html', context)
