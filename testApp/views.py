from django.shortcuts import render
from django.utils import timezone
from .models import Model1
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import Model1Form, ArticuloForm
from django.shortcuts import redirect


# RestFramework
from django.http import JsonResponse, FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ModelSerializer


def edit_modelo(request, pk):
    model = get_object_or_404(Model1, pk=pk)
    if request.method == "POST":
        form = Model1Form(request.POST, instance=model)
        if form.is_valid():
            model = form.save(commit=False)
            model.autor = request.user
            model.fechaPubli = timezone.now()
            model.save()
            return redirect('detalle_modelo', pk=model.pk)
    else:
        form = Model1Form(instance=model)
    return render(request, 'testApp/edit_modelo.html', {'form': form})


def new_model(request):
    if request.method == "POST":
        form = Model1Form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.autor = request.user
            model.fechaPubli = timezone.now()
            model.save()
            return redirect('detalle_modelo', pk=model.pk)
    else:
        form = Model1Form()
    return render(request, 'testApp/edit_modelo.html', {'form': form})


def detalle_modelo(request, pk):
    post = get_object_or_404(Model1, pk=pk)
    return render(request, 'testApp/detalle_modelo.html', {'post': post})


def post_list(request):
    # usuarios = User.objects.all()
    modelos = Model1.objects.all()
    return render(request, 'testApp/post_list.html', {'modelos': modelos})


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


def nuevoArt(request):
    if request.method == "POST":
        response = FileResponse(open('articulo.txt', 'rb'))
        form = ArticuloForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.save()
            
            return redirect('/articulos/', pk=art.pk)
    else:
        form = ArticuloForm()
    return render(request, 'testApp/editArt.html', {'form': form})
