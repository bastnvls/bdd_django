from django.db import models
from firstApp.models import Producto
from django.contrib.auth.models import Group, User
# Create your models here.
#Descomentar este codigo, luego de realizar la primera migración, ya que 
#necesita la tabla auth_user para ser valido y crear el grupo Administradores.
group, created = Group.objects.get_or_create(name='Administradores') 