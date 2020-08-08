from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from gestioncontactos.models import Contacto
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def ListaContactos(request):
    template = loader.get_template('contactos.html')
    context = {
        'contactos':Contacto.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def index (request):

    return render(request, 'index.html')