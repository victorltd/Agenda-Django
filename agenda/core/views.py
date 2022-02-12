from urllib import response
from django.shortcuts import redirect, render
from core.models import Evento

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

'''
#para redirecionar o index para a pagina que eu quero
def index(request):
    return redirect('/agenda/')
'''

def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request,username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
            
    return redirect('/')

@login_required(login_url='/login/') #boto esse atributo dentro do login_required, pra me redirecionar quando n tiver autenticado
def lista_eventos(request):

    usuario=request.user
    
    evento= Evento.objects.filter(usuario=usuario)
    #evento= Evento.objects.all() #pra mostrar todos os eventos
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
