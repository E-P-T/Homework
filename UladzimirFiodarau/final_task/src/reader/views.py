from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View

from .models import Cache
from .forms import AddUrlForm, NewsParametersForm, FreshNewsParametersForm
from .reader import DjangoRssReader, DjangoRssReaderCached
import ast

from django.http import HttpResponse, FileResponse
import io
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from xhtml2pdf import pisa


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
    feed_news = [{key: value}for key, value in processed_cache['feed_items'].items()]
    paginator = Paginator(feed_news, 10)  # Show 10  per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    _context['news'] = processed_cache
    _context['feed_title'] = feed_title
    _context['feed_news'] = feed_news
    _context['page_obj'] = page_obj

    return render(request, 'reader/read_news.html', _context)


def news_pdf(request):
    # create bytestream buffer
    buffer = io.BytesIO()
    canv = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    # creating object
    textob = canv.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    lines = ['1', '2', '3']

    for line in lines:
        textob.textLine(line)

    canv.drawText(textob)
    canv.showPage()
    canv.save()
    buffer.seek(0)

    # return file
    return FileResponse(buffer, as_attachment=True, filename='list.pdf')


def news_html(request):
    news = ast.literal_eval(request.POST.get('news', {}))
    if news:
        response = HttpResponse(content_type='html')
        response['Content-Disposition'] = 'attachment; filename=news.html'

        html_buffer = ['<!DOCTYPE html>',
                       '<html>',
                       '<head><meta charset="utf-8"><title>News gathered by rss_reader</title></head>',
                       ]
        # forming Feed info block
        html_buffer.append(f'<h1 style="text-align:left">{"=" * 83}</h1>')
        feed_image = 'https://www.ict4dconference.org/wp-content/uploads/2020/10/rss-feed-logo.png'
        if 'feed_media' in news:
            if 'type' not in news['feed_media'] or news['feed_media']['type'].startswith('image'):
                feed_image = news['feed_media']['url']
        feed_title = news.get('feed_title', 'No title')
        html_buffer.append(f'<img src="{feed_image}" alt="Logo" width="120" height="60" style="float:left">'
                           f'<h1 style = "margin-left: 130px">{feed_title}</h1>')
        feed_desc = news.get('feed_description', 'No additional description')
        html_buffer.append(f'<h2 style = "margin-left: 130px">{feed_desc}</h2>')
        feed_link = news.get('feed_link', '')
        if feed_link != 'News sources can be reached through links listed in news':
            html_buffer.append(f'<h3 style = "margin-left: 130px"><a href={feed_link}>{feed_link}</a></h3>')
        else:
            html_buffer.append(f'<h3 style = "margin-left: 130px">{feed_link}</a></h3>')
        html_buffer.append(f'<h1 style="text-align:left">{"=" * 83}</h1>')
        # forming news items
        for item in sorted(news['feed_items'], reverse=True):
            news_title = news["feed_items"][item].get("title", "No title provided")
            # checking for media and its type for forming the document
            news_media = None
            news_image = None
            if 'media' in news["feed_items"][item] and 'url' in news["feed_items"][item]['media']:
                media = news["feed_items"][item]['media']
                news_media = media['url']  # We will use a link to media later in script
                if 'type' not in media or media['type'].startswith('image'):
                    news_image = media['url']
            tab = 330 if news_image else 0
            # printing image if found and title
            if news_image:
                html_buffer.append(f'<img src="{news_image}" alt="Image" width="320" height="200" style="float:left">'
                                   f'<h3 style = "margin-left: {tab}px">{news_title}</h3>')
            else:
                html_buffer.append(f'<h3 style = "margin-left: 0px">{news_title}</h3>')
            # printing publication date
            news_date = f'Publication date: {news["feed_items"][item].get("pubDate", "No publication date provided")}'
            html_buffer.append(f'<p style = "margin-left: {tab}px">{news_date}</p>')
            # printing description
            news_desc = news["feed_items"][item].get("description", "No description provided")
            html_buffer.append(f'<p style = "margin-left: {tab}px">{news_desc}</p><br>')
            # printing news link and media link
            news_link = news["feed_items"][item].get("link", "No link provided")
            if news_link != "No link provided":
                html_buffer.append(f'<p style = "margin-left: {tab}px"><a href={news_link}>{news_link}</a><p>')
            else:
                html_buffer.append(f'<p style = "margin-left: {tab}px"><{news_link}<p>')
            if news_media:
                html_buffer.append(f'<p style = "margin-left: {tab}px"><a href={news_media}>Media link: {news_media}'
                                   f'</a><p>')
            # finishing news item block with printing a separator between news
            html_buffer.append(f'<p style="text-align:left">{"-" * 280}</p>')
        html_buffer.append('</html>')

        response.writelines(html_buffer)
        return response


def html_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePdf(View):
    def post(self, request, *args, **kwargs):
        _context = {}
        news = ast.literal_eval(request.POST.get('news', {}))
        _context['news'] = news
        # getting the template
        pdf = html_to_pdf('reader/output.html', _context)

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
