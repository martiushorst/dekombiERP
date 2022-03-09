from django.urls import path
from cadastros import views

urlpatterns = [
    path('clientes', views.ClientesCreateView.as_view(), name='cadastro-clientes'),
]
