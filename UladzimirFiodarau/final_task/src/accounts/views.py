from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm

__all__ = ['login_view',
           'logout_view',
           'register_view',
           'user_settings_view',
           'user_delete_view'
           ]

User = get_user_model()


def login_view(request):
    """view function for rendering Login screen and user authentication"""
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
    """view function for user logout"""
    logout(request)
    return redirect('login')


def register_view(request):
    """view function for rendering Register screen and user registration"""
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        messages.success(request, 'User added to the system')
        return render(request, 'accounts/register_done.html',
                      {'new_user': new_user})
    return render(request, 'accounts/register.html',
                  {'form': form})


def user_settings_view(request):
    """view function for rendering UserSettings screen and working with user settings"""
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.send_email = data['send_email']
                user.save()
                messages.success(request, 'User settings saved')
                return redirect('settings')
        form = UserUpdateForm(initial={'send_email': user.send_email})
        return render(request, 'accounts/user_settings.html', {'form': form})
    else:
        return redirect('login')


def user_delete_view(request):
    """view function for user deletion"""
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            qs = User.objects.get(pk=user.pk)
            qs.delete()
            messages.success(request, 'User deleted')
    return redirect('login')
