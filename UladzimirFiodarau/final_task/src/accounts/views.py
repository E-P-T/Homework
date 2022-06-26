from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserLoginForm

__all__ = ['login_view',
           'logout_view',
           ]


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('start')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
