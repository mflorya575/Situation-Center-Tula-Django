from django.shortcuts import render


def index(request):
    context = {
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
