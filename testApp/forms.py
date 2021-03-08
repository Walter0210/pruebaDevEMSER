from django import forms
from .models import Model1, Articulo


class Model1Form(forms.ModelForm):

    class Meta:
        model = Model1
        fields = ('titulo', 'text')


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ("nombre", "descripcion")
