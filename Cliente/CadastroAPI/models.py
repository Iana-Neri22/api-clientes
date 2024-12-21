from django.db import models
from .db_connection import db


cadastro_cliente_collection = db['cadastro_cliente']

class CadastroCliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome