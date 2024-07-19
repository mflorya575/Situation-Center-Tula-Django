from django.shortcuts import render, get_object_or_404

from .models import News
from taggit.models import Tag


def news(request):
    tag = request.GET.get('tag', None)

    if tag:
        news_all = News.objects.filter(tags__name=tag)
    else:
        news_all = News.objects.all()

    # Получаем все теги, связанные с моделью News
    tags = Tag.objects.all()

    context = {
        'news_all': news_all,
        'tags': tags,
        'title': 'Новости | СЦ РЭУ филиал им. Г.В. Плеханова',
    }

    return render(request, 'news/news.html', context)


def news_detail(request, news_slug):
    news_item = get_object_or_404(News, slug=news_slug)

    # Форматирование даты
    formatted_date = news_item.create.strftime('%d.%m.%Y')

    context = {
        'news_item': news_item,
        'formatted_date': formatted_date,
        'title': f'{news_item.title} | СЦ РЭУ филиал им. Г.В. Плеханова',
    }

    return render(request, 'news/news_detail.html', context)
