from django.urls import path
from apps.usuarios.views import cadastro, login, logout

urlpatterns = [
    path('registro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout')
]
    