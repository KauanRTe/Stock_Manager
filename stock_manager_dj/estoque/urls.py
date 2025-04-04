from django.urls import path
from .views import lista_produtos, produtos_por_categoria, relatorio_estoque

urlpatterns = [
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('categoria/<slug:slug>/', produtos_por_categoria, name='produtos_por_categoria'),
    path('relatorio/', relatorio_estoque, name='relatorio_estoque')
]
