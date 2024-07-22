from django.shortcuts import render


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
