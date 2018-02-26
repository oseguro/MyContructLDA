from django.db import models
from.modelos.ImovelModelo import TipoImovel
from.modelos.CategoriaModelo import Categoria


class PedidoOrcamento(models.Model):
    cod_postal = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria)
    largura =  models.DecimalField(label='Value', max_digits=10, decimal_places=2)
    comprimento = models.DecimalField(label='Value', max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=250)
    tipo_imovel = models.ForeignKey(TipoImovel)
       

    
    def __str__(self):
        return self.descricao