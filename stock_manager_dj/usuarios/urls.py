from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('logout/', LogoutView.as_view(next_page='home:home'), name='logout'),
    path('login/', views.login_usuario, name='login')
]
