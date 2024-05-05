from django.contrib import admin
from .models import Producto
# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion','ram','procesador','grafica','almacenamiento','unidad_almacenamiento','tipo_almacenamiento','refrigeracion_cpu','unidad_optica','teclado','mouse','sistema_operativo','placa','gabinete','fuente']
