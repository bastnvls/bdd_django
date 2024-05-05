from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth import login, logout, authenticate
from .models import Producto
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import tarjeta
import random
import datetime
# Create your views here.
def home(request):
    return render(request, 'home.html')
@login_required
def tarjeta_form(request):
    form = tarjeta()
    if request.method == 'POST':
        form = tarjeta(request.POST)
        if form.is_valid():
            messages.success(request, "COMPRA REALIZADA")
            return redirect('detalles')  # Redirige después de definir el mensaje
    else:
        form = tarjeta()

    return render(request, 'tarjeta_form.html', {'formulario_tarjeta': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('list_products')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Verificar si el usuario pertenece al grupo 'Administradores'
            administradores_group = Group.objects.get(name='Administradores')

            if administradores_group in user.groups.all():
                # El usuario es un administrador, redirigir a la página de administradores
                return redirect('index')
            else:
                # El usuario no es un administrador, redirigir a la página principal
                return redirect('list_products')
        
    return render(request, 'login.html')

def list_products(request):
    products = Producto.objects.all()
    messages_success = messages.get_messages(request)
    data = {
        'products': products
    }
    if messages_success:
        data['messages_success'] = messages_success
    return render(request, 'home.html', data)

    

def check_admin_and_redirect(request):
    if request.user.groups.filter(name='Administradores').exists():
        return redirect('index')
    else:
        messages.success(request,"¡Esta opcion es solo para Admnistradores!")
        return redirect('list_products')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Sesion Cerrada")
    return redirect('list_products')

@login_required
def add_to_cart(request, product_id):
    cart_key = f'cart_{request.user.id}'  # Clave única del carrito para cada usuario
    cart = request.session.get(cart_key, {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session[cart_key] = cart
    return redirect('list_products')

@login_required
def view_cart(request):
    cart_key = f'cart_{request.user.id}'
    cart = request.session.get(cart_key, {})
    products_in_cart = {}
    total_precio = 0  
    for product_id, quantity in cart.items():
        product = get_object_or_404(Producto, id=product_id)
        products_in_cart[product] = quantity
        total_precio += product.precio * quantity

    if total_precio > 0:
        total_precio = total_precio + (total_precio * 0.19)
        total_precio = round(total_precio, 2)

    data = {
        'cart': products_in_cart, 
        'total_precio': total_precio
    }
    return render(request, 'view_cart.html', data)

@login_required
def detalles(request):
    cart_key = f'cart_{request.user.id}'
    cart = request.session.get(cart_key, {})
    products_in_cart = {}
    total_precio = 0  
    for product_id, quantity in cart.items():
        product = get_object_or_404(Producto, id=product_id)
        products_in_cart[product] = quantity
        total_precio += product.precio * quantity  
        

    if total_precio > 0:
        monto_neto = total_precio
        iva = total_precio * 0.19
        total_precio = total_precio + iva
        total_precio = round(total_precio, 2)
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        codigo = ''.join(random.choice('0123456789') for _ in range(6))

        data = {
            'cart': products_in_cart, 
            'total_precio': total_precio,
            'fecha_actual':fecha,
            'codigo':  codigo,
            'iva':iva,
            'monto_neto':monto_neto,
            }
        messages_success = messages.get_messages(request)
        if messages_success:
            data['messages_success'] = messages_success
            clear_cart(request)
    return render(request, 'detalles.html',data )

@login_required
def clear_cart(request):
    cart_key = f'cart_{request.user.id}'
    if cart_key in request.session:
        del request.session[cart_key]
    return redirect('view_cart')