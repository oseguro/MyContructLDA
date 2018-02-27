from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

def home(request):
    treasures = Treasure.objects.all()
    categorias = Categoria.objects.all()
    form = TreasureForm()
    return render(request, 'home.html', {'treasures': treasures,'categorias': categorias,'form':form})

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})

def post_treasure(request):
    form = TreasureForm(request.POST,request.FILES)
    if form.is_valid():
       form.save(commit = True)
       
    return HttpResponseRedirect('/')


def like_treasure(request):
    treasure_id = request.POST.get('treasure_id', None)
    likes = 0
    if treasure_id:
        treasure = Treasure.objects.get(id=int(treasure_id))
        if treasure is not None:
            likes = treasure.likes + 1
            treasure.likes = likes
            treasure.save()

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