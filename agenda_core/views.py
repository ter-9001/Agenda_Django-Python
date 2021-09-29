from django.shortcuts import render,  HttpResponse
from agenda_core import models

# Create your views here.
def Exibir_Evento(request, evento):
    try:
        titulo = models.Evento.objects.get(titulo = evento).titulo
        data = models.Evento.objects.get(titulo = evento).data_evento
        return HttpResponse("<p style='color:#00ff00'>Olá, está é a descrição do Evento {} </p> <p> Título é {} </p> <p> Data é {} </p>".format( evento, titulo, data))
    except:
        return HttpResponse("<p style='color:#ff0000'>Olá, o Evento com título {} </p> <p style='color:#ff0000'> Não existe! </p>".format(evento))    