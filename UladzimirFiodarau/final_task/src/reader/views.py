import ast

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xhtml2pdf.default import DEFAULT_FONT
from xhtml2pdf import pisa

from .models import Cache
from .forms import AddUrlForm, NewsParametersForm, FreshNewsParametersForm
from .reader import DjangoRssReader, DjangoRssReaderCached
from django.views.decorators.cache import cache_page

__all__ = ['add_news',
           'start_page_view',
           'cached_news_view',
           'update_all_cache_view',
           'read_news_view',
           'fresh_news_view',
           'read_fresh_news_view',
           'news_pdf',
           'news_html',
           'page_not_found',
           'page_server_error',
           'page_permission_denied',
           'page_bad_request',
           ]


def add_news(request):
    """ view function for adding new URLs to track list"""
    url = request.POST.get('url')
    try:
        if url:
            cache = DjangoRssReader(url)
            cache.save_django_reader_cache()
            messages.success(request, 'URL successfully added')
        qs = Cache.objects.all()
        news_choice_form = NewsParametersForm()
        add_form = AddUrlForm()
        return render(request, 'reader/cached_news.html',
                      {'object_list': qs,
                       'add_form': add_form,
                       'choice_form': news_choice_form,
                       })
    except Exception:
        messages.error(request, f"Couldn't add {url} to tracking list")
        return redirect('cached_news')


def start_page_view(request):
    """ view function for rendering start page"""
    return render(request, 'reader/start.html'
                  )


def cached_news_view(request):
    """ view function for rendering CachedNews page. Takes a queryset from Cache Model to show user info about
    currently tracked URLs"""
    qs = Cache.objects.all()
    news_choice_form = NewsParametersForm()
    add_form = AddUrlForm()
    return render(request, 'reader/cached_news.html',
                  {'object_list': qs,
                   'add_form': add_form,
                   'choice_form': news_choice_form,
                   })


def update_all_cache_view(request):
    """ view function for updating all cached URLs. Takes a queryset from Cache Model to show user info about
    currently tracked URLs"""
    qs = Cache.objects.all()
    news_choice_form = NewsParametersForm()
    add_form = AddUrlForm()
    url_list = [obj.url for obj in qs if obj]
    for url in url_list:
        try:
            news = DjangoRssReader(url, news_limit=None)
            news.save_django_reader_cache()
            messages.success(request, f'{url} successfully updated')
        except Exception:
            messages.error(request, f"Couldn't update {url}")
    return render(request, 'reader/cached_news.html',
                  {'object_list': qs,
                   'add_form': add_form,
                   'choice_form': news_choice_form,
                   })


@cache_page(60 * 15)
def read_news_view(request):
    """View function with a controller to process cached news into output data to render news for reading"""
    _context = {'url': request.GET['url'], 'limit': request.GET['limit'], 'date': request.GET['date']}

    news_url = request.GET['url'] if request.GET['url'] else ''
    news_limit = int(request.GET['limit']) if request.GET['limit'] and int(request.GET['limit']) > 0 else None
    news_date = request.GET['date'].replace('/', ':')
    try:
        qs = Cache.objects.all()
        cache = {}
        for obj in qs:
            if obj and obj.url and obj.cache:
                cache[obj.url] = obj.cache
        processed_cache = DjangoRssReaderCached.limit_news_dict(news_cache=cache, limit=news_limit,
                                                                news_url=news_url, news_date=news_date)
        feed_title = {key: value for key, value in processed_cache.items() if key != 'feed_items'}
        feed_news = [{key: value} for key, value in processed_cache['feed_items'].items()]
        paginator = Paginator(feed_news, 10)  # Show 10  per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        _context['news'] = processed_cache
        _context['feed_title'] = feed_title
        _context['feed_news'] = feed_news
        _context['page_obj'] = page_obj
        return render(request, 'reader/read_news.html', _context)
    except Exception:
        messages.error(request, f"Couldn't get news from cache")
        return redirect('cached_news')


def fresh_news_view(request):
    """ view function for rendering FreshNews page."""
    news_choice_form = FreshNewsParametersForm()
    return render(request, 'reader/fresh_news.html',
                  {'choice_form': news_choice_form,
                   })


@cache_page(60 * 15)
def read_fresh_news_view(request):
    """View function with a controller to process fresh news into output data to render news for reading"""
    _context = {'url': request.GET['url'], 'limit': request.GET['limit']}

    news_url = request.GET['url'] if request.GET['url'] else ''
    news_limit = int(request.GET['limit']) if request.GET['limit'] and int(request.GET['limit']) > 0 else None
    try:
        news = DjangoRssReader(news_url, news_limit=news_limit)
        news.save_django_reader_cache()
        if 'news_dict' in news.__dict__:
            processed_cache = DjangoRssReader.limit_news_dict(news_cache=news.news_dict, limit=news_limit)
        else:
            raise ValueError('No news found')
        feed_title = {key: value for key, value in processed_cache.items() if key != 'feed_items'}
        feed_news = [{key: value} for key, value in processed_cache['feed_items'].items()]
        paginator = Paginator(feed_news, 10)  # Show 10  per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        _context['news'] = processed_cache
        _context['feed_title'] = feed_title
        _context['feed_news'] = feed_news
        _context['page_obj'] = page_obj
        return render(request, 'reader/read_news.html', _context)
    except Exception:
        messages.error(request, f"Couldn't get news from {news_url}")
        return redirect('fresh_news')


@cache_page(60 * 15)
def news_pdf(request):
    """view function to process news to PDF document and return it to user"""
    news = ast.literal_eval(request.POST.get('news', {}))
    template = get_template('reader/output.html')
    _context = {'news': news}
    html = template.render(_context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=news.pdf'
    font_path = 'static/fonts/DejaVuSansMono.ttf'
    pdfmetrics.registerFont(TTFont('DejaVuSansMono', font_path))
    DEFAULT_FONT["helvetica"] = "DejaVuSansMono"
    pisa_status = pisa.CreatePDF(html, dest=response, encoding="utf-8")
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@cache_page(60 * 15)
def news_html(request):
    """view function to process news to HTML document and return it to user"""
    news = ast.literal_eval(request.POST.get('news', {}))
    if news:
        _context = {'news': news}
        template = get_template('reader/output.html')
        html = template.render(_context)
        response = HttpResponse(content_type='html')
        response['Content-Disposition'] = 'attachment; filename=news.html'
        response.writelines(html)
        return response


def page_not_found(request, exception):
    """view function for custom handling Error 404 and rendering it on a template"""
    message = f'Error 404. Page not found, please check URL'
    return render(request, 'reader/exception.html',
                  {'message': message,
                   })


def page_server_error(request, *args, **kwargs):
    """view function for custom handling Error 500 and rendering it on a template"""
    message = 'Error 500. Something went wrong, Server Error happened'
    return render(request, 'reader/exception.html',
                  {'message': message,
                   })


def page_permission_denied(request, *args, **kwargs):
    """view function for custom handling Error 403 and rendering it on a template"""
    message = 'Error 403. Permission Denied for this operation'
    return render(request, 'reader/exception.html',
                  {'message': message,
                   })


def page_bad_request(request, *args, **kwargs):
    """view function for custom handling Error 400 and rendering it on a template"""
    message = 'Error 400. You have made a suspicious from a security perspective request, \noperation stopped'
    return render(request, 'reader/exception.html',
                  {'message': message,
                   })
