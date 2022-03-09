from django import forms
from .models import *


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_razao_social', 'cpf_cnpj', 'rg_ie', 'endereco', 'bairro', 'numero', 'complemento', 'cep',
                  'cidade', 'uf', 'fone', 'celular', 'whats', 'email', 'data_nasc_abertura', 'contato')
