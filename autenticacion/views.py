from django.shortcuts import render

def Autenticacion(request):
    return render(request, 'paginas/autenticacion.html')
