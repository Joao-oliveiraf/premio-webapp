from django.contrib import admin

from apps.galeria.models import Veiculo

class ListandoVeiculos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cor', 'ano','foto', 'publicada')




admin.site.register(Veiculo, ListandoVeiculos)

# Register your models here.
