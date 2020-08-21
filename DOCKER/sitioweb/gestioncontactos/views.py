from django.shortcuts import render
from .models import Contacto
from .forms import ContactosForm
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect

def Contactos(request):
    template = loader.get_template('contactos.html')
    if request.method == 'POST':

        form = ContactosForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Thanks/')
        else:
            return HttpResponseRedirect('/Error/')
    else:   
            form = ContactosForm()
            context ={'form': form,
                    'contactos':Contacto.objects.all(),   
            }
    return HttpResponse(template.render(context, request))