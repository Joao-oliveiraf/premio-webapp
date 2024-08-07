from django import forms
from django.utils import timezone
from localflavor.br.forms import BRCPFField, BRCNPJField, BRStateSelect,BRStateChoiceField

class StepOneFinanciamento(forms.Form):
    choices_pessoa_fisica_juridica = [
        ('cpf', 'Pessoa Física'),
        ('cnpj', 'Pessoa Jurídica')
    ]

    tipo_pessoa = forms.ChoiceField(
        choices=choices_pessoa_fisica_juridica,
        label='',
        widget=forms.RadioSelect(attrs={
                'class':'wizard_forms_row'
            }
        )
    )
    ano_atual = int(str(timezone.now())[0:4])
    marca = forms.CharField(
        max_length=100,
        required=True,
        label='Marca do veículo',
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Marca'
            }
        )
    )
    modelo = forms.CharField(
        max_length=150,
        required=True,
        strip=True,
        label='Modelo do veículo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Modelo'
            }
        )
    )
    anofab = forms.IntegerField(
        max_value=ano_atual,
        required=True,
        label='Ano de fabricação',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ano de fabricação',
                'type':'number'
            }
        )
    )
    anomod = forms.IntegerField(
        max_value=ano_atual + 1,
        required=True,
        label='Ano do modelo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ano do modelo',
                'type':'number'
            }
        )
    )
    cor = forms.CharField(
        max_length=50,
        required=True,
        strip=True,
        label='Cor do veículo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cor do veículo',
                'type':'text'
            }
        )
    )
    valor_veiculo = forms.FloatField(
        max_value=None,
        min_value=None,
        required=True,
        label='Valor do veículo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Valor do veículo',
                'type':'number',
                'step': '0.00'
            }
        )
    )
    valor_entrada = forms.FloatField(
        max_value=None,
        min_value=None,
        required=True,
        label='Valor do veículo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Valor do veículo',
                'type':'number',
                'step': '0.00'
            }
        )
    )

    prazo_meses = forms.IntegerField(
        initial=24,
        required=True,
        label='Prazo em Meses',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cor do veículo',
                'type':'number'
            }
        )
    )
class StepTwoFinanciamento_cpf(forms.Form):
    cpf = BRCPFField(
        max_length=16,
        label='CPF',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder':'000.000.000-00',
                'class':'form-control'
            }
        )
    )
    nome_completo = forms.CharField(
        max_length=250,
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'João da Silva',
                'type':'text'
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'exemplo@gmail.com',
                'type':'email'
            }
        )
    )
    data_nascimento = forms.DateTimeField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'type':'date'
            }
        )
    )
    uf = BRStateChoiceField(
        label='UF',
        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo_pessoa')
        cpf = cleaned_data.get('cpf')
        cnpj = cleaned_data.get('cnpj')

        if tipo == 'cpf' and not cpf:
            self.add_error('cpf','Insira um valido')
        return cleaned_data
class StepTwoFinanciamento_cnpj(forms.Form):
    cnpj = BRCNPJField(
        max_length=16,
        label='CNPJ',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder':'XX.XXX.XXX/0001-XX',
                'class':'form-control'
            }
        )
    )
    razao_social = forms.CharField(
        max_length=250,
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'João da Silva',
                'type':'text'
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'exemplo@gmail.com',
                'type':'email'
            }
        )
    )
    data_nascimento = forms.DateTimeField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'type':'date'
            }
        )
    )
    uf = BRStateChoiceField(
        label='UF',
        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo_pessoa')
        cnpj = cleaned_data.get('cnpj')

        if tipo == 'cnpj' and not cnpj:
            self.add_error('cnpj','Insira um valido')
        return cleaned_data



    
class StepThreeFinanciamento(forms.Form):
    pass