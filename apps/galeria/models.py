from django.db import models
from django.utils import timezone

class Veiculo(models.Model):

    nome = models.CharField(max_length=150, null=False, blank=False,)
    ano = models.IntegerField(null=False, blank=False,)
    cor = models.CharField(max_length=100, blank=False, null=False)
    combustivel = models.CharField(max_length=150, blank=False, null=False)
    descricao = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='foto/%Y/%m/%d', blank=True)
    data = models.DateTimeField(default=timezone.now, blank=False)
    publicada = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome.title()
