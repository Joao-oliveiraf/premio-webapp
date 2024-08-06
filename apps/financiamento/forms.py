from django import forms
from django.utils import timezone

class StepOneFinanciamento(forms.Form):
    choices_pessoa_fisica_juridica = [
        ('cpf', 'Pessoa Física'),
        ('cnpj', 'Pessoa Jurídica')
    ]
    ano_atual = int(str(timezone.now())[0:4])
    tipo_pessoa = forms.ChoiceField(
        choices=choices_pessoa_fisica_juridica,
        label='',
        widget=forms.RadioSelect(attrs={
                'class':'wizard_forms_row'
            }
        )
    )
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
class StepTwoFinanciamento(forms.Form):
    pass
class StepThreeFinanciamento(forms.Form):
    pass