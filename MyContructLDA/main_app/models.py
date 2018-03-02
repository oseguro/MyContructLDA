from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Divisao(models.Model):
    divisao = models.CharField(max_length=100)


    def __str__(self):
        return self.divisao



class Estilo(models.Model):
    estilo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.estilo)
        super(Estilo,self).save(*args, **kwargs)

    def __str__(self):
        return self.estilo




class Projetos(models.Model):
    data_registo = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    divisao = models.ForeignKey('Divisao', on_delete=models.CASCADE)
    estilo = models.ForeignKey('Estilo', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='treasure_images', default='media/default.png')
    likes = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.titulo)
        super(Projetos,self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo



class TipoImovel(models.Model):
    imovel = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.imovel


class PedidoOrcamento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cod_postal = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    largura =  models.DecimalField(max_digits=10, decimal_places=2)
    comprimento = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=250)
    tipo_imovel = models.ForeignKey('TipoImovel', on_delete=models.CASCADE)

    
    def __str__(self):
        return self.descricao




class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.categoria)
        super(Categoria,self).save(*args, **kwargs)

    def __str__(self):
        return self.categoria

