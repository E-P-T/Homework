from django.urls import path

from .views import *

urlpatterns = [
    path('cached_news/', cached_news_view, name='cached_news'),
    path('add_news/', add_news, name='add_news'),
    path('read_news/', read_news_view, name='read_news'),
    path('fresh_news/', fresh_news_view, name='fresh_news'),
    path('read_fresh_news/', read_fresh_news_view, name='read_fresh_news'),
    path('news_pdf/', news_pdf, name='news_pdf'),
    path('news_html/', news_html, name='news_html'),
    path('start/', start_page_view, name='start'),
]
