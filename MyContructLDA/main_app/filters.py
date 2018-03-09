import django_filters
from .models import *


class ProjetosFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains',label='Titulo')
    distrito = django_filters.CharFilter(lookup_expr='icontains',label='Distrito')
    class Meta:
        model = Projetos
        fields = ['titulo', 'distrito','divisao','estilo','categoria',]