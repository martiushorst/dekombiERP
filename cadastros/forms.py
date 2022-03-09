from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import *


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        #cep = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '1111111'}))

        fields = '__all__'
        
        #cep = forms.CharField(widget=forms.Textarea({'data-mask': "00000-000"}))
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['cep'].widget.attrs.update({'data-mask': '00000-000'})
            
        """
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field('cep', attrs={'data-mask': "00000-000"}),
            )
        """

        #widgets = {'cep': forms.TextInput(attrs={'data-mask': "00000-000"})}
