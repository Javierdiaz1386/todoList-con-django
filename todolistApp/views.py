

from django.shortcuts import render, redirect


from .models import tareasTable
from .forms import TodoListForm

def inicio(request):
    
    return render(request, 'paginas/index.html' )

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
    formulario = TodoListForm(request.POST or None, instance=tarea)
    
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('tareas')
    return render(request, 'tareasPorHacer/editar.html', { 'formulario' : formulario })

def eliminarTareas(request, id):
    tarea = tareasTable.objects.get(id=id)
    tarea.delete()
    return redirect('tareas')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')
