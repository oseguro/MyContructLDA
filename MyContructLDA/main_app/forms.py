from django import forms
from .models import *

class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name','value','material','location','image','likes']



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria','slug']


class TipoImovelForm(forms.ModelForm):
    class Meta:
        model = TipoImovel
        fields = ['imovel']


class EstiloForm(forms.ModelForm):
    class Meta:
        model = Estilo
        fields = ['estilo','slug']


class ProjetosForm(forms.ModelForm):
    class Meta:
        model = Projetos
        fields = ['data_registo','titulo','imagem', 'distrito','descricao','divisao','estilo','likes','slug','categoria']



class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


class OrcamentosForm(forms.ModelForm):
    class Meta:
        model = PedidoOrcamento
        fields = ['cod_postal','categoria','estilo','largura','comprimento','area','descricao','tipo_imovel']


class FotosProjetoFrom(forms.ModelForm):
    class Meta:
        model = FotosProjeto
        fields = ['imagem','projeto']