"""
URL configuration for Eva3Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from firstApp import views as app1
from secondApp import views as app2
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('productos', app2.ProductoViewSets)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.list_products, name='list_products'),
    path('register/', app1.register, name='register'),
    path('login/', app1.user_login, name='login'),
    path('logout/', app1.user_logout, name='user_logout'),
    path('add_to_cart/<int:product_id>/', app1.add_to_cart, name='add_to_cart'),
    path('view_cart/', app1.view_cart, name='view_cart'),
    path('clear_cart/', app1.clear_cart, name='clear_cart'),
    path('detalles/', app1.detalles, name='detalles'),
    path('tarjeta_form/', app1.tarjeta_form, name='tarjeta_form'),
    path('check_admin/', app1.check_admin_and_redirect, name='check_admin'),

    path('index/', app2.index, name='index'),
    path('empresas/', app2.listadoProductos),
    path('agregarEmpresa/', app2.agregarProducto),
    path('eliminarEmpresa/<int:id>', app2.eliminarProducto),
    path('actualizarEmpresa/<int:id>', app2.actualizarProducto),
    path('dfr/', include(router.urls))

    
]
