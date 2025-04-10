from django.urls import path
from . import views

app_name = "estoque"
urlpatterns = [
    path('categoria/<slug:slug>/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('nova-categoria/', views.criar_categoria, name='criar_categoria'),
    path('novo-produto/', views.criar_produto, name='criar_produto'),
    path('novo-estoque/', views.criar_estoque, name='criar_estoque'),
    path('configurar-estoques/', views.configurar_estoques, name='configurar_estoques'),
    path('renomear-estoque/', views.renomear_estoque, name='renomear_estoque'),
    path('deletar-estoque/', views.deletar_estoque, name='deletar_estoque'),
]
