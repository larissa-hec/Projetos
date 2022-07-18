from django.db import models

class cliente(models.Model):
    Nome_completo = models.CharField(max_length=255)
    Conta_corrente = models.CharField(max_length=6)
    Agencia = models.CharField(max_length=4)
    Senha = models.CharField( max_length=6)
    CPF = models.CharField(max_length=11)
    Saldo = models.CharField
    Endereço = models.CharField(max_length=255)
    CEP = models.CharField(max_length=8)
    Telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=255)

