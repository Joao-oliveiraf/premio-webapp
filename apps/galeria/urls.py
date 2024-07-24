from django.urls import path
from apps.galeria.views import index, novo_veiculo, imagem


urlpatterns = [
    path('', index, name='index'),
    path('novo-veiculo', novo_veiculo, name='novo_veiculo'),
    path('imagem/<int:foto_id>', imagem, name='imagem')
]