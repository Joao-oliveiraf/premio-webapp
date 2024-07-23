from django.urls import path
from apps.galeria.views import index, novo_veiculo


urlpatterns = [
    path('', index, name='index'),
    path('novo-veiculo', novo_veiculo, name='novo_veiculo')
]