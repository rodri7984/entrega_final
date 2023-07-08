from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('productosList', views.productosList, name='productosList'),
    path('home', views.home, name='home'),
]