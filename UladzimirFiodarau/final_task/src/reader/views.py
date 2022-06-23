from django.shortcuts import render
from .models import Cache
from .forms import AddUrlForm
from .reader import DjangoRssReader, DjangoRssReaderCached


def home_view(request):
    qs = Cache.objects.all()
    add_form = AddUrlForm()
    return render(request, 'reader/home.html', {'object_list': qs, 'add_form': add_form})


def news_view(request):
    qs = Cache.objects.all()
    cache = {}
    for obj in qs:
        if obj and obj.url and obj.cache:
            cache[obj.url] = obj.cache
    processed_cache = DjangoRssReaderCached.limit_news_dict(cache)
    return render(request, 'reader/news.html', {'news': processed_cache})

