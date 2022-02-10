from django.contrib import admin
from core.models import Evento

# Register your models here.

#para aparecer la na lista, esses campos ai embaixo e nao somente o titulo
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao', 'usuario')
    list_filter=('titulo',) #para mostrar do lado um direito da tela um campo para que eu possa filtrar 


admin.site.register(Evento, EventoAdmin)
