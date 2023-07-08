from django.shortcuts import redirect, render
from .models import Marca, Talla, producto
from .forms import ProductoForm
from .carrito import Carrito
from productos.carrito import Carrito
# Create your views here.

def index(request):
    context={}
    return render(request, 'productos/index.html',context)

def productosList(request):
    productos = producto.objects.all()
    context={
        'productos' : productos
    }
    return render(request, 'productos/productosList.html',context)

def productosAdd(request):
    context= {'form': ProductoForm()}
    #verificar peticion Post
    if request.method=='POST':
        #con el request se recuperan los datos del form
        formulario=ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            context={'mensaje':"Producto guardado correctamente"}
    return render(request, 'productos/productosAdd.html', context)

def productosEdit(request, pk):
    # Select * from alumnos where id_prod=pk
    productos=producto.objects.get(id_prod=pk)

    context= {'form': ProductoForm(instance=productos)}
    #verificar peticion Post
    if request.method=='POST':
        #con el request se recuperan los datos del form
        # se filtra por el id del producto a editar
        formulario=ProductoForm(request.POST, files=request.FILES, instance=productos)
        if formulario.is_valid:
            formulario.save()
            context={'mensaje':"Producto se edito correctamente"}
    return render(request, 'productos/productosAdd.html', context)

def productosDel(request,pk):
    productos=producto.objects.get(id_prod=pk)
    productos.delete()
    return redirect(to='productosList')



# tienda y carrito


def tienda(request):
    productos = producto.objects.all()
    return render(request, 'productos/tienda.html', {'productos': productos})

def carrito(request):
    context={}
    return render(request, 'productos/carrito.html',context)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto_obj  = producto.objects.get(id_prod=producto_id)
    carrito.agregar(producto_obj)
    return redirect("tienda")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto_obj  = producto.objects.get(id_prod=producto_id)
    carrito.eliminar(producto_obj)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto_obj  = producto.objects.get(id_prod=producto_id)
    carrito.restar(producto_obj)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")