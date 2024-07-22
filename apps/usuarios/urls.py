from django.urls import path
from apps.usuarios.views import cadastro, login

urlpatterns = [
    path('registro', cadastro, name='cadastro'),
    path('login', login, name='login')
]
    