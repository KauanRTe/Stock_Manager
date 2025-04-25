from django.contrib import admin
from .models import Categoria, Produto, Estoque

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Estoque)