## How to run
### Install requirements
```shell
pip install -r .\requirements.txt
```
### Application
```shell
python .\src\rss_reader.py
```
### Tests
```shell
python .\src\test_all.py
```
---
## Print format
### JSON
#### News:
```
{
  "feed": string,
  "items": array of Items
}
```
#### Item:
```
{
  "title": string,
  "date": datetime,
  "link": string,
  "images": array of strings
}
```
### String
Same as JSON but without brackets and quotes
#### News:
```yaml
feed: string
items: 
  array of Items
```
#### Item:
```yaml
title: string
date: datetime
link: string
images: 
  array of strings
```
---
## Caching system
All items were fetched 
will be stored in cached.json 
which is located 
(will be created if it doesn't exist) 
in source folder and will be stored 
in JSON format with checking for duplicates 
