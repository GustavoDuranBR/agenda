from django.shortcuts import render, redirect
from core.models import Evento



# Create your views here.
'''# esse modelo retorna apenas o evento do ID selecionado
def lista_eventos(request):
    evento = Evento.objects.get(id=1)
    dados = {'evento':evento}
    return render(request, 'agenda.html', dados)'''

'''def index(request): # um tipo de redirecionar a URL
    return redirect('/agenda/')'''

# esse modelo retorna TODOS os eventos cadastrados
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
