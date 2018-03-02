from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

def home(request):
    treasures = Treasure.objects.all()
    categorias = Categoria.objects.all()
    estilos = Estilo.objects.all();
    projetos = Projetos.objects.all()
    form = TreasureForm()
    return render(request, 'home.html', {'treasures': treasures,'projetos':projetos, 'categorias': categorias,'estilos': estilos,'form':form})

def detail(request, slug):
    projeto = Projetos.objects.get(slug=slug)
    return render(request, 'detail.html', {'projeto': projeto})

def post_treasure(request):
    form = TreasureForm(request.POST,request.FILES)
    if form.is_valid():
       form.save(commit = True)
       
    return HttpResponseRedirect('/')


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
    treasures = Treasure.objects.filter(user=user)
    print('treasures', treasures)
    return render(request, 'profile.html',{'username': username, 'treasures': treasures})



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
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('/')
                    #return Index(request)
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


#def search(request):
  #  search_val = request.GET.get('search', None)
  #  if (search_val != None):
  #      results = []
   #     treasures = Treasure.objects.filter(name__icontains=search_val)
  #      for treasure in treasures:
           # json = {}
           # json['name'] = treasure.name
           # json['link'] = '/' + str(treasure.id) + '/'
           # results.append(json)
  #      return JsonResponse({'results':results})
 #   else:
  #      return render(request, 'search.html')


def estilos_view(request,slug):
    estilo_proj = Estilo.objects.get(slug=slug)
    projeto = Projetos.objects.filter(estilo = estilo_proj)
    return render(request, 'projetos_estilo.html', {'projetos': projeto})


def categorias_view(request,slug):
    categoria_proj = Categoria.objects.get(slug=slug)
    projeto = Projetos.objects.filter(categoria = categoria_proj)
    return render(request, 'projetos_categorias.html', {'projetos': projeto})