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
    

    def get(self,request,id=0):
        if(id>0):
            articulos = list(Articulos.objects.filter(id=id).values())
            if len(articulos) > 0:
                articulo = articulos[0]
                datos={'message':'Success','articulos':articulo}
            else:
                datos={'message':'no se encontró el articulo por id'}
            return JsonResponse(datos)
        else:
            articulos=list(Articulos.objects.values())
            if len(articulos)>0:
                datos={'message':'Success','articulos':articulos}
            else:
                datos={'message':"No hay articulos en la tabla"}
            return JsonResponse(datos)
    def post(self,request):
       
        jd = json.loads(request.body)
        Articulos.objects.create(name=jd['name'],maker_website=jd['maker_website'],made_at=jd['made_at'])
        datos =  {'message':'Success'}
        return JsonResponse(datos)
    def put(self,request):
        pass
    def delete(self,request):
        pass