first of all 

$ docker-compose up -d --build

$ docker ps : you shoul have 4 containers up

check services are ready

Nginx managin django :  http://localhost:8000

phpmyadmin : http://localhost:8087

```
$ docker-compose exec app django-admin.py startproject app .
```

let's create an app named api

$ docker exec app django-admin createapp api

add the string 'api' as last index of the array INSTALLED_APPS in your settings.py

DATABASE SETTINGS are already set in the file docker-compose.yml and the file settings.py
feel free to change it .

create a Model for your application api and declare it in admin.py

time to check mysql connection running command

$ docker-compose exec app python manage.py migrate

check in localhost:8087 phpMyadmin if you have 10 default django tables inside django-local db
if exits it was success

next step , create a super user


migrate your model Articulos

$ docker-compose exec app python manage.py makemigrations

you can check in migrations/0001_initial.py

and migrate that migration

$ docker-compose exec app python manage.py createsuperuser

pay attention and answer carefully the questions python makes

MIGRATE YOUR MIGRATION

$ docker-compose exec app python manage.py migrate

run the server

$ docker-compose exec app python manage.py runserver

ingress as admin in http://localhost:admin and INSERT A NEW ARTICLE in Articulos table

let's create a view in views.py inside app api importing View from django.views using POO paradigma

and create urls.py inside api app

and register this urls.py inside main urls.py of the project


