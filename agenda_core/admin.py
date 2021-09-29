from django.contrib import admin
from agenda_core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento', 'usuario')
    list_filter = ('titulo', 'data_evento',)


admin.site.register(Evento, EventoAdmin)

