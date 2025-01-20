from django.db import models

# Create your models here.

# tarefas/models.py

from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, help_text="Título da tarefa")
    concluida = models.BooleanField(default=False, help_text="Indica se a tarefa foi concluída")

    def __str__(self):
        return self.titulo
