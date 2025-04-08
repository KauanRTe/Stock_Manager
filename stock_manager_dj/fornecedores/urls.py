from django.urls import path
from . import views

app_name = 'fornecedores'

urlpatterns = [
    path('novo-fornecedor', views.criar_fornecedor, name='criar_fornecedor')
]
