from django.contrib import admin


from apps.galeria.models import Veiculo,ImagemVeiculo


class ImagemVeiculoInline(admin.TabularInline):
    model = ImagemVeiculo
    extra = 1



class ListandoVeiculos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cor', 'ano','foto', 'publicada')
    list_display_links = ('id', 'nome')
    inlines = [ImagemVeiculoInline]

class ImagemVeiculoAdmin(admin.ModelAdmin):
    model = ImagemVeiculo
    list_display = ['veiculo', 'imagem']
    list_filter = ['veiculo',]
    list_per_page = 10
    search_fields = ['veiculo',]


admin.site.register(Veiculo, ListandoVeiculos)
admin.site.register(ImagemVeiculo, ImagemVeiculoAdmin)




# Register your models here.
