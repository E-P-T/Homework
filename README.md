 _ __  ___  ___         _ __   ___   __ _   __| |  ___  _ __
| '__|/ __|/ __|       | '__| / _ \ / _` | / _` | / _ \| '__|
| |   \__ \\__ \       | |   |  __/| (_| || (_| ||  __/| |
|_|   |___/|___/ _____ |_|    \___| \__,_| \__,_| \___||_|
                |_____|


Welcome to rss_reader.py readme file!

usage: rss_reader.py [-h] [--date DATE] [-v] [--verbose] [--json]          
                     [--limit LIMIT]                                       
                     [source]                                              
                                                                           
This program gets information from RSS-channel and returns in user friendly
format.                                                                    
                                                                           
positional arguments:                                                      
  source         RSS link for your information                             
                                                                           
options:                                                                   
  -h, --help     show this help message and exit                           
  --date DATE    Get news form the database by date.                       
  -v, --version  Print program version and exit.                           
  --verbose      Outputs verbose status messages.                          
  --json         Print result as JSON in stdout.                           
  --limit LIMIT  Limit news topics if this parameter provided.   


source is a positional argument that you should input to your program, when you have to get information from the RSS-channel.

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

--date - parameter to get information from the database. This parameter should take a date in `%Y%m%d` format.
For example: `--date 20191020`

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


With --json parameter this parameter returns JSON string:

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