from django import forms
from .models import Filmes

class Filmes_Form(forms.ModelForm):
    class Meta:
        model = Filmes
        fields = "__all__"