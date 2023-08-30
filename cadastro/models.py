from django.db import models

class Clientes(models.Model):
    nome = models.TextField(max_length=50, verbose_name='Nome')
    telefone = models.IntegerField(verbose_name='telefone')
    endereco = models.TextField(max_length=255, verbose_name='Endereço')
