import datetime
import re
import rss_reader


def isUrlValid(url):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if url is None:
        return False

    # Return if the string
    # matched the ReGex
    if re.search(p, url):
        return True
    else:
        return False

