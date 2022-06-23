Welcome to rss_reader.py readme file!



Installization.
First option:
- copy your programm to your folder 
- open your folder in terminal 
- than install requerments: 
	py -m pip install -r requerments.txt
- after that you you can adress to script typing command in terminal:
....\you folder\rss_reader\py rss_reader.py [-h] [-v] [--verbose] [--json] [--limit LIMIT] source

Second option:
- copy your package to your folder 
- open your folder in terminal 
- than install package: 
	py pip install setup.py 
	or
	py pip install .
- after that you you can adress to script typing command in terminal:
....\you folder\rss_reader\py rss_reader.py [-h] [-v] [--verbose] [--json] [--limit LIMIT] source
....\you folder\py rss_reader [-h] [-v] [--verbose] [--json] [--limit LIMIT] source
....\any folder\rss_reader [-h] [-v] [--verbose] [--json] [--limit LIMIT] source


usage: rss_reader.py [-h] [-v] [--verbose] [--json] [--limit LIMIT] source

This program gets information from RSS-channel and returns in user friendly format.

positional arguments:
  source         RSS link for your information

options:
  -h, --help     show this help message and exit
  -v, --version  Print program version and exit.
  --verbose      Outputs verbose status messages.
  --json         Print result as JSON in stdout.
  --limit LIMIT  Limit news topics if this parameter provided.


source is a positional argument that you should always input to your program.

If --limit parameter takes only integer numbers which provide program to return that number of news.
If that parameter not provided, program print all news from RSS-channel. 

If --json parameter not provided, program print to console news in format below.

Feed:[title of the rss site where you get news]
    
Title: [fact [1] title]
Date: [date of that fact[1]]
Link: [link to the fact[1]]
Description: [fact's [1] short summary] 
......
Title: [fact [limit] title]
Date: [date of that fact[limit]]
Link: [link to the fact[limit]]
Description: [fact's [limit] short summary] 


Parameter --json print json string in format that described below. This parameter also takes effect from --limit parameter.

"[title of the rss site where you get news]": [
        {
            "Title": "[date of that fact[1]]",
            "Link": "[link to the fact[1]]",
            "Date": "[date of that fact[1]]",
            "Description": "[fact's [1] short summary]"
        },
        ...........,
        {
            "Title": "[date of that fact[limit]]",      
            "Link": "[link to the fact[limit]]",
            "Date": "[date of that fact[limit]]",
            "Description": "[fact's [limit] short summary]"
        }
    ]
}
