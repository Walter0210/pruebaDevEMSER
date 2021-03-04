from django.shortcuts import render
from .models import Model1

def post_list(request):
    return render(request, 'testApp/post_list.html', {})