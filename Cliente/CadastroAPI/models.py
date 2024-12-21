from django.db import models
from .db_connection import db
from pymongo import MongoClient


cadastro_cliente_collection = db['cadastro_cliente']

class Cliente(models.Model):

    def __init__(self, CPF, email, nome):
        self.CPF = CPF
        self.email = email
        self.nome = nome

        self.cliente = {
            "CPF": self.CPF,
            "nome": self.nome,
            "email": self.email
        }
    
    def __str__(self):
        return Cliente.cliente