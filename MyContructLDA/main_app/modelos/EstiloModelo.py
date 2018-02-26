from django.db import models


class Estilo(models.Model):
    estilo = models.CharField(max_length=100)


    def __str__(self):
        return self.estilo