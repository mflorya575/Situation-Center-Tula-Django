from django.shortcuts import render


def in_development(request):
    context = {
        'title': 'В разработке | СЦ РЭУ филиал им. Г.В. Плеханова',
    }
    return render(request, 'errors/in_development.html', context)


def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request=request, template_name='errors/error404.html', status=404, context={
        'title': '404 Not Found',
    })


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return render(request=request, template_name='errors/error500.html', status=500, context={
        'title': '500 Server Error',
    })


def tr_handler403(request, exception):
    """
    Обработка ошибки 403
    """
    return render(request=request, template_name='errors/error403.html', status=403, context={
        'title': '403 Access is Closed',
    })


def tr_handler400(request, exception):
    """
    Обработка ошибки 400
    """
    return render(request=request, template_name='errors/error400.html', status=400, context={
        'title': '400 Bad Request',
    })


def tr_handler429(request, exception):
    """
    Обработка ошибки 429
    """
    return render(request=request, template_name='errors/error429.html', status=429, context={
        'title': '429 Too Many Requests',
    })


def tr_handler503(request, exception):
    """
    Обработка ошибки 503
    """
    return render(request=request, template_name='errors/error503.html', status=503, context={
        'title': '503 Service Unavailable',
    })
