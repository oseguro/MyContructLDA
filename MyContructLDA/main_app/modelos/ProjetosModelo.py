from django.db import models
from .modelos.DivisaoModelo import Divisao
from .modelos.EstiloModelo import Estilo


class Projetos(models.Model):
    data_registo = models.SelectDateWidget()
    distrito = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    divisao = models.ForeignKey(Divisao)
    estilo = models.ForeignKey(Estilo)
    
    
    def __str__(self):
        return self.descricao