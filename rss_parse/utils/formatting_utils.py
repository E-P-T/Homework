from html2text import HTML2Text


def __configure_translator():
    translator = HTML2Text()
    translator.inline_links = False
    translator.wrap_links = False
    return translator


HTML_TO_TEXT_TRANSLATOR = __configure_translator()


def format_date_pretty(pub_date):
    if not pub_date:
        return ""
    return pub_date.strftime("%a, %d %b %Y %H:%M:%S %z")


def get_description_plain(description):
    if not description:
        return description
    desc = description.strip()
    # try to parse description as html
    html = HTML_TO_TEXT_TRANSLATOR.handle(desc)
    return html.rstrip() if html else desc
