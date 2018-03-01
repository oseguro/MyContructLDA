from django import forms
from .models import *

class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name','value','material','location','image','likes']



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']


class TipoImovelForm(forms.ModelForm):
    class Meta:
        model = TipoImovel
        fields = ['imovel']


class EstiloForm(forms.ModelForm):
    class Meta:
        model = Estilo
        fields = ['estilo']


class ProjetosForm(forms.ModelForm):
    class Meta:
        model = Projetos
        fields = ['data_registo','titulo','imagem', 'distrito','descricao','divisao','estilo','likes','slug']



class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())