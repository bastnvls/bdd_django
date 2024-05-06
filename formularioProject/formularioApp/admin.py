from django.contrib import admin
from formularioApp.models import Formulario_paciente



# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    list_display = ['nombre_propietario','apellido_propietario','email','direccion','telefono','nombre_paciente','raza','especie','sexo','peso','fecha_nacimiento','color','tipo_pelaje']

admin.site.register(Formulario_paciente, PacientesAdmin)