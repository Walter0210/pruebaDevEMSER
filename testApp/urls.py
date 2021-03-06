from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name = 'post_list'),
    path('', views.TestView.as_view(), name = 'test')
]