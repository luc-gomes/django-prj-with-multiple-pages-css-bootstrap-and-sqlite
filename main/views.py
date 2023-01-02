from django.shortcuts import render
from django.http import HttpResponse

from main.models import ToDoList
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    #return HttpResponse("<h1> texto texto texto, o indice da pagina é igual à : %s, blz? e o nome na lista = a %s</h1>" % id, ls.name)
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})