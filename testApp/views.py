from django.shortcuts import render
from django.utils import timezone
from .models import Model1
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ModelSerializer


def post_list(request):
    usuarios = User.objects.all()
    modelos = Model1.objects.all()
    return render(request, 'testApp/post_list.html', {'modelos' : modelos})

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Model1.objects.all()
        serial = ModelSerializer(qs, many=True)
        return Response(serial.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)


# def test_view(request):
#     datos = {
#         'name': 'Walter',
#         'age': 25
#     }
#     return JsonResponse(datos)