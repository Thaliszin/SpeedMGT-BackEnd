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


 