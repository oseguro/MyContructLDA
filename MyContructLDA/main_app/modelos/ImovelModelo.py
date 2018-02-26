from django.db import models

class TipoImovel(models.Model):
    imovel = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.imovel