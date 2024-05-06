from django.db import models


# Create your models here.

class Formulario_paciente(models.Model):
    nombre_propietario = models.CharField(max_length=50)
    apellido_propietario = models.CharField(max_length=50)
    email = models.EmailField()
    direccion= models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    nombre_paciente= models.CharField(max_length=50)
    raza= models.CharField(max_length=50)
    especie= models.CharField(max_length=50)
    sexo= models.CharField(max_length=50)
    peso= models.FloatField()
    fecha_nacimiento = models.DateField()
    color= models.CharField(max_length=50)
    tipo_pelaje= models.CharField(max_length=50)


    

