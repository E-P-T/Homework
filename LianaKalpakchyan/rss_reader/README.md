[Readme for RSS reader].
===================================================================
One-shot command-line RSS reader.
RSS reader is a command-line utility which receive [RSS](https://wikipedia.org/wiki/RSS) URL and prints results in human-readable format.
The program allows you to read news articles directly in the console output. 


[Common usage]:
===================================================================
    usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] [--date DATE] [--to-pdf [TO_PDF ...]] [--to-html [TO_HTML ...]] [source]

    One-shot command-line RSS reader ^_^
    
    positional arguments:
      source                RSS URL
    
    optional arguments:
      -h, --help            show this help message and exit
      --version             Print version info
      --json                Print result as JSON in stdout
      --verbose, --v        Outputs verbose status messages
      --limit LIMIT         Limit news topics if this parameter provided
      --date DATE           Takes a date. For example: for "--date 20191020" news from the specified day will be printed out.
      --to-pdf [TO_PDF ...]
                            Conversion of news into a PDF format
      --to-html [TO_HTML ...]
                            Conversion of news into an HTML format


