Program launch
==============

This part of the documentation describes how to run rss-reader.
---------------------------------------------------------------

To start rss-reader, just run this simple command in the terminal of your choice::

    $ python -m rss_reader

The program supports the following keys:
    * source - RSS URL. Required argument.
    * \-\-verbose - Outputs verbose status messages.a
    * \-\-json - Print result as JSON in stdout.
    * \-\-limit - Limit news topics if this parameter provided.
    * \-\-version - Print version info.


Information display:
--------------------
Normally.
~~~~~~~~~~~
    * When all data is available.
  
        .. figure:: /images/output.jpg

    * When there is missing data.

        .. figure:: /images/output-empty.jpg


With the given \-\-json parameter:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    * When all data is available.
  
        .. code-block:: JSON

            {
                'title_web_resource': 'Yahoo News - Latest News & Headlines',         
                'items':
                    [
                        {
                        'title': 'Wisconsin election investigator says he deleted records',
                        'link': 'https://news.yahoo.com/wisconsin999.html',
                        'pubDate': '2022-06-23T15:52:47Z',
                        'source': 'Associated Press',                    
                        'content': {
                            'url':'https://s.yimg.com/uu/api5f67f7c68',
                            'title': None}
                        }
                    ]
            }

    * When there is missing data.
    
        .. code-block:: JSON

            {
                'title_web_resource': 'Yahoo News - Latest News & Headlines',         
                'items':
                    [
                        {
                        'title': 'Wisconsin election investigator says he deleted records',
                        'link': '',
                        'pubDate': '2022-06-23T15:52:47Z',
                        'source': '',                    
                        'content': {
                            'url':'',
                            'title': None}
                        }
                    ]
            }
