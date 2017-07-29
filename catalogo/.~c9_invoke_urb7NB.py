from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def criar_post(request):
    return HttpResponse("<h1>Home</h1>")
    
def detalhe_do_post(request):
    return HttpResponse("<h1>Home</h1>")

def lista_de_posts(request):
    return HttpResponse("<h1>Home</h1>")
    
def atualizar_post(request):
    return HttpResponse("<h1>Home</h1>")
    
def apagar_post(request):
    return HttpResponse("<h1>Home</h1>")