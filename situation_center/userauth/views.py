from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm, AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')
    else:
        form = UserCreationForm()
    return render(request, 'userauth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:index')
        else:
            return render(request, 'userauth/login.html', {'form': form, 'error': 'Неправильный Email или пароль'})
    else:
        form = AuthenticationForm()
    return render(request, 'userauth/login.html', {'form': form})
