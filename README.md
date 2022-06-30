## Documentation

### Minimal requirements:
__Python 3.9__\
On linux please add alias _python_ to _python3_. Look [here](https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3).

### Setup:
#### Virtual Environment (Optional)
Creating Virtual Environment (from the root of the project)\
Windows: `python -m venv ./venv`\
Linux: `virtualenv venv`

Activate Virtual Environment:\
Windows: `./venv/Scripts/activate`\
Linux: `source venv/bin/activate`

*_On Windows you might need to give rights to execute commands from PowerShell via the following command (running as Administrator)_\
`Set-ExecutionPolicy Unrestricted`

*_If you want to exit Virtual Environment please run `deactivate`_

#### Required Steps
Update pip:\
`python -m pip install --upgrade pip`

Install requirements:\
`pip install -r ./requirements.txt`

### Run Application:
Run `python ./rss_parse/rss_reader.py --help` to find available options

### Cache
Application stores RSS Feed in a local storage in a temp folder (and rss_reader sub-folder).\
For more info on what is considered a temp directory please look [here](https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir)

### Run Tests:
Run `pytest ./tests` to run tests

### Package distributive:
To create a distribution package please run\
`pip install -e .`\
You will be able to run `rss_reader` directly\
Also you should run this command as it makes the required font available for fpdf library
