from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import UserCreationForm, CustomAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Получаем кодовое слово из формы
            code_word = request.POST.get('code_word')

            # Проверяем кодовое слово
            if code_word != 'arnbbErTbUla':
                messages.error(request, 'Неверное кодовое слово.')
                return render(request, 'userauth/register.html', {'form': form})

            # Если кодовое слово верное, сохраняем пользователя
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались.')
            return redirect('main:index')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
            return render(request, 'userauth/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'userauth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Вы успешно вошли в систему.')
            return redirect('main:index')
        else:
            messages.error(request, 'Неверный email или пароль')
            return render(request, 'userauth/login.html', {'form': form, 'error': 'Неверный email или пароль'})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'userauth/login.html', {'form': form})
