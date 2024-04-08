from django import forms
from .models import Filmes, Generos

class Filmes_Form(forms.ModelForm):
    class Meta:
        model = Filmes
        fields = "__all__"

class Generos_Form(forms.ModelForm):
    class Meta:
        model = Generos
        fields = "__all__"