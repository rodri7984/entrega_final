from django.shortcuts import render
from productos.models import producto, Talla, Marca
from productos.views import productosList
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    context={}
    return render(request, 'administrador/inicio.html',context)
    
@login_required
def productosList(request):
    productos = producto.objects.all()
    context={
        'productos' : productos
    }
    return render(request, 'productos/productosList.html',context)

def home(request):
    context={}
    return render(request, 'administrador/home.html',context)