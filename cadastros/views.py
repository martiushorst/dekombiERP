from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy


class ClientesView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Clientes"
        greeting['pageview'] = "Cadastros"
        return render(request, 'cadastros/clientes.html', greeting)


class ClientesCreateView(LoginRequiredMixin, CreateView):
    form_class = ClienteForm
    template_name = "cadastros/clientes.html"
    success_url = reverse_lazy('cadastro-clientes')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['heading'] = "Cliente"
        context['pageview'] = "Cadastros"
        return context
