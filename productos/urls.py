from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('productosList', views.productosList, name="productosList"),
    path('productosAdd', views.productosAdd, name="productosAdd"),
    path('productosEdit/<str:pk>', views.productosEdit, name="productosEdit"),
    path('productosDel/<str:pk>', views.productosDel, name="productosDel"),
    path('tienda', views.tienda, name='tienda'),
    path('carrito', views.carrito, name='carrito'),
    
]