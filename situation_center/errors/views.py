from django.shortcuts import render


def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request=request, template_name='errors/error404.html', status=404, context={
        'title': '404 Not Found',
    })
