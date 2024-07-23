from django.shortcuts import render


def strategy1(request):
    context = {
        'title': 'Внешнеэкономические связи | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'strategy/strategy1.html', context)


def strategy2(request):
    context = {
        'title': 'Развитие инфраструктуры | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'strategy/strategy2.html', context)
