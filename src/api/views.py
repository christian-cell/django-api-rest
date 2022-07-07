from typing import List
from django.shortcuts import render
from django.views import View
from .models import Articulos
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
#poo

class ArticulosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            articulos = list(Articulos.objects.filter(id=id).values())
            if len(articulos) > 0:
                articulo = articulos[0]
                datos = {'message': "Success", 'articulo': articulo}
            else:
                datos = {'message': "Articulo not found..."}
            return JsonResponse(datos)
        else:
            articulos = list(Articulos.objects.values())
            if len(articulos) > 0:
                datos = {'message': "Success", 'articulos': articulos}
            else:
                datos = {'message': "Article not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Articulos.objects.create(name=jd['name'], maker_website=jd['maker_website'], made_at=jd['made_at'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        articulos = list(Articulos.objects.filter(id=id).values())
        if len(articulos) > 0:
            articulo = Articulos.objects.get(id=id)
            articulo.name = jd['name']
            articulo.maker_website = jd['maker_website']
            articulo.made_at = jd['made_at']
            articulo.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Article not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        articulos = list(Articulos.objects.filter(id=id).values())
        if len(articulos) > 0:
            Articulos.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Article not found..."}
        return JsonResponse(datos)