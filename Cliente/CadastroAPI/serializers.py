from rest_framework import serializers
from .models import CadastroCliente

class CadastroClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroCliente
        fields = '__all__'