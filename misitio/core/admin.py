from django.contrib import admin
from core.models import Correspondencia
from core.models import Residencia
class Residencias(admin.ModelAdmin):
    list_display = ("numero","dueno","telefono","correo")

class Correspondencias(admin.ModelAdmin):
    list_display=("fecha_recepcion","conserje","remitente","destinatario","estado","nroresidencia")
admin.site.register(Residencia,Residencias)
admin.site.register(Correspondencia,Correspondencias)
