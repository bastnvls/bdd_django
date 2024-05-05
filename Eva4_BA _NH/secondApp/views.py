from django.shortcuts import render, redirect
from firstApp.models import Producto
from secondApp.forms import FormProductos
from django.contrib import messages
from django.contrib.auth.models import Group
from rest_framework import viewsets
from firstApp.serializer import ProductoSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
@login_required
class ProductoViewSets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoProductos(request):
    productos = Producto.objects.all()
    data = {'productos' : productos}
    return render(request, 'empresas.html', data)

def agregarProducto(request):
    form = FormProductos()
    if request.method == 'POST':
        form = FormProductos(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"¡El producto se Agrego correctamente!")
            return index(request)
        data = {'form' : form}
    data = {'form' : form}
    return render(request, 'agregarEmpresa.html', data)


def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    messages.success(request, "¡El producto fue Eliminado correctamente!")
    producto.delete()
    return redirect('/empresas')

def actualizarProducto(request, id):
    producto = Producto.objects.get(id=id)
    form = FormProductos(instance=producto) 
    if request.method == 'POST':
        form = FormProductos(request.POST, instance=producto)  
        if form.is_valid():
            form.save()
            messages.success(request,"¡El producto se Modifico correctamente!")
            return index(request)
        data = {'form' : form} 
    data = {'form': form}
    
    return render(request, 'agregarEmpresa.html', data)
