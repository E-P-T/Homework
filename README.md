## Documentation

### Minimal requirements:
__Python 3.9__

### Setup:
Creating Virtual Environment (from the root of the project)\
`python -m venv ./venv`

Activate Virtual Environment:\
`./venv/Scripts/activate`

*_On Windows you might need to give rights to execute commands from PowerShell via the following command (running as Administrator)_\
`Set-ExecutionPolicy Unrestricted`

*_If you want to exit Virtual Environment please run `deactivate`_

Update pip:\
`python -m pip install --upgrade pip`

Install requirements:\
`pip install -r ./requirements.txt`
 
### Run Application:
Run `python ./rss_parse/rss_reader.py --help` to find available options

### Package distributive:
To create a distribution package please run\
`pip install -e .`
You will be able to run `rss-reader` directly
