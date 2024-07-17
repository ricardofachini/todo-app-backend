from django.db import models


# Modelo para tarefas do usuário
class Task(models.Model):
    id: int = models.IntegerField()
    title: str = models.CharField(max_length=120)
    description: str = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title