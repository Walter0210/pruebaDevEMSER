from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('api/', views.TestView.as_view(), name = 'test'),
    path('post/<int:pk>/', views.detalle_modelo, name='detalle_modelo'),

]