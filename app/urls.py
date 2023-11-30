from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register('produto', CRUDProduto),
router.register('pedido', CRUDPedido)
router.register('itenspedido', CRUDItensPedido)


urlpatterns = []+router.urls