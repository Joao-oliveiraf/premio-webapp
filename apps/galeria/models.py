from django.db import models
from django.utils import timezone
import os

def caminho_imagens(instance, filename):
    return os.path.join('veiculos/attachments/', instance.veiculo.nome, filename)

class Veiculo(models.Model):

    nome = models.CharField(max_length=150, null=False, blank=False,)
    ano = models.IntegerField(null=False, blank=False,)
    cor = models.CharField(max_length=100, blank=False, null=False)
    combustivel = models.CharField(max_length=150, blank=False, null=False)
    descricao = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='veiculos/imagens', blank=False, null=False)
    data = models.DateTimeField(auto_now_add=True, blank=False)
    publicada = models.BooleanField(default=True)
    preco = models.FloatField(max_length=20, blank=True, null=True, default=0)

    def __str__(self) -> str:
        return self.nome.title()
    

    def show_preco(self) -> str:
        return f'{self.preco:,.2f}'.replace(',', '.')
    
    def delete(self, *args, **kwargs):
        self.foto.delete(save=False)
        super().delete(*args, **kwargs)


class ImagemVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to=caminho_imagens, blank=False, max_length=255, null=False)

    def delete(self, *args, **kwargs):
        self.imagem.delete(save=False)
        super().delete(*args, **kwargs)