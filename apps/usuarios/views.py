from django.shortcuts import render, redirect
from apps.usuarios.forms import CadastroForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você já está logado!')
        return redirect('index')
    form = LoginForm

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form['nome_de_usuario'].value()
            senha = form['senha'].value()
            usuario = auth.authenticate(request,
                                 username=nome,
                                 password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Bem vindo novamente {nome.title()}')
                return redirect('index')
            else:
                messages.error('Senha incorreta!')
                return redirect('login')
        
    return render(request, 'usuarios/login.html', {'form':form})

def cadastro(request):
    if not request.user.is_superuser:
        return redirect('index')
    
    form = CadastroForm
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome = form['nome_de_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_2'].value()

            username_already_exists = User.objects.filter(username=nome).exists()
            if username_already_exists:
                messages.error(request,'Nome de usuário já cadastrado')
                return redirect('registro')
            
            #Criar um novo usuário
            novo_usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
                is_active=1,
                is_staff=0, 
            )
            novo_usuario.save()
            messages.success(request,'Novo usuário cadastrado com sucesso')
            return redirect('index')


    return render(request, 'usuarios/cadastro.html', {'form':form})

def logout(request):
    if not request.user.is_authenticated:
        messages.error('Nenhum usuário logado!')
        
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('index')
    

