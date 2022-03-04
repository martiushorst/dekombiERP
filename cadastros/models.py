# -*- coding: utf-8 -*-
from django.db import models


class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True #Rascunho para ser usado em outras classes, não é migrado
        

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
    nome_razao_social = models.CharField('Nome/Razão Social', max_length=200)
    celular = models.CharField('Celular', blank=False, max_length=15)
    cpf_cnpj = models.CharField('CPF/CNPJ', blank=False, max_length=14)
    rg_ie = models.CharField('RG/I.E.', blank=False, max_length=10)
    endereco = models.CharField('Endereço', blank=False, max_length=150)
    bairro = models.CharField('Bairro', blank=True, max_length=100)
    numero = models.CharField('Nº', blank=True, max_length=10)
    complemento = models.CharField('Complemento', blank=True, max_length=100)
    cep = models.CharField('CEP', blank=False, max_length=9)
    cidade = models.CharField(blank=False, max_length=50)
    uf = models.CharField('UF', max_length=2, choices=UF_CHOICES, blank=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        #ordering = ('created_at',)

    def __str__(self):
        return self.nome
    
    
class Fornecedor(models.Model):
    nome = models.CharField('Nome', max_length=200)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices=(
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
    )

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        #ordering = ('created_at',)

    def __str__(self):
        return self.nome
    
    
class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=200)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices=(
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
    )

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        #ordering = ('created_at',)

    def __str__(self):
        return self.nome