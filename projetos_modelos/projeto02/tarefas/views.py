from django.shortcuts import render

# Create your views here.

# tarefas/views.py

from django.shortcuts import render, redirect
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()  # Busca todas as tarefas
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo:
            Tarefa.objects.create(titulo=titulo)
        return redirect('lista_tarefas')
    return render(request, 'tarefas/adicionar.html')

def excluir_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    return redirect('lista_tarefas')
