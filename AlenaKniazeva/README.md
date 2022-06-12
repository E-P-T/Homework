<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h2>Description</h2>
    <p>This application is Python RSS-reader. It is implemented to read news from a given feed with prescribed arguments.</p>
    <h2>Requirements</h2>
    <p>The applications require the next Python libraries to be installed: <br><i>requests<br>beautifulsoup4<br>lxml</i></p>
    <p>Necessary libraries may be installed by entering the next command in command line:<br><b>pip install library_name</b></p>
    <h2>Running</h2>
    <p>User can run the application in two ways:</p>
    <ul>
        <li><p>from command line by command:<br> <b>python rss_reader.py source [--version] [--json] [--verbose] [--limit LIMIT] [-h]</b></p>
        <p>positional arguments:<br>
        <dl>
            <dt>source</dt><dd><i>RSS URL</i></dd>
        </dl>
        </p>
        <p>optional arguments:<br>
        <dl>
            <dt>--version</dt><dd><i>Print version info</i></dd>
            <dt>--json</dt><dd><i>Print result as JSON in stdout</i></dd>
            <dt>--verbose</dt><dd><i>Outputs verbose status messages</i></dd>
            <dt>--limit LIMIT</dt><dd><i>Limit news topics if this parameter provided</i></dd>
            <dt>-h, --help</dt><dd><i>Show a help message and exit</i></dd>
        </dl>
        </p>
        </li>
        <li>Second way
        </li>
    </ul>
    <h4>* About JSON structure</h4>
    <p>This application generates JSON with the next structure:</p>
    <p style="margin-left: 40px">{"feed": "Name of sourse feed", <br> "news": [<br>{<br>"title": "title of news_1",<br>"pubdate": "publication date of a news_1",<br>"link": "sourse link for a news_1",<br>"description": "Short description of a content of a news_1"<br>},<br>{<br>"title": "title of news_2",<br>"pubdate": "publication date of a news_2",<br>"link": "sourse link for a news_2",<br>"description": "Short description of a content of a news_2"<br>...<br>]}</p>

</body>
</html>