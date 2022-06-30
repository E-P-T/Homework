 _ __  ___  ___         _ __   ___   __ _   __| |  ___  _ __
| '__|/ __|/ __|       | '__| / _ \ / _` | / _` | / _ \| '__|
| |   \__ \\__ \       | |   |  __/| (_| || (_| ||  __/| |
|_|   |___/|___/ _____ |_|    \___| \__,_| \__,_| \___||_|
                |_____|


Welcome to rss_reader.py readme file!

Tested on Windows 10!

usage: rss_reader.py [-h] [--date DATE] [-v] [--verbose] [--to-html] [--to-epub] [--json] [--limit LIMIT] [source]

This program gets information from RSS-channel and returns in user friendly format.

positional arguments:
  source         RSS link for your information

options:
  -h, --help     show this help message and exit
  --date DATE    Get news form the database by date.
  -v, --version  Print program version and exit.
  --verbose      Outputs verbose status messages.
  --to-html      Return HTML file to C:\rss_reader\html_files
  --to-epub      Return HTML file to C:\rss_reader\epub_files
  --json         Print result as JSON in stdout.
  --limit LIMIT  Limit news topics if this parameter provided.
 


source is a positional argument that you should input to your program, when you have to get information from the RSS-channel.

If --limit parameter takes only integer numbers which provide program to return that number of news.
If that parameter not provided, program print all news from RSS-channel. 


--json is a parameter that print json string in format that described below. This parameter also takes effect from --limit parameter.

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

--to-html is parameter that saves information to C:\rss_reader\html_files folder with given name in date time format `%d%m%y%H%M`.

--to-epub is parameter that saves information to C:\rss_reader\epub_files folder with given name in date time format `%d%m%y%H%M`.

--to-epub and --to-html also works with other parameters.

--date is a parameter to get information from the database. This parameter should take a date in `%Y%m%d` format.
For example: `--date 20191020` 
With --to-epub or --to-html parameter program saves html or epub files to corresponding folders with  `%Y%m%d` nameformat.
--date with source parameter returns data from database according to date and source link.
Just --date parameter returns to console news in format described below:

News on date [date]!
    
Title: [fact [1] title]
Date: [date of that fact[1]]
Link: [link to the fact[1]]
Description: [fact's [1] short summary] 
......
Title: [fact [limit] title]
Date: [date of that fact[limit]]
Link: [link to the fact[limit]]
Description: [fact's [limit] short summary] 


With --json parameter  returns JSON string:

"[date]": [
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

Running unittests for rss_reader:
py -m unittest rss_reader/dbh_tests.py
py -m unittest rss_reader/tests.py