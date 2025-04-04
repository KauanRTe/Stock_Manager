from django.urls import path
from .views import lista_produtos, home, produtos_por_categoria

urlpatterns = [
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('', home, name='home'),
    path('categoria/<slug:slug>/', produtos_por_categoria, name='produtos_por_categoria'),
]
