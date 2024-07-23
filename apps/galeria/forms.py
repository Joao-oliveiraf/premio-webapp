from django import forms
from apps.galeria.models import Veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        exclude = ['publicada',]

        labels = {
            'nome': 'Nome do veículo',
            'ano': 'Ano do veículo',
            'cor': 'Cor do veículo',
            'combustivel': 'Combustível',
            'descricao': 'Descrição',
            'data': 'Data de registro',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.TextInput(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'}),
            'combustivel': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }
 