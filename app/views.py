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

class CRUDPedido(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def list(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(" ")[1]
        dados_TOKEN = AccessToken(token)
        usuario = dados_TOKEN['user_id']
        PedidoObject = Pedido.objects.filter(cliente_id=usuario)
        serializer = PedidoSerializer(PedidoObject, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(" ")[1]
        dados_TOKEN = AccessToken(token)
        usuario = dados_TOKEN['user_id']
        usuarioObject = Usuario.objects.get(id=usuario)
        dados = request.data

        criar = Pedido.objects.create(cliente=usuarioObject, preco_total=dados['preco_total'])
        criar.save()

        serializer = PedidoSerializer(criar)

        return Response(serializer.data)
    

class CRUDItensPedido(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Pedido_Itens.objects.all()
    serializer_class = ItensPedidoSerializer

    def create(self, request, *args, **kwargs):
        dados = request.data

        precoTotal = 0
        produto= Produto.objects.get(id=dados['produto'])
        print(produto)
        pedido = Pedido.objects.get(id=dados['pedido'])

        criar = Pedido_Itens.objects.create(produto=produto, quantidade=dados["quantidade"],precoXquantidade=produto.Preco * int(dados['quantidade']),pedido=pedido)
        criar.save()
        precos = Pedido_Itens.objects.filter(pedido_id=dados['pedido'])

        for preco in precos:
            precoTotal += preco.precoXquantidade

        Pedido.objects.filter(id=dados['pedido']).update(preco_total=precoTotal)

        serializer = ItensPedidoSerializer(criar)

        return Response(serializer.data)