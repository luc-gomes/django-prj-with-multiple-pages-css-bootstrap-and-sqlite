from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response, id):
    return HttpResponse("<h1> texto texto texto, o indice da pagina é igual à : %s, blz?</h1>" % id)

def v1(response):
    return HttpResponse("<h1>222 texto</h1>")

