from django.shortcuts import render
from .models import Filmes
from django.db import models
from django.http import HttpResponse

def list_filmes(request):
    filmes = Filmes.objects.all()
    template_name = "list_filmes.html"
    context = {
        "filmes" : filmes
    }
    
    return render(request, template_name, context)

def new_filmes(request):
    new_filme = [Filmes.filme, Filmes.genero, Filmes.quantidade, Filmes.preco]
    
    return HttpResponse("nome %s" % new_filme)

def update_filmes(request):
    pass

def delete_filmes(request):
    pass
