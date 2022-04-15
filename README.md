# Django Parser Project

Django API project for parsing all links on a page by URL and getting extended information about their domains from a public API


## Description

The service accepts the URL as a get request parameter. 
After that, all valid links of the page are parsed. 
The resulting links are used as a search parameter in the domain database open API. 
Information about the received domains is recorded in the PostreSQL database in accordance with the URL. 

All actions after receiving the URL occur asynchronously through the Celery.

## Result fields
    url: url-type
    domain: string
    create_date: datetime
    update_date: datetime
    country: string
    isDead: boolean 
    A: list 
    NS: list
    CNAME: list
    MX: list
       exchange: string
       priority: integer
    TXT: list 

***
## Getting started

### Clone remote files

```sh
$ git clone https://github.com/gryroach/Django_Parser_URL.git
$ cd Django_Parser_URL
```
### Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install virtualenv
$ python3 -m venv env
$ source env/bin/activate
```
### Install the dependencies for django project:
```sh
(env)$ pip install -r .web/requirements.txt
```
### Create .env file to configure database settings:
```sh
(env)$ touch .env
(env)$ nano .env
```
### Set the following environment variables:
- ```SECRET_KEY```
- ```DEBUG```
- ```POSTGRES_NAME```
- ```POSTGRES_USER```
- ```POSTGRES_PASSWORD```
- ```OPEN_API_DOMAIN```

> **NOTE**: **When developing this project , OPEN_API_DOMAIN is used as https://api.domainsdb.info/v1/domains/search**

### Run docker-compose
```sh
(env)$ docker-compose up --build -d
```
### Make migrations for Postgres database
```sh
(env)$ docker-compose exec web python manage.py makemigrations
(env)$ docker-compose exec web python manage.py migrate
```
***

### API
- GET -> http://127.0.0.1:8000/api/parser?url=<url_for_parsing>- start parsing page by URL
- GET -> http://127.0.0.1:8000/api/domains - list of all domains with filters and sorting

To get a description of the developed API in Swagger UI format, follow the documentation link:
http://0.0.0.0:8000/api/docs/
