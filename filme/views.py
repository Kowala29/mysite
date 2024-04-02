from django.shortcuts import render, redirect
from .models import Filmes
from .forms import Filmes_Form

def list_filmes(request):
    filmes = Filmes.objects.all()
    template_name = 'list_filmes.html'
    context = {
        'filmes': filmes
    }
    return render(request, template_name, context)

def new_filmes(request):
    print(request.method)
    if request.method == "POST":
        form = Filmes_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("filme:list_filmes")
    else:
        template_name = "new_filmes.html"
        context = {
            "form" : Filmes_Form()
        }
        return render(request, template_name, context)
    

def update_filmes(request, pk):
    filme = Filmes.objects.get(id = pk)
    if request.method == "POST":
        form = Filmes_Form(request.POST, instance = filme)
        if form.is_valid():
            form.save()
            return redirect("filme:list_filmes")
    else:
        template_name = "update_filmes.html"
        context = {
            "form" : Filmes_Form(instance = filme),
            "pk" : pk
        }
        return render(request, template_name, context)

def delete_filmes(request, pk):
    filme = Filmes.objects.get(id = pk)
    filme.delete()
    return redirect("filme:list_filmes")
    