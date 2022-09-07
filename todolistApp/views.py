from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import tareasTable
from .forms import TodoListForm

def inicio(request):
    
    return render(request, 'paginas/index.html' )
@login_required(login_url='/InicioSesion/')
def tareas(request):




    tareas = tareasTable.objects.all()
    
    return render(request, 'tareasPorHacer/index.html', {'tareas': tareas})



def crearTarea(request):
    formulario = TodoListForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('tareas')
    return render(request, 'tareasPorHacer/agregar.html', {'formulario': formulario})



def editarTarea(request, id):
    tarea = tareasTable.objects.get(id=id)
    usuario = request.user
    formulario = TodoListForm(request.POST or None, instance=tarea)
    if str(usuario) == str(tarea.usuario):

        if formulario.is_valid() and request.method == 'POST':
            formulario.save()
            return redirect('tareas')
    else:
        redirect('tareas')
    return render(request, 'tareasPorHacer/editar.html', { 'formulario' : formulario })

def eliminarTareas(request, id):
    tarea = tareasTable.objects.get(id=id)
    usuario= request.user
    if str(usuario) == str(tarea.usuario):
        tarea.delete()
    return redirect('tareas')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def login(request):
    return render(request, 'registration/login.html')
