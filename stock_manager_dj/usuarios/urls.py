from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar'),
]
