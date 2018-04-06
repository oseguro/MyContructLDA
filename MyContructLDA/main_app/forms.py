from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name','value','material','location','image','likes']



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria','slug']


class DivisaoForm(forms.ModelForm):
    class Meta:
        model = Divisao
        fields = ['divisao']


class TipoImovelForm(forms.ModelForm):
    class Meta:
        model = TipoImovel
        fields = ['imovel']


class EstiloForm(forms.ModelForm):
    class Meta:
        model = Estilo
        fields = ['estilo','slug']


class ProjetosForm(forms.ModelForm):
    divisao = forms.ModelChoiceField(queryset=Divisao.objects.all(), label='Divisão')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoria')
    estilo  = forms.ModelChoiceField(queryset=Estilo.objects.all(), label='Estilo')
    imagem = forms.ImageField()
    class Meta:
        model = Projetos
        fields = ['data_registo','titulo','imagem', 'distrito','descricao','divisao','estilo','likes','slug','categoria','area']



class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de Utilizador', max_length=64)
    password = forms.CharField(label='Palavra chave', widget=forms.PasswordInput())


class OrcamentosForm(forms.ModelForm):
    cod_postal = forms.CharField(label='Código Postal', min_length=4, max_length=100)
    descricao = forms.CharField(label='Descrição', max_length=250, widget=forms.Textarea)
    email = forms.EmailField(label='Email',max_length=250)
    divisao = forms.ModelChoiceField(queryset=Divisao.objects.all(), label='Divisão')
    area = forms.DecimalField(label='Área em m2',max_digits=10, decimal_places=2)
    class Meta:
        model = PedidoOrcamento
        fields = ['cod_postal','tipo_imovel','divisao','categoria','estilo','area','descricao','email']


class FotosProjetoFrom(forms.ModelForm):
    imagem = forms.ImageField()
    class Meta:
        model = FotosProjeto
        fields = ['imagem','projeto','descricao']




class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Nome de Utilizador', min_length=4, max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Palavra Chave', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar palavra chave', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError('O nome de utilizador já existe')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError('O email já existe')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise  ValidationError('Palavra chave não é igual')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user