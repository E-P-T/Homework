## RSS Reader

### Setup:
#### Virtual Environment
Create Virtual Environment\
Linux: `virtualenv venv`\
Windows: `python -m venv ./venv`\

Activate Virtual Environment:\
Linux: `source venv/bin/activate`\
Windows: `./venv/Scripts/activate`\

#### Pip Usage:
Update pip:\
`python -m pip install --upgrade pip`

### Requirements: 
Install requirements using: `pip install -r .\requirements.txt`

### Run Application:
Run `python ./rss_reader.py -h` to find available options

### Cache
Application stores RSS Feed using buildin pickle module, which is located in the root directory of the project.
Particularly, we are using it to convert python object into byte stream to store it in our database.
For more information regarding its usage, refer to the [official documentation](https://docs.python.org/3/library/pickle.html). 

### Run Tests:
Tests for this project can mainly be found in the fourth version/iteration of the task.

### Package distributive:
To install package distributive you can install sudo, to be able able to accept it as the system wide CLI.

### Output format
The project supports HTML, which means you are able to export news to the HTML5 format.

### Json structure
Json structure looks as follows:
```
{
  "title": string,
  "date": datetime,
  "link": string,
  "image": string,
  "channel": string,
  "source": string
}
```

