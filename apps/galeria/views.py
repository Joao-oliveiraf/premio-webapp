from django.shortcuts import render,redirect,get_object_or_404

from apps.galeria.forms import VeiculoForm
from apps.galeria.models import Veiculo, ImagemVeiculo
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    fotos = Veiculo.objects.filter(publicada=True)
    
    return render(request, 'shared/index.html', {'cards':fotos})


def novo_veiculo(request):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    form = VeiculoForm

    if request.method == 'POST':

        form = VeiculoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Novo cadastro de Veículo realizado')
            return redirect('index')

    return render(request, 'galeria/novo_veiculo.html', {'form':form})

def imagem(request, foto_id):# foto_id
    foto = get_object_or_404(Veiculo, pk=foto_id)
    imagens = ImagemVeiculo.objects.filter(veiculo_id=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia':foto, 'imagens':imagens})