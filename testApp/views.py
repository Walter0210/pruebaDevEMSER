from django.shortcuts import render
from django.utils import timezone
from .models import Model1
from django.contrib.auth.models import User

def post_list(request):
    usuarios = User.objects.all()
    modelos = Model1.objects.all()
    return render(request, 'testApp/post_list.html', {'modelos' : modelos})