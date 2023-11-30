from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

class Usuario(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    DataNasc = models.DateField()
    Logradouro = models.CharField(max_length=100)
    Numero = models.PositiveIntegerField()
    CEP = models.PositiveIntegerField()
    Cidade = models.CharField(max_length=50)
    UF = models.CharField(max_length=2)
    Bairro = models.CharField(max_length=50)

    objects = CustomUserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "Logradouro", "Numero", "CEP", "Cidade", "UF", "Bairro", 'DataNasc']

    def __str__(self) -> str:
        return str(self.username)

class Produto(models.Model):
    Nome = models.CharField(max_length=100)
    Preco = models.DecimalField(decimal_places=2, max_digits=4)
    Foto = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.Nome)

class Pedido(models.Model):
    STATUS_PD_ENTREGUE = 'E'
    STATUS_PD_CANCELADO = 'C'
    STATUS_PD_TRANSPORTE = 'T'
    STATUS_PD_PREPARACAO = 'P'
    
    STATUS_PD_CHOICES = (
        (STATUS_PD_ENTREGUE,'Entregue'),
        (STATUS_PD_CANCELADO, 'Cancelado'),
        (STATUS_PD_TRANSPORTE,'Transporte'),
        (STATUS_PD_PREPARACAO,'Preparação'),
    )
    PAGAMENTO_PIX = 'P'
    PAGAMENTO_CARTAO = 'C'
    PAGAMENTO_BOLETO = 'B'
    PAGAMENTO_CHOICES = [
        (PAGAMENTO_PIX,'PIX'),
        (PAGAMENTO_CARTAO, 'CARTÃO'),
        (PAGAMENTO_BOLETO,'BOLETO')
    ]
    metodo = models.CharField(max_length=1, choices=PAGAMENTO_CHOICES ,default=PAGAMENTO_PIX)
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    data_pedido = models.DateField(auto_now=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status_pedido = models.CharField(max_length=1, choices=STATUS_PD_CHOICES, default=STATUS_PD_PREPARACAO)

    def __str__(self) -> str:
        return str(self.id)

class Pedido_Itens(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    precoXquantidade = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

 