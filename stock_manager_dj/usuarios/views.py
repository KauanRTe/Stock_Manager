from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm
from estoque.models import Estoque

# Create your views here.
def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Estoque.objects.create(usuario=usuario, nome=f"Estoque de {usuario.username}")
            login(request, usuario)
            return redirect("home:home")
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            erro = 'O usuário ou a senha estão inválidos.'
            return render(request, 'usuarios/login.html', {'erro': erro})
    return render(request, 'usuarios/login.html')


