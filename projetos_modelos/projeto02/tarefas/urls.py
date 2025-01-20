from django.urls import path
from . import views  # Importa as views do app

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),  # Define a rota para a página inicial
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),  # Define a rota para adicionar tarefas
    path('excluir/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),  # Define a rota para excluir tarefas
]