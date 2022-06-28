import logging

import requests


# Deprecated: too time-consuming
def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    return r.headers["content-type"] in image_formats


# Deprecated: too time-consuming
def is_url_html(html_url):
    html_format = 'text/html'
    r = requests.head(html_url)
    return html_format in r.headers['content-type']


def get_media_link_type(url: str) -> str:
    logging.info(f'Classifying media link type for {url}')
    if url.split('.')[-1] in ('jpg', 'jpeg', 'png', 'gif'):
        return '(Image)'
    return '(Link)'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def validate_method_args(func):
    def wrapper(self, *args):
        for arg, (arg_name, arg_type) in zip(args, func.__annotations__.items()):
            if not isinstance(arg, arg_type):
                raise TypeError(f'The argument: "{arg_name}", must be of type "{arg_type.__name__}",'
                                f' but received: "{type(arg).__name__}"')
        return func(self, *args)

    return wrapper
