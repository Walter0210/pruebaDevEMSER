from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api/', views.TestView.as_view(), name='test'),
    path('model/<int:pk>/', views.detalle_modelo, name='detalle_modelo'),
    path('model/new/', views.new_model, name='new_model'),
    path('model/<int:pk>/edit/', views.edit_modelo, name='edit_modelo'),

]
