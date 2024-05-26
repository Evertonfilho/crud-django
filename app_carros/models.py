from django.db import models

class Carro(models.Model):
    id_carro = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100)
    quantidade_portas = models.IntegerField()
    tipo_combustivel = models.CharField(max_length=50)
    ano_carro = models.IntegerField()
    placa = models.CharField(max_length=20)
    estado = models.CharField(max_length=20) 
    valor_comprado = models.DecimalField(max_digits=10, decimal_places=2)
    valor_vendido = models.DecimalField(max_digits=10, decimal_places=2)
