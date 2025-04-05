from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)



    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    preco = models.FloatField(default=0)
    descricao = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 
    estoque = models.ForeignKey('Estoque', on_delete=models.CASCADE, related_name='produtos' )

    def __str__(self):
        return f"{self.nome} ({self.categoria})"
    
class Estoque(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='estoque')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"Estoque de {self.usuario.username}"
