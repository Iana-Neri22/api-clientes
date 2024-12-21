from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from CadastroAPI.models import cadastro_cliente_collection, Cliente



@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse('Aplicação rodando', safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ClienteView(View):

    def get(self, req):
        clientes = []
        for cliente in cadastro_cliente_collection.find():
            cliente['_id'] = str(cliente['_id'])
            clientes.append(cliente)
        return JsonResponse(clientes, safe=False)


    def post(self, req):
        cliente = {
            "CPF": req.POST['CPF'],
            "nome": req.POST['nome'],
            "email": req.POST['email']
        }
        cadastro_cliente_collection.insert_one(cliente)
        return JsonResponse("Cadastro realizado com sucesso!", safe=False)
    
    def delete(self, req):
        Cliente.objects.filter(CPF=req.POST['CPF']).delete()
        return JsonResponse("Cliente deletado com sucesso!", safe=False)
    
