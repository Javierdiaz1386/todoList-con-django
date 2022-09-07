from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .form import RegistroForm
class RegistoUsuario(CreateView):
    model = User
    template_name = 'paginas/autenticacion.html'
    form_class = RegistroForm
    success_url = reverse_lazy('inicio')

