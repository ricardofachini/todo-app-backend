from django.db import models


class Task(models.Model):
    """ 
    Modelo para tarefas do usuário
    """

    title: str = models.CharField(max_length=120)
    description: str = models.CharField(max_length=300)
    is_completed: bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
