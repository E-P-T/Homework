from html2text import HTML2Text


def __configure_translator():
    translator = HTML2Text()
    translator.inline_links = False
    translator.wrap_links = False
    return translator


HTML_TO_TEXT_TRANSLATOR = __configure_translator()


def format_date_pretty(pub_date):
    """
    Format date in a human-readable form
    """
    if not pub_date:
        return ""
    return pub_date.strftime("%a, %d %b %Y %H:%M:%S %z")


def get_description_plain(description):
    """
    Format a text that might be an HTML by parsing its tags and conveting them to plain text alternatives
    """
    if not description:
        return description
    desc = description.strip()
    # try to parse description as html
    html = HTML_TO_TEXT_TRANSLATOR.handle(desc)
    return html.rstrip() if html else desc
