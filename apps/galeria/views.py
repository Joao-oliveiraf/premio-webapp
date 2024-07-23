from django.shortcuts import render,redirect

from apps.galeria.forms import VeiculoForm
from django.contrib import messages

def index(request):
    return render(request, 'shared/index.html')

def novo_veiculo(request):
    form = VeiculoForm

    if request.method == 'POST':

        form = VeiculoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo cadastro de Veículo realizado')
            return redirect('index')

    return render(request, 'galeria/novo_veiculo.html', {'form':form})
