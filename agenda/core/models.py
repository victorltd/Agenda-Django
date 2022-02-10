from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento(models.Model):
    titulo=models.CharField(max_length=100) #campo tem ate 100 caracteres
    descricao=models.TextField(blank=True, null=True) #campo pode ser em branco e nulo
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao=models.DateTimeField(auto_now=True) #esse campo e criado automaticamente, ja preenche no caso
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    #coloco essa parte para aparecer o nome do evento como titulo, e nao object
    def __str__(self):
        return self.titulo

