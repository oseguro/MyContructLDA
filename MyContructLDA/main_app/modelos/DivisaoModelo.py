from django.db import models


class Divisao(models.Model):
    divisao = models.CharField(max_length=100)

    
    def __str__(self):
        return self.divisao