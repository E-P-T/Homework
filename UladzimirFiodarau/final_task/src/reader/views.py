import ast

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xhtml2pdf.default import DEFAULT_FONT
from xhtml2pdf import pisa

from .models import Cache
from .forms import AddUrlForm, NewsParametersForm, FreshNewsParametersForm
from .reader import DjangoRssReader, DjangoRssReaderCached

__all__ = ['cached_news_view',
           'read_news_view',
           'fresh_news_view',
           'read_fresh_news_view',
           'news_pdf',
           'news_html',
           'page_not_found',
           'page_server_error',
           'page_permission_denied',
           'page_bad_request',
           'add_news',
           'start_page_view'
           ]


def add_news(request):
    url = request.POST.get('url')
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


def start_page_view(request):
    return render(request, 'reader/start.html'
                  )


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
    feed_news = [{key: value} for key, value in processed_cache['feed_items'].items()]
    paginator = Paginator(feed_news, 10)  # Show 10  per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    _context['news'] = processed_cache
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
    feed_news = [{key: value} for key, value in processed_cache['feed_items'].items()]
    paginator = Paginator(feed_news, 10)  # Show 10  per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    _context['news'] = processed_cache
    _context['feed_title'] = feed_title
    _context['feed_news'] = feed_news
    _context['page_obj'] = page_obj
    return render(request, 'reader/read_news.html', _context)


def news_pdf(request):
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


def news_html(request):
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
    message = f'Error 404. Page not found, please check URL'
    return render(request, 'reader/exception.html',
                  {'message': message,
                   })


def page_server_error(request, *args, **kwargs):
    message = 'Error 500. Something went wrong, Server Error happened'
    return render(request, 'reader/exception.html',
                  {'message': message,
                   })


def page_permission_denied(request, *args, **kwargs):
    message = 'Error 403. Permission Denied for this operation'
    return render(request, 'reader/exception.html',
                  {'message': message,
                   })


def page_bad_request(request, *args, **kwargs):
    message = 'Error 400. You have made a suspicious from a security perspective request, \noperation stopped'
    return render(request, 'reader/exception.html',
                  {'message': message,
                   })