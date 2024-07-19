from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self) -> str:
        return self.name
