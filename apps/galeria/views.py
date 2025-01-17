from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.galeria.forms import VeiculoForm,ImagemVeiculoForm
from apps.galeria.models import Veiculo, ImagemVeiculo
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

def index(request):
    fotos = Veiculo.objects.filter(publicada=True)
    
    return render(request, 'shared/index.html', {'cards':fotos})

@login_required(login_url='/login')
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
    imagens_query_set = ImagemVeiculo.objects.filter(veiculo_id=foto_id)
    imagens = enumerate(imagens_query_set, start=1)
    tem_imagens = imagens_query_set.exists()
    
    
    return render(request, 'galeria/imagem.html', {
        'fotografia': foto,
        'imagens': imagens,
        'tem_imagens': tem_imagens
    })
    
    
@login_required(login_url='/login')
def add_imagem(request, foto_id):
    foto = Veiculo.objects.get(id=foto_id)
    
    form2 = ImagemVeiculoForm

    if request.method == 'POST':
        
        form2 = ImagemVeiculoForm(request.POST, request.FILES)

        if form2.is_valid():
            form2.save()
            messages.success(request, 'Sucesso')
            return render(request, 'galeria/add_imagem.html', {'fotografia':foto, 'form2':form2})
        
    return render(request, 'galeria/add_imagem.html', {'fotografia':foto, 'form2':form2})

def buscar(request):

    if 'buscar' in request.GET:
        search = request.GET['buscar'].strip()
        if Veiculo.objects.filter(Q(nome__icontains=search)| Q(descricao__icontains=search)):
            search_result = Veiculo.objects.filter(Q(nome__icontains=search)| Q(descricao__icontains=search))
            return render(request, 'shared/buscar.html', {'cards':search_result})
        elif request.GET['buscar'] == ' ':
            messages.info(request, 'Nenhum resultado de sua busca')
            return redirect('index')
        else:
            messages.info(request, 'Nenhum resultado de sua busca')
            return redirect('index')
@login_required(login_url='/login')
def deletar_veiculo(request, foto_id):
    if request.user.is_authenticated:
        imagens_disponiveis = ImagemVeiculo.objects.filter(veiculo_id=foto_id)
        for object in imagens_disponiveis:
            object.delete()
        veiculo = get_object_or_404(Veiculo, id=foto_id)
        veiculo.delete() #Delete confirmation with javascript
        messages.info(request, 'Veiculo excluido com sucesso')
        return redirect('index')
def contato(request):
    return render(request, 'galeria/contato.html')
def deletar_imagem(request, veiculo_id):
    imagens_disponiveis = ImagemVeiculo.objects.filter(veiculo_id=veiculo_id)
    if request.method == 'POST':
        ids_to_delete = request.POST.getlist('fotos')
        if not ids_to_delete:
            messages.info(request, 'Nenhuma imagem deletada!')
            return redirect('index')
        for foto_id in ids_to_delete:
            item_to_delete = get_object_or_404(ImagemVeiculo, id=foto_id)
            item_to_delete.delete()
            messages.success(request, f"{len(ids_to_delete)} foto(s) deletada(s) com sucesso")
        return redirect('index')
    return render(request, 'galeria/del_imagem.html', {'fotografia': imagens_disponiveis})
def editar_veiculo(request, veiculo_id):
    veiculo = Veiculo.objects.get(id=veiculo_id)
    form = VeiculoForm(instance=veiculo)

    if request.method == 'POST':

        form = VeiculoForm(request.POST, request.FILES, instance=veiculo)

        if form.is_valid():
            form.save()
            messages.success(request, 'Veiculo editado com sucesso!')
            return redirect('index')
    return render(request, 'galeria/editar_veiculo.html', {'form':form, 'veiculo_id':veiculo_id})