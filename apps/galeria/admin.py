from django.contrib import admin

from apps.galeria.models import Veiculo,ImagemVeiculo



class ImagemVeiculoInline(admin.TabularInline):
    model = ImagemVeiculo
    extra = 1



class ListandoVeiculos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cor', 'ano','foto', 'publicada')
    inlines = [ImagemVeiculoInline]


admin.site.register(Veiculo, ListandoVeiculos)

# Register your models here.
