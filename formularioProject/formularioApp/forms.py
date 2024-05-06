from django import forms
from formularioApp import models
from django.forms import ValidationError

    


class Formulario_pacienteForm(forms.ModelForm):


    SEXO_PACIENTE = [('hembra','HEMBRA'),('macho', 'MACHO')]
    TIPO_ESPECIE = [('perro','PERRO'),('gato','GATO')]
    nombre_propietario = forms.CharField(min_length=3,max_length=50)
    apellido_propietario = forms.CharField(min_length=2,max_length=50)
    email = forms.EmailField(error_messages={
        'invalid': 'Por favor, ingresa un correo valido. Ejemplo: bastian@gmail.com'
    })
    direccion = forms.CharField(min_length=2,max_length=50)
    nombre_paciente = forms.CharField(min_length=2,max_length=50)
    raza= forms.CharField(min_length=2,max_length=50)
    especie = forms.CharField(widget=forms.Select(choices=TIPO_ESPECIE))
    sexo = forms.CharField(widget=forms.Select(choices=SEXO_PACIENTE))
    peso= forms.FloatField(label="Peso (KG):")
    color= forms.CharField(min_length=2,max_length=50)
    tipo_pelaje= forms.CharField(min_length=2,max_length=50)

    fecha_nacimiento = forms.DateField(error_messages={
        'invalid': 'Por favor, ingresa una fecha valida. Ten en cuenta que el formato es dd/mm/aaaa'
    })

    #Verificar que el peso del perro sea real
    def clean_peso(self):
        inputPeso = self.cleaned_data['peso']
        if inputPeso > 85:
            raise ValidationError("El limite del peso es de 85KG.")
        elif inputPeso <= 0:
            raise ValidationError("No se puede ingresar un peso menor a 0KG.")
        return inputPeso
    
    #(Verifica el formato del numero telefonico)
    def clean_telefono(self):
        inputTelefono = self.cleaned_data['telefono']
        if '+56' in inputTelefono:
            raise ValidationError("No debes agregar el '+56' en tu teléfono")
        elif len(inputTelefono) != 9:
            raise ValidationError("El número de teléfono debe tener 9 dígitos")
        elif not inputTelefono.isdigit():
            raise ValidationError("No intentes ingresar datos falsos. Ingresa solo números.")
        return inputTelefono
    
    
    #Valida que no ingrese un año menor al 1993
    def clean_fecha_nacimiento(self):
        inputFechaNacimiento = self.cleaned_data.get('fecha_nacimiento')

        if inputFechaNacimiento.year < 1993:
            raise ValidationError("La fecha de nacimiento debe ser en el año 1993 o después.")

        return inputFechaNacimiento
  
    
    class Meta:
        model = models.Formulario_paciente
        fields = '__all__'

    