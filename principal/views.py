from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ListaContactos(request):
    return HttpResponse("Hola mundo")
