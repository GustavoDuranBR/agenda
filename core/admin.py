from django.contrib import admin
from core.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao') # adiciona um display na tabela evento
    list_filter = ('usuario','data_evento',) # adiciona o campo pesquisa na tabela evento

admin.site.register(Evento, EventoAdmin)