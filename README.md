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

