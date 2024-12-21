from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CadastroAPI.models import cadastro_cliente_collection
from CadastroAPI.serializers import CadastroClienteSerializer



@csrf_exempt
def index(request):
    return JsonResponse(request, 'App rodando')


def cadastrar_cliente(request):
    cliente ={
        'cpf': '000000000',
        'nome': 'John Smith',
        'email': 'john@gmail.com',
    }             
    cadastro_cliente_collection.insert_one(cliente)
    return JsonResponse("Cadastro realizado com sucesso!", safe=False)

def buscar_clientes(request):
    clientes = []
    for cliente in cadastro_cliente_collection.find():
        cliente['_id'] = str(cliente['_id'])
        clientes.append(cliente)
    return JsonResponse(clientes, safe=False)

@csrf_exempt
def cadastro_clienteAPI(request, id=0):
    if request.method == 'GET':
        cadastroCliente = CadastroCliente.objects.all()
        cadastroCliente_serializer = CadastroClienteSerializer(cadastroCliente, many=True)
        return JsonResponse(cadastroCliente_serializer.data, safe=False)
    if request.method == 'POST':
        cadastroCliente_data = JSONParser().parse(request)
        cadastroCliente_serializer = CadastroClienteSerializer(data=cadastroCliente_data)
        if cadastroCliente_serializer.is_valid():
            cadastroCliente_serializer.save()
            return JsonResponse("Cadastro realizado com sucesso!", safe=False)
        return JsonResponse("Falha ao cadastrar.", safe=False)
    if request.method == 'PUT':
        cadastroCliente_data = JSONParser().parse(request)
        cadastroCliente = CadastroCliente.objects.get(id=cadastroCliente_data['id'])
        cadastroCliente_serializer = CadastroClienteSerializer(cadastroCliente, data=cadastroCliente_data)
        if cadastroCliente_serializer.is_valid():
            cadastroCliente_serializer.save()
            return JsonResponse("Cadastro atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar.", safe=False)
    if request.method == 'DELETE':
        cadastroCliente = CadastroCliente.objects.get(id=id)
        cadastroCliente.delete()
        return JsonResponse("Cadastro deletado com sucesso!", safe=False)

