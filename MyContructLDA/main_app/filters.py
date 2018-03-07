import django_filters
from .models import *


class ProjetosFilter(django_filters.FilterSet):
    class Meta:
        model = Projetos
        fields = ['data_registo','titulo', 'distrito','divisao','estilo','categoria',]