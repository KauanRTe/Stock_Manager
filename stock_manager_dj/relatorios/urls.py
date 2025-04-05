from django.urls import path
from . import views

app_name = 'relatorios'

urlpatterns = [
    path('estoque/', views.relatorio_estoque, name='relatorio_estoque'),
]