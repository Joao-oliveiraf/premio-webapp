from django.shortcuts import render,redirect

from apps.galeria.forms import VeiculoForm
from apps.galeria.models import Veiculo
from django.contrib import messages

def index(request):
    fotos = Veiculo.objects.filter(publicada=True)
    
    return render(request, 'shared/index.html', {'cards':fotos})


def novo_veiculo(request):
    if not request.user.is_authenticated:
        messages.error('Faça login')
        return redirect('index')

    form = VeiculoForm

    if request.method == 'POST':

        form = VeiculoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Novo cadastro de Veículo realizado')
            return redirect('index')

    return render(request, 'galeria/novo_veiculo.html', {'form':form})
