from django.shortcuts import render, redirect
from . import forms 

from formularioApp.forms import Formulario_pacienteForm
from formularioApp.models import Formulario_paciente

from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'veterinaria_index.html')



def listadoPaciente(request):
    proyectos = Formulario_paciente.objects.all()
    data = {'proyectos' : proyectos}
    return render(request, 'listadoPaciente.html', data)
    
def agregarPaciente(request):
    form = Formulario_pacienteForm()
    if request.method == 'POST':
        form = Formulario_pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado correctamente")
            return listadoPaciente(request)
        data = {'form' : form}
    data = {'form' : form}
    return render(request, 'agregarPaciente.html', data)

def eliminarPaciente(request, id):
    proyecto = Formulario_paciente.objects.get(id = id)
    proyecto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('/listadoPaciente')

def actualizarPaciente(request, id):
    proyecto = Formulario_paciente.objects.get(id = id)
    form = Formulario_pacienteForm(instance=proyecto)
    if request.method == 'POST':
        form = Formulario_pacienteForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificacion exitosa")
            return listadoPaciente(request)
        data = {'form' : form}
    data = { 'form' : form}
    return render(request, 'agregarPaciente.html', data)