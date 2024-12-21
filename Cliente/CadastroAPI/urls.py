from django.urls import path

from . import views

urlpatterns = [
        path('',views.index, name='index'),
        path('cadastrar-cliente/',views.cadastrar_cliente, name='cadastrar-cliente'),
        path('buscar-clientes/',views.buscar_clientes, name='buscar-clientes'),
    ]