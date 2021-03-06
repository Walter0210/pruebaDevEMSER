from rest_framework import serializers
from .models import Model1
from django import forms

# class PostModel(form.ModelForm):
#     class Meta:
#         model = Model1
#         fields = {
#             'titulo', 'texto'
#         }

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model1
        fields = (
            'autor', 'titulo', 'text', 'fechaCreacion', 'fechaPubli'
        )