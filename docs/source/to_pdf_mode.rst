Mode for saving work results to an PDF file.
=============================================

This part of the documentation describes how to save the results of your work in a PDF file.
---------------------------------------------------------------------------------------------

You can start this mode::
    
    $ rss_reader https://rss.nytimes.com/services/xml/rss/nyt/World.xml --to-pdf D:\

The file will be saved as news.pdf.

The save handler in the PDF file is called by the chain template.
Temporary files are stored in the user's directory and are deleted after saving the PDF file.