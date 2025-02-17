from django import forms
from .models import Banco, Movimentacao

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['nome', 'numero_conta', 'nome_gerente', 'contato_gerente']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_conta': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_gerente': forms.TextInput(attrs={'class': 'form-control'}),
            'contato_gerente': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MovimentacaoForm(forms.ModelForm):
    tipo = forms.ChoiceField(
        choices=[('C', 'Crédito'), ('D', 'Débito')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True
    )

    class Meta:
        model = Movimentacao
        fields = ['data', 'documento', 'descricao', 'tipo', 'valor']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
