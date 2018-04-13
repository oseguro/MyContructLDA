from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from .filters import *
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    categorias = Categoria.objects.all()
    estilos = Estilo.objects.all();
    projetos = Projetos.objects.all().order_by('-created_at')[:4]
    #projetos_top = reversed(projetos)
    form = TreasureForm()
    return render(request, 'home.html', {'projetos':projetos, 'categorias': categorias,'estilos': estilos,'form':form})

def detail(request, slug):
    projeto = Projetos.objects.get(slug=slug)
    fotos_projeto = FotosProjeto.objects.filter(projeto = projeto)
    tipo_imovel = TipoImovel.objects.all();
    form = OrcamentosForm(initial={'area':projeto.area,'estilo':projeto.estilo,'categoria':projeto.categoria, 'divisao':projeto.divisao, 'tipo_imovel':tipo_imovel,'cod_postal':1234,'slug':projeto.slug})
    f = FotosProjetoFrom(initial={'projeto':projeto})
    if request.method == 'POST':
        form = OrcamentosForm(request.POST)
        f = FotosProjetoFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit = True)
            send_mail('MyContructLDA', 'O Pedido de orçamento foi submetido. Será contatado o mais breve possivel.', 'osmarseguro@gmail.com', [request.POST['email']])
            send_mail('MyContructLDA', 'Tem um novo pedido de orçamento sobre um projeto já realizado por si: \n'+'Descrição: '+request.POST['descricao']+'\nIdentificador do projeto: '+request.POST['slug']+'\nConsulte o website para mais detalhes.', 'osmarseguro@gmail.com', ['osmarseguro@gmail.com'])
            messages.success(request, 'Pedido submetido!')
            form = OrcamentosForm(initial={'area':projeto.area,'estilo':projeto.estilo,'categoria':projeto.categoria, 'divisao':projeto.divisao, 'tipo_imovel':tipo_imovel,'cod_postal':1234,'slug':projeto.slug})
            return render(request, 'detail.html', {'projeto': projeto, 'fotos': fotos_projeto, 'form':form,'f':f})
        elif f.is_valid():
             f.save(commit = True)
             form = OrcamentosForm(initial={'area':projeto.area,'estilo':projeto.estilo,'categoria':projeto.categoria, 'divisao':projeto.divisao, 'tipo_imovel':tipo_imovel,'cod_postal':1234,'slug':projeto.slug})
             f = FotosProjetoFrom(initial={'projeto':projeto})
             return render(request, 'detail.html', {'projeto': projeto, 'fotos': fotos_projeto, 'form':form, 'f':f})  
    else:
        form = OrcamentosForm(initial={'area':projeto.area,'estilo':projeto.estilo,'categoria':projeto.categoria, 'divisao':projeto.divisao, 'tipo_imovel':tipo_imovel,'cod_postal':1234,'slug':projeto.slug})
        f = FotosProjetoFrom(initial={'projeto':projeto})

    return render(request, 'detail.html', {'projeto': projeto, 'fotos': fotos_projeto, 'form':form,'f':f})

def post_treasure(request):
    form = TreasureForm(request.POST,request.FILES)
    if form.is_valid():
       form.save(commit = True)
       
    return HttpResponseRedirect('/')

def post_orcamento(request):
    if request.method == 'POST':
        form = OrcamentosForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            send_mail('MyContructLDA', 'O Pedido de orçamento foi submetido. Será contatado o mais breve possivel.', 'osmarseguro@gmail.com', [request.POST['email']])
            send_mail('MyContructLDA', 'Tem um novo pedido de orçamento: \n'+'Descrição: '+request.POST['descricao']+'\nConsulte o website para mais detalhes.', 'osmarseguro@gmail.com', ['osmarseguro@gmail.com'])
            messages.success(request, 'Pedido submetido!')
            form = OrcamentosForm()
            return render(request, 'orcamentos.html',{'form':form})
    else:
        form = OrcamentosForm()

    return render(request, 'orcamentos.html', {'form': form})
    



def like_treasure(request):
    projeto_id = request.POST.get('projeto_id', None)
    likes = 0
    if projeto_id:
        projeto = Projetos.objects.get(id=int(projeto_id))
        if projeto is not None:
            likes = projeto.likes + 1
            projeto.likes = likes
            projeto.save()

    return HttpResponse(likes)



def profile(request, username):
    user = User.objects.get(username=username)
    #projetos = Projetos.objects.filter(user=user)
    #print('treasures', treasures)
    return render(request, 'profile.html',{'username': username,})

def profileadmin(request, username):
    user = User.objects.get(username=username)
    #projetos = Projetos.objects.filter(user=user)
    #print('treasures', treasures)
    pedidosList = PedidoOrcamento.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(pedidosList, 10)
    try:
        pedidos = paginator.page(page)
    except PageNotAnInteger:
        pedidos = paginator.page(1)
    except EmptyPage:
        pedidos = paginator.page(paginator.num_pages)
        
    return render(request, 'profileadmin.html',{'username': username,'pedidos': pedidos})


def verpedidos(request):
    pedidosList = PedidoOrcamento.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(pedidosList, 10)
    try:
        pedidos = paginator.page(page)
    except PageNotAnInteger:
        pedidos = paginator.page(1)
    except EmptyPage:
        pedidos = paginator.page(paginator.num_pages)
        
    return render(request, 'verpedidos.html',{'pedidos': pedidos})


def apagarticket(request, id=None):
    object = get_object_or_404(PedidoOrcamento, id=id)
    object.delete()
    return redirect("/verpedidos")



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    #print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                     error = 'A palavra chave é valida, mas a conta foi desativada!'
                     return render(request, 'login.html', {'form':form, 'error': error})
            else:
                # the authentication system was unable to verify the username and password
                error='O nome de utilizador ou palavra chave estão incorretos.'
                return render(request, 'login.html', {'form':form, 'error': error})
    
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Conta criada com sucesso!')
            return render(request, 'registration.html',{'form':f})

    else:
        f = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': f})


def search(request):
    search_val = request.GET.get('search',None)
    projetos = Projetos.objects.all()
    if (search_val != None):
        projetos = Projetos.objects.filter(titulo__icontains=search_val)
        
    return render(request, 'projetos.html', {'projetos': projetos})



def estilos_view(request,slug):
    estilo_proj = Estilo.objects.get(slug=slug)
    projeto = Projetos.objects.filter(estilo = estilo_proj)
    return render(request, 'projetos_estilo.html', {'projetos': projeto})


def categorias_view(request,slug):
    categoria_proj = Categoria.objects.get(slug=slug)
    projeto = Projetos.objects.filter(categoria = categoria_proj)
    return render(request, 'projetos_categorias.html', {'projetos': projeto})


def projetos_bck(request,tags):
    #projetos = Projetos.objects.all()
    #return render(request, 'projetos.html', {'projetos': projetos})
    projetos_list = Projetos.objects.filter(tags__icontains=tags)
    return render(request, 'projetos.html', {'projetos': projetos_list})


def pesquisa(request):
    projetos_list = Projetos.objects.all()
    projetos_filter = ProjetosFilter(request.GET.get('projetos', None), queryset=projetos_list)
    return render(request, 'projetos.html', {'filter': projetos_filter})



def projetos(request):
    projetos_list = Projetos.objects.all()
    projetos_filter = ProjetosFilter(request.GET, queryset=projetos_list)
    return render(request, 'projetos/projetos.html', {'filter': projetos_filter})


def addprojeto(request):
    if request.method == 'POST':
        f = ProjetosForm(request.POST, request.FILES)
        if f.is_valid():
            projeto = f.save(commit = False)
            projeto.likes = 0
            projeto.save()
            return HttpResponseRedirect('/addprojeto')

    else:
        f = ProjetosForm()

    return render(request, 'addprojeto.html', {'form': f})



def addfoto(request):
    if request.method == 'POST':
        f = FotosProjetoFrom(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Foto adicionada!')
            return render(request, 'addfoto.html',{'form':f})

    else:
        f = FotosProjetoFrom()

    return render(request, 'addfoto.html', {'form': f})

