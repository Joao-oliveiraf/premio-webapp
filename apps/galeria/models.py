from django.db import models
from django.utils import timezone

class Veiculo(models.Model):

    nome = models.CharField(max_length=150, null=False, blank=False,)
    ano = models.IntegerField(null=False, blank=False,)
    cor = models.CharField(max_length=100, blank=False, null=False)
    combustivel = models.CharField(max_length=150, blank=False, null=False)
    descricao = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='foto/%Y/%m/%d', blank=True, max_length=250)
    data = models.DateTimeField(default=timezone.now, blank=False)
    publicada = models.BooleanField(default=True)
    preco = models.FloatField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome.title()
    
    def show_preco(self):
        preco_string = f'{self.preco:,.2f}'.replace(',', '.')
        
        return preco_string
    
class ImagemVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='attachments/%Y/%m', blank=True, max_length=255)