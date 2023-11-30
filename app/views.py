from django.shortcuts import render
from rest_framework import viewsets
from .models import Produto,Pedido,Usuario, Pedido_Itens
from .serializer import ProdutoSerializer, PedidoSerializer, ItensPedidoSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CRUDProduto(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

