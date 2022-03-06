from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class CadastroClientesView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Clientes"
        greeting['pageview'] = "Cadastros"
        return render(request, 'cadastros/clientes.html', greeting)

