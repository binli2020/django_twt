from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(name=id)
    item = ls.item_set.get(id=1)

    return HttpResponse("<h1>Main site %s</h1><br></br><p>   %s</p>" % (ls, item))

def v1(response):
    return HttpResponse("<h1>View 1</h1>")