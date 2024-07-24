from django import forms
from django.contrib.auth.models import User



class CadastroForm(forms.Form):
    nome_de_cadastro = forms.CharField(
        label='Nome de usuário',
        max_length=100,
        strip=True,
        required=True,
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput()
    )
    senha_1 = forms.CharField(
        label='Insira sua senha',
        required=True,
        widget=forms.PasswordInput(),
        max_length=70,
    )
    senha_2 = forms.CharField(
        label='Insira sua senha',
        required=True,
        widget=forms.PasswordInput(),
        max_length=70,
    )
    def clean_nome_de_cadastro(self):
        nome = self.cleaned_data.get('nome_de_cadastro')
        nome = nome.strip()

        if " " in nome:
            raise forms.ValidationError('Nome de usuário não pode conter espaços!')
        elif User.objects.filter(username=nome).exists():
            raise forms.ValidationError('Nome de usuário já está em uso!')
        else:
            return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        
        if senha_1 != senha_2:
            raise forms.ValidationError('Senhas não conferem!')
        else:
            return senha_2
class LoginForm(forms.Form):
    nome_de_usuario = forms.CharField(
        label='Nome de usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Nome de usuário',
                'style':'margin: 10px;'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Senha',
                'style':'margin: 10px;'
            }
        )
    )
    def clean_nome_de_usuario(self):
        nome = self.cleaned_data.get('nome_de_usuario')

        if not User.objects.filter(username=nome).exists():
            raise forms.ValidationError('Nome de usuário incorreto')
        else:
            return nome
