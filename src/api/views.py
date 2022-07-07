from typing import List
from django.shortcuts import render
from django.views import View
from .models import Articulos
from django.http.response import JsonResponse

# Create your views here.
#poo

class ArticulosView(View):
    def get(self,request):
        articulos=list(Articulos.objects.values())
        if len(articulos)>0:
            datos={'message':'Success','articulos':articulos}
        else:
            datos={'message':"No hay articulos en la tabla"}
        return JsonResponse(datos)
    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass