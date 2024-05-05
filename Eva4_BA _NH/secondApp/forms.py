from django import forms
from firstApp.models import Producto
from django.core.exceptions import ValidationError
from django.core import validators

def validar_ram(value):
    if not value.endswith('GB'):
        raise forms.ValidationError('La RAM debe terminar con "GB"')
    
    # Eliminar 'GB' y verificar si lo que queda es un número válido
    numeric_part = value[:-2]
    try:
        numeric_value = int(numeric_part)
    except ValueError:
        raise forms.ValidationError('La RAM debe contener un número antes de "GB"')
    
    # Verificar que el número esté en el rango deseado (entre 1 y 99)
    if not 1 <= numeric_value <= 99:
        raise forms.ValidationError('La cantidad de RAM debe estar entre 1 y 99')
    
def validar_almacenamiento(value):
    if not (isinstance(value, int) and 1 <= value <= 999):
        raise forms.ValidationError('El almacenamiento debe ser como max un numero de 3 digitos')
    
def validar_fuente(value):
    if not (isinstance(value, str) and len(value) <= 5 and value[0] != '0' and value.endswith("w")):
        raise forms.ValidationError('La fuente debe tener de 1 a 5 caracteres y que termine en "w" ademas el primer valor no puede ser 0')
    
def validar_precio(value):
    if value <= 0 :
        raise forms.ValidationError('El precio no puede ser un número negativo ni 0')
    
class FormProductos(forms.ModelForm):

    nombre = forms.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    descripcion = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(255)])
    ram = forms.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50), validar_ram])
    procesador = forms.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    grafica = forms.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    almacenamiento = forms.IntegerField(validators=[validar_almacenamiento])
    TIPO = [('HDD','HDD'),('SSD','SSD'),('SSHD','SSHD'),('M.2','M.2')]
    tipo_almacenamiento = forms.CharField(widget=forms.Select(choices=TIPO))
    INCLUYE = [('No incluye','NO INCLUYE'),('Si incluye','SI INCLUYE')]
    refrigeracion_cpu = forms.CharField(widget=forms.Select(choices=INCLUYE))
    unidad_optica = forms.CharField(widget=forms.Select(choices=INCLUYE))
    teclado = forms.CharField(widget=forms.Select(choices=INCLUYE))
    mouse = forms.CharField(widget=forms.Select(choices=INCLUYE))
    UNIDAD = [('GIGABYTE','GIGABYTE(GB)'),('TERABYTE','TERABYTE(TB)')]
    unidad_almacenamiento= forms.CharField(widget=forms.Select(choices=UNIDAD))
    SISTEMA_OPERATIVO = [('Linux','LINUX'),('Windows','WINDOWS')]
    sistema_operativo = forms.CharField(widget=forms.Select(choices=SISTEMA_OPERATIVO))
    placa = forms.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    gabinete = forms.CharField(validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(50)])
    fuente = forms.CharField(validators=[validar_fuente])
    precio = forms.IntegerField(validators=[validar_precio])
    
    
    class Meta:
        model = Producto
        fields = '__all__'

