from django.shortcuts import render
from .models import *

def index(request):
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')
    endereco = request.POST.get('endereco')
    cliente = Clientes(nome=nome, telefone=telefone, endereco=endereco)
    cliente.save()
    return render(request, 'index.html')

def clientes_cadastrados(request):
    clientes = Clientes.objects.all()
    context = {
        clientes:clientes
    }
    return render(request, 'clientes_cadastrados.html',context)
 