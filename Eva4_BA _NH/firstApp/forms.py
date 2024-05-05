from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label='Correo Electrónico', error_messages={
        'invalid': 'Por favor, ingresa un correo valido. Ejemplo: bastian@gmail.com'
    })
    username = forms.CharField(min_length=3,max_length=50)


    def clean_first_name(self):

        inputFirstName = self.cleaned_data['first_name']
        if any(char.isdigit() for char in inputFirstName):
            raise ValidationError("No intentes ingresar datos falsos. Ingresa solo letras.")
        return inputFirstName
    
    def clean_last_name(self):

        inputLastName = self.cleaned_data['last_name']
        if any(char.isdigit() for char in inputLastName):
            raise ValidationError("No intentes ingresar datos falsos. Ingresa solo letras.")
        return inputLastName
    
    class Meta:
        model = User
        fields = [ 'username', 'password1', 'password2', 'email', 'first_name', 'last_name' ]
        labels = {
            'username': 'Nombre de Usuario'
        }

class tarjeta(forms.Form):
    nombreCompleto = forms.CharField(label='Nombre Completo',min_length=10,max_length=100)
    CVV = forms.CharField(label='CVV',max_length=3)
    numeroTarjeta = forms.CharField(label='Numero de Tarjeta',max_length=16)
    fechaExp = forms.CharField(label='Fecha Expiracion', max_length=5, help_text='Formato: MM/YY')

    def clean_nombreCompleto(self):
        inputnombreCompleto = self.cleaned_data['nombreCompleto']
        if any(char.isdigit() for char in inputnombreCompleto):
            raise ValidationError("No intentes ingresar datos falsos. Ingresa solo letras.")
        return inputnombreCompleto

    def clean_CVV(self):
        inputcleanCVV = self.cleaned_data['CVV']
        if  len(inputcleanCVV) != 3:
            raise ValidationError("El CVV solo tiene 3 numeros.")
        elif not inputcleanCVV.isdigit():
            raise ValidationError("No intentes ingresar datos falsos. Ingresa solo números.")
        return inputcleanCVV

    def clean_numeroTarjeta(self):
        inputclean_numeroTarjeta = self.cleaned_data['numeroTarjeta']
        if  len(inputclean_numeroTarjeta) != 16:
            raise ValidationError("El numero de tarjeta solo debe tener 16 dígitos. Asegurate de poner los numeros sin espacio.")
        elif not inputclean_numeroTarjeta.isdigit():
            raise ValidationError("No intentes ingresar datos falsos. Ingresa solo números.")
        return inputclean_numeroTarjeta

    def clean_fechaExp(self):
        input_fechaExp = self.cleaned_data['fechaExp']
        if len(input_fechaExp) != 5 or not input_fechaExp[0:2].isdigit() or not input_fechaExp[3:].isdigit() or input_fechaExp[2] != '/':
            raise forms.ValidationError("Por favor, ingresa una fecha válida. El formato debe ser MM/YY.")

        return input_fechaExp
