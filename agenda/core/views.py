from urllib import response
from django.shortcuts import redirect, render
from core.models import Evento

# Create your views here.

'''
#para redirecionar o index para a pagina que eu quero
def index(request):
    return redirect('/agenda/')
'''

def lista_eventos(request):
    usuario=request.user
    evento= Evento.objects.filter(usuario=usuario)
    #evento= Evento.objects.all() #pra mostrar todos os eventos
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
