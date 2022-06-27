from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('settings/', user_settings_view, name='settings'),
    path('delete/', user_delete_view, name='delete'),
]