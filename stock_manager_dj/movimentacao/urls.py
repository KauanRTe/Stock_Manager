from django.urls import path
from . import views

app_name = 'movimentacao'

urlpatterns = [
     path('nova/', views.nova_movimentacao, name='nova_movimentacao'),
     path('produto/<int:produto_id>/movimentacoes/', views.movimentacoes_produto, name='movimentacoes_produto'),
]