from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.form import CreateNewList
from main.models import ToDoList
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    #{"save":["save"], "c1":["clicked"]}
    if response.method =="POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id))== "clicked":
                    item.complete=True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    #return HttpResponse("<h1> texto texto texto, o indice da pagina é igual à : %s, blz? e o nome na lista = a %s</h1>" % id, ls.name)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {"name": "test"})


def cadastro(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            n= form.cleaned_data["name"]
            t= ToDoList(name = n)
            t.save()

            return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form })