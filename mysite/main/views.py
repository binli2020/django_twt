from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if ls not in request.user.todolist.all():
        return render(request, "main/view.html", {})

    # item = ls.item_set.get(id=id)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

        
    return render(request, "main/list.html", {"ls":ls})

def home(request):
    return render(request, "main/home.html", {})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
        
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(request, "main/create.html", {"form":form})

def view(request):
    return render(request, "main/view.html", {})