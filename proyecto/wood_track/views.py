#views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Producto
from .forms import ProductoForm



@login_required(login_url='/wood_track/login/')
def home(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('login') 
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login') 

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})




def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('index')