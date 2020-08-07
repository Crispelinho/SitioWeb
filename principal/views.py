from django.shortcuts import render
from django.http import HttpResponse
from principal.models import Contacto
from django.template import loader

# Create your views here.

def ListaContactos(request):
    template = loader.get_template('contactos.html')
    context = {
        'contactos':Contacto.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def index (request):

    return render(request, 'index.html')