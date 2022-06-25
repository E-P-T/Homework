import os
from urllib.request import urlopen, Request

import fpdf
from django.core.paginator import Paginator
from django.shortcuts import render
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xhtml2pdf.default import DEFAULT_FONT

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
from rss_reader_service.settings import BASE_DIR

from rss_reader import rss_output


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
    """"""
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
        return HttpResponse('We had som errors <pre>' + html + '</pre>')
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


def news_pdf2(request):
    news = ast.literal_eval(request.POST.get('news', {}))

    pdf = fpdf.FPDF()
    pdf.add_font("DejaVuMono", style="",
                 fname="static/fonts/DejaVuSansMono.ttf", uni=True)
    pdf.add_font("DejaVuMono", style="B",
                 fname="static/fonts/DejaVuSansMono-Bold.ttf", uni=True)
    pdf.add_font("DejaVuMono", style="I",
                 fname="static/fonts/DejaVuSansMono-Oblique.ttf", uni=True)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)
    #  setting a separate font for header block
    pdf.set_font('DejaVuMono', 'B', 14)
    pdf.cell(200, 5, txt="=" * 65, ln=1, align='L')
    # trying to use feed logo if it is saved, in case of failure - will use a standard rss logo
    feed_image = 'static/images/rss-header.png'
    if 'feed_media' in news:
        if 'type' not in news['feed_media'] or news['feed_media']['type'].startswith('image'):
            try:
                pdf.image(news['feed_media']['url'], 12, 14, 33, 15)
            except Exception:
                pdf.image(feed_image, 12, 14, 33, 15)
    else:
        pdf.image(feed_image, 12, 14, 33, 15)
    # printing Feed header
    rss_output.PdfConverter.print_cell(pdf, tab=36, text=news.get('feed_title', 'No title'), length=53, line_length=164)
    pdf.cell(200, 2, ln=1, align='L')
    rss_output.PdfConverter.print_cell(pdf, tab=36, text=news.get('feed_description', 'No additional description'), length=53,
                            line_length=164)
    pdf.cell(200, 2, ln=1, align='L')
    feed_link = news.get('feed_link', '')
    if feed_link != 'News sources can be reached through links listed in news':
        rss_output.PdfConverter.print_cell(pdf, tab=36, text=feed_link, link=feed_link, length=53, line_length=164)
    else:
        rss_output.PdfConverter.print_cell(pdf, tab=36, text=feed_link, length=53, line_length=164)
    pdf.cell(200, 5, txt="=" * 65, ln=1, align='L')
    #  converting news
    for num, item in enumerate(sorted(news['feed_items'], reverse=True)):
        pdf.set_font('DejaVuMono', 'B', 14)
        news_title = news["feed_items"][item].get("title", "No title provided")
        news_link = news["feed_items"][item].get("link", "No link provided")  # will also be used later
        rss_output.PdfConverter.print_cell(pdf, text=news_title, length=65, link=news_link)  # link to make Title clickable
        pdf.cell(200, 1, ln=1, align='L')
        pdf.set_font('DejaVuMono', '', 12)
        news_date = f'Publication date: {news["feed_items"][item].get("pubDate", "No publication date provided")}'
        rss_output.PdfConverter.print_cell(pdf, text=news_date, length=65)
        pdf.cell(200, 4, ln=1, align='L')
        news_media = ''
        if 'media' in news["feed_items"][item] and 'url' in news["feed_items"][item]['media']:
            media = news["feed_items"][item]['media']
            news_media = media['url']  # We will use a link to media later in script
            if 'type' not in media or media['type'].startswith('image'):
                temp_name = 'reader/tmp/' + str(num) + 'temp.jpg'
                try:
                    with urlopen(Request(news_media), timeout=3) as response:
                        with open(temp_name, "wb") as temp:
                            temp.write(response.read())
                            pdf.image(temp_name, w=60)
                except Exception:  # if script could not get the image or format not supported, we supress
                    pass  # Exception and will use a link to media later in script
                finally:
                    if os.path.exists('reader/tmp/' + str(num) + 'temp.jpg'):
                        os.remove('reader/tmp/' + str(num) + 'temp.jpg')
        # Printing news description
        news_desc = news["feed_items"][item].get("description", "No description provided")
        rss_output.PdfConverter.print_cell(pdf, text=news_desc, length=75)
        # changing font and colour for printing links (news_link formed previously in news_title section)
        pdf.set_font('DejaVuMono', 'I', 9)
        pdf.cell(200, 4, ln=1, align='L')
        pdf.set_text_color(0, 0, 255)
        rss_output.PdfConverter.print_cell(pdf, text='Link: ' + news_link, length=100, link=news_link, line_height=4)
        if news_media:
            pdf.cell(200, 2, ln=1, align='L')
            rss_output.PdfConverter.print_cell(pdf, text=f'Media link: {news_media}', length=100, link=news_media,
                                    line_height=4)
        pdf.set_font('DejaVuMono', '', 12)
        pdf.set_text_color(0, 0, 0)
        # finishing news item block with printing a separator between news
        pdf.cell(200, 5, txt="-" * 76, ln=1, align='L')
    # converting and saving pdf to file
    file_name = 'reader/tmp/news.pdf'
    pdf.output(file_name)
    response = FileResponse(open(file_name, 'rb'), as_attachment=True)

    return response
