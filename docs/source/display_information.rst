Display of information.
=======================

This part of the documentation describes how rss-reader displays information.
-----------------------------------------------------------------------------

Information display:
--------------------
Normally.
~~~~~~~~~~~
    * When all data is available.
  
        .. figure:: /images/output.jpg

    * When there is missing data.

        .. figure:: /images/output-empty.jpg
    
    * When the date parameter is used and the result contains different news sources.

        .. figure:: /images/date_parametr.jpg


With the given \-\-json parameter:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    * When all data is available.
  
        .. code-block:: JSON

            [
                {
                    "title_web_resource": "Yahoo News - Latest News & Headlines",
                    "link": "https://news.yahoo.com/rss/",
                    "items": 
                        [
                            {
                                "title": "1955 warrant family seeks",
                                "link": "https://news.yahoo.com/1955-war79.html",
                                "pubDate": "2022-06-29T19:41:30Z",
                                "source": "Associated Press",
                                "content": {
                                    "url": "https://s.yimg.com/uu/api/res/1.2/z8bf83",
                                    "title": null
                                }
                            }
                        ]
                }
            ]

    * When there is missing data.
    
        .. code-block:: JSON

            [
                {
                    "title_web_resource": "Yahoo News - Latest News  Headlines",
                    "link": "https://news.yahoo.com/rss/",
                    "items": 
                        [
                            {
                                "title": "Biden takes",
                                "link": "",
                                "pubDate": "2022-06-18T14:37:24Z",
                                "source": "",
                                "content": {
                                    "url": "",
                                    "title": null
                                }
                            }
                        ]
                }
            ]


With the given \-\-date and \-\-json parameter:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: JSON

    [
        {
            "title_web_resource": "Yahoo News - Latest News & Headlines",
            "link": "https://news.yahoo.com/rss/",
            "items": 
                [
                    {
                        "title": "Hong Kongs",
                        "link": "https://news.yahoo.com/hong.html",
                        "pubDate": "2022-06-01",
                        "source": "Associated Press",
                        "content": {
                            "url": "https://s.yimg.com/uu/api/reen/ap.org/0c",
                            "title": null
                        }
                    }
                ]
        },
        {
            "title_web_resource": "Новости ООН - Здравоохранение",
            "link": "https://news.un.org/feed/rss.xml",
            "items": 
                [
                    {
                        "title": "ВОЗ: необходимы антибиотики нового поколения",
                        "link": "https://news.un.org/08.html",
                        "pubDate": "2022-06-01",
                        "source": "Associated Press",
                        "content": {
                        "url": "https://s.yimg.com/uu/api-rg/0725fc",
                        "title": null
                        }
                    }
                ]
        }
    ]