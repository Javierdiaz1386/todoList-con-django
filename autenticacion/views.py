from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, redirect

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm





class Vregistro(View):

    def get(self, request):
        form= UserCreationForm()
        return render(request, 'paginas/registro.html', { 'form': form})


    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario= form.save()
            login(request, usuario)
            return redirect('inicio')

        else:
            for i in form.error_messages:
                messages.error(request, form.error_messages[i])
            return render(request, 'paginas/registro.html', {'form': form})

def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

def inicioDeSesion(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            ususuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            usuario= authenticate(username=ususuario, password=contra)
            if usuario is not  None:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, 'usuario invalido')
        else:
            messages.error(request, 'Usuario incorrecto')
    form = AuthenticationForm()
    return render(request, 'paginas/login.html', {'form': form})

