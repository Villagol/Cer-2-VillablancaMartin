from django.shortcuts import render
from .models import Correspondencia,Residencia
from django.db.models import Q
# Create your views here.

def home(request):
    busqueda=(request.GET.get("buscar"))   
    correspondencia=Correspondencia.objects.all()
    
    if busqueda:
        correspondencia=Correspondencia.objects.filter(           
            Q(nroresidencia= busqueda)
        ).distinct()       
    return render(request, 'core/home.html',{"correspondencia":correspondencia})
