from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    precio=models.IntegerField(verbose_name="Precio")
    descripcion = models.TextField(verbose_name="Descripción")
    ram = models.CharField(max_length=100, verbose_name="RAM")
    procesador = models.CharField(max_length=100, verbose_name="Procesador")
    grafica = models.CharField(max_length=100, verbose_name="Gráfica")
    almacenamiento = models.CharField(max_length=100, verbose_name="Almacenamiento")
    unidad_almacenamiento = models.CharField(max_length=20)
    tipo_almacenamiento = models.CharField(max_length=20)
    refrigeracion_cpu = models.CharField(max_length=20)
    unidad_optica = models.CharField(max_length=20)
    teclado = models.CharField(max_length=20)
    mouse = models.CharField(max_length=20)
    sistema_operativo = models.CharField(max_length=20)
    placa = models.CharField(max_length=100, verbose_name="Placa Madre")
    gabinete = models.CharField(max_length=100, verbose_name="Gabinete")
    fuente = models.CharField(max_length=100, verbose_name="Fuente de Poder")

    def __str__(self):
        return self.nombre
    

class tarjeta(models.Model):
    nombre_completo=models.CharField(max_length=100, verbose_name="Nombre")
    cvv=models.CharField(max_length=3, verbose_name="CVV")
    numero_tarjeta = models.CharField(max_length=100, verbose_name="Numero Tarjeta")
    fecha_exp = models.DateField(verbose_name="Fecha expiracion")


    def __str__(self):
        return self.nombre