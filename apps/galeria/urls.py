from django.urls import path
from apps.galeria.views import index, novo_veiculo,imagem,add_imagem,buscar,deletar_veiculo, contato, deletar_imagem


urlpatterns = [
    path('', index, name='index'),
    path('novo-veiculo', novo_veiculo, name='novo_veiculo'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('add-imagem/<int:foto_id>', add_imagem, name='add_imagem'),
    path('buscar', buscar, name='buscar'),
    path('deletar_veiculo/<int:foto_id>', deletar_veiculo, name='deletar_veiculo'),
    path('contato', contato, name='contato'),
    path('del-imagem/<int:veiculo_id>', deletar_imagem, name='deletar_imagem'),
]