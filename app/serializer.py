from rest_framework import serializers
from .models import *


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto 
        fields = ["id","Nome", "Preco", "Foto"]

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id','cliente','data_pedido','preco_total', 'metodo', 'status_pedido']

class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Itens
        fields = ["produto","quantidade","precoXquantidade","pedido"]