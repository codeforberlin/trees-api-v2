# trees-api-v2

## Setup

``` bash
python3 -m venv env
source env/bin/activate
cp config/settings/sample.local.py config/settings/local.py
pip install -r requirements.txt
```

Create `local.py` and edit for database credentials:

``` bash
cp config/settings/sample.local.py config/settings/local.py
```

Setup database:

``` bash
./manage.py sqlcreate  # use output to create database user
./manage.py migrate
```

## Usage

Run development server

``` bash
./manage.py runserver
```

Create config file like the following:

``` yml
feature_name: 's_uferbaeume'
url: 'https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_uferbaeume?service=wfs&version=2.0.0&request=GetFeature&typeNames=s_uferbaeume'
file_name: /srv/trees/files/s_uferbaeume.xml
fields:
  identifier: gml_id
  species: ART
  genus: GATTUNG
  borough: BEZIRK
  year: PFLANZJAHR
  age:
  circumference: STAMMUMFAN
  height: BAUMHOEHE
```

where `feature_name` is an assigned name, `url` is the full wfs request to the service, `file_name` is the place to store the download on the local system, and `fields` is a mapping of the attributes of the api to the property fields of the service.

Then, fetch and ingest the data from the WFS service using:

``` bash
./manage.py fetch /path/to/config.yml
./manage.py ingest /path/to/config.yml
```

## Making queries

On the development server the api is available at http://localhost:8000/trees.

* Filter trees with given properties: http://localhost:8000/trees/?genus=Abies
* For numerical fields `gt` (>), `gte` (>=), `lt` (<), `lte` (<=) can be used: http://localhost:8000/trees/?height__gt=10
* All trees with a given distance to point (or less) can be retrieved: http://localhost:8000/trees/?dist=100&point=13.381018,52.498606
