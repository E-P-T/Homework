from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Cache
from .forms import AddUrlForm, NewsParametersForm, FreshNewsParametersForm
from .reader import DjangoRssReader, DjangoRssReaderCached


def paginate_news(dictionary: dict, limit: int = 0):
    pass


def cached_news_view(request):
    qs = Cache.objects.all()
    news_choice_form = NewsParametersForm()
    add_form = AddUrlForm()

    return render(request, 'reader/cached_news.html',
                  {'object_list': qs,
                   'add_form': add_form,
                   'choice_form': news_choice_form,
                   })


def read_news_view(request):
    _context = {'url': request.GET['url'], 'limit': request.GET['limit'], 'date': request.GET['date']}

    news_url = request.GET['url'] if request.GET['url'] else ''
    news_limit = int(request.GET['limit']) if request.GET['limit'] and int(request.GET['limit']) > 0 else None
    news_date = request.GET['date'].replace('/', ':')

    qs = Cache.objects.all()
    cache = {}
    for obj in qs:
        if obj and obj.url and obj.cache:
            cache[obj.url] = obj.cache
    processed_cache = DjangoRssReaderCached.limit_news_dict(news_cache=cache, limit=news_limit,
                                                            news_url=news_url, news_date=news_date)

    feed_title = {key: value for key, value in processed_cache.items() if key != 'feed_items'}
    feed_news = [{key: value}for key, value in processed_cache['feed_items'].items()]
    paginator = Paginator(feed_news, 10)  # Show 10  per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    _context['feed_title'] = feed_title
    _context['feed_news'] = feed_news
    _context['page_obj'] = page_obj

    return render(request, 'reader/read_news.html', _context)


def fresh_news_view(request):
    news_choice_form = FreshNewsParametersForm()
    return render(request, 'reader/fresh_news.html',
                  {'choice_form': news_choice_form,
                   })


def read_fresh_news_view(request):
    _context = {'url': request.GET['url'], 'limit': request.GET['limit']}

    news_url = request.GET['url'] if request.GET['url'] else ''
    news_limit = int(request.GET['limit']) if request.GET['limit'] and int(request.GET['limit']) > 0 else None

    news = DjangoRssReader(news_url, news_limit=news_limit)
    news.save_django_reader_cache()
    if 'news_dict' in news.__dict__:
        processed_cache = DjangoRssReader.limit_news_dict(news_cache=news.news_dict, limit=news_limit)
    else:
        raise ValueError('No news found')

    feed_title = {key: value for key, value in processed_cache.items() if key != 'feed_items'}
    feed_news = [{key: value}for key, value in processed_cache['feed_items'].items()]
    paginator = Paginator(feed_news, 10)  # Show 10  per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    _context['feed_title'] = feed_title
    _context['feed_news'] = feed_news
    _context['page_obj'] = page_obj

    return render(request, 'reader/read_news.html', _context)
