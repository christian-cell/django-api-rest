from django.urls import path
from .views import ArticulosView

urlpatterns = [
    path('articulos/' , ArticulosView.as_view() , name='lista_de_articulos')
]
