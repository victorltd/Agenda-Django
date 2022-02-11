from urllib import response
from django.shortcuts import render
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    usuario=request.user
    evento= Evento.objects.filter(usuario=usuario)
    #evento= Evento.objects.all() #pra mostrar todos os eventos
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
