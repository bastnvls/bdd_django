from rest_framework import serializers
from firstApp.models import Producto
from secondApp.forms import FormProductos
from django.core import validators

def validar_precio(value):
    if value <= 0 :
        raise serializers.ValidationError('El precio no puede ser un número negativo ni 0')
def validar_ram(value):
    if not value.endswith('GB'):
        raise serializers.ValidationError('La RAM debe terminar con "GB"')
    # Se eliina la parte GB para verificar si lo que queda es un numero valido

    numeric_part = value[:-2]
    try:
        numeric_value = int(numeric_part)
    except ValueError:
        raise serializers.ValidationError('La RAM debe contener un número antes de "GB"')
    
    # Se verifica que el numero se encuentre entre los valores 1 y 99 
    if not 1 <= numeric_value <= 99:
        raise serializers.ValidationError('La cantidad de RAM debe estar entre 1 y 99')

#El isinstance comprueba una instancia. En este caso evalua que value sea de tipo entero.
def validar_almacenamiento(value):
    if not (isinstance(value, int) and 1 <= value <= 999):
        raise serializers.ValidationError('El almacenamiento debe ser como máximo un número de 3 dígitos')

def validar_fuente(value):
    if not (isinstance(value, str) and len(value) <= 5 and value[0] != '0' and value.endswith("w")):
        raise serializers.ValidationError('La fuente debe tener de 1 a 5 caracteres y que termine en "w", además el primer valor no puede ser 0')

class ProductoSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    descripcion = serializers.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(255)])
    ram = serializers.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50), validar_ram])
    procesador = serializers.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    grafica = serializers.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    almacenamiento = serializers.IntegerField(validators=[validar_almacenamiento])
    tipo_almacenamiento = serializers.ChoiceField(choices=FormProductos.TIPO)
    refrigeracion_cpu = serializers.ChoiceField(choices=FormProductos.INCLUYE)
    unidad_optica = serializers.ChoiceField(choices=FormProductos.INCLUYE)
    teclado = serializers.ChoiceField(choices=FormProductos.INCLUYE)
    mouse = serializers.ChoiceField(choices=FormProductos.INCLUYE)
    unidad_almacenamiento = serializers.ChoiceField(choices=FormProductos.UNIDAD)
    sistema_operativo = serializers.ChoiceField(choices=FormProductos.SISTEMA_OPERATIVO)
    placa = serializers.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    gabinete = serializers.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    fuente = serializers.CharField(validators=[validar_fuente])
    precio = serializers.IntegerField(validators=[validar_precio])

    class Meta:
        model = Producto
        fields = '__all__'



    