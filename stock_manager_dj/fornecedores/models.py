from django.db import models
from estoque.models import Estoque

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='fornecedores', blank=True, null=True)

    def __str__(self):
        return self.nome
