# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True  # Rascunho para ser usado em outras classes, não é migrado


class Cliente(Base):
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    nome_razao_social = models.CharField('Nome/Razão Social', max_length=200, blank=False)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14, blank=False)
    rg_ie = models.CharField('RG/I.E.', max_length=10, blank=False)
    endereco = models.CharField('Endereço', max_length=150, blank=False)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    numero = models.CharField('Nº', max_length=15, blank=True)
    complemento = models.CharField('Complemento', max_length=100, blank=True)
    cep = models.CharField('CEP', max_length=9, blank=False)
    cidade = models.CharField('Cidade', max_length=50, blank=False)
    uf = models.CharField('UF', max_length=2, choices=UF_CHOICES, blank=False)
    fone = models.CharField('Fone', max_length=10, blank=True)
    celular = models.CharField('Celular', blank=False, max_length=15)
    whats = models.BooleanField('Whats?', default=False)
    email = models.EmailField('E-mail', max_length=254, blank=True)
    data_nasc_abertura = models.DateField('data de nascimento/abertura', blank=True)
    contato = models.CharField('Contato', max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nome_razao_social


class Fornecedor(Base):
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    nome_razao_social = models.CharField('Nome/Razão Social', max_length=200, blank=False)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14, blank=False)
    rg_ie = models.CharField('RG/I.E.', max_length=10, blank=False)
    endereco = models.CharField('Endereço', max_length=150, blank=False)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    numero = models.CharField('Nº', max_length=15, blank=True)
    complemento = models.CharField('Complemento', max_length=100, blank=True)
    cep = models.CharField('CEP', max_length=9, blank=False)
    cidade = models.CharField('Cidade', max_length=50, blank=False)
    uf = models.CharField('UF', max_length=2, choices=UF_CHOICES, blank=False)
    fone = models.CharField('Fone', max_length=10, blank=True)
    celular = models.CharField('Celular', blank=False, max_length=15)
    whats = models.BooleanField('Whats?', default=False)
    email = models.EmailField('E-mail', max_length=254, blank=True)
    data_nasc_abertura = models.DateField('data de nascimento/abertura', blank=True)
    contato = models.CharField('Contato', max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
    
    def __str__(self):
        return self.nome_razao_social


class Funcionario(Base):
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    nome = models.CharField('Nome/Razão Social', max_length=200, blank=False)
    cpf = models.CharField('CPF/CNPJ', max_length=14, blank=False)
    rg = models.CharField('RG/I.E.', max_length=10, blank=False)
    endereco = models.CharField('Endereço', max_length=150, blank=False)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    numero = models.CharField('Nº', max_length=15, blank=True)
    complemento = models.CharField('Complemento', max_length=100, blank=True)
    cep = models.CharField('CEP', max_length=9, blank=False)
    cidade = models.CharField('Cidade', max_length=50, blank=False)
    uf = models.CharField('UF', max_length=2, choices=UF_CHOICES, blank=False)
    fone = models.CharField('Fone', max_length=10, blank=True)
    celular = models.CharField('Celular', blank=False, max_length=15)
    whats = models.BooleanField('Whats?', default=False)
    email = models.EmailField('E-mail', max_length=254, blank=True)
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return self.nome
