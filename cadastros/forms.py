from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        """
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['cep'].widget.attrs.update({'data-mask': '00000-000'})

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                InlineField('email', readonly=True),
            )

        #widgets = {'cep': forms.TextInput(attrs={'data-mask': "00000-000"})}
        """
