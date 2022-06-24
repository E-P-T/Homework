import os
import sys

import django

project_path = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "rss_reader_service.settings")
django.setup()

from reader.reader import DjangoRssReader


if __name__ == '__main__':
    news = DjangoRssReader('http://www.gazeta.ru/export/gazeta_rss.xml')
    news.save_django_reader_cache()
