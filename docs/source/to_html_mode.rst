Mode for saving work results to an HTML file.
=============================================

This part of the documentation describes how to save the results of your work in a HTML file.
---------------------------------------------------------------------------------------------

You can start this mode::
    
    $ rss_reader https://rss.nytimes.com/services/xml/rss/nyt/World.xml --to-html D:\

The file will be saved as news.html.

The save handler in the html file is called through the chain pattern, and the specific way
the file is generated is determined through the strategy pattern.