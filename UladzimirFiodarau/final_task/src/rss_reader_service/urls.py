"""rss_reader_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reader.views import cached_news_view, read_news_view, fresh_news_view, read_fresh_news_view, news_pdf, news_html, news_pdf2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cached_news/', cached_news_view, name='cached_news'),
    path('read_news/', read_news_view, name='read_news'),
    path('fresh_news/', fresh_news_view, name='fresh_news'),
    path('read_fresh_news/', read_fresh_news_view, name='read_fresh_news'),
    path('news_pdf/', news_pdf, name='news_pdf'),
    path('news_html/', news_html, name='news_html'),
]
