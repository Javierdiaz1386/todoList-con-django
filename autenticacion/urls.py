from django.urls import path
from . import views

urlpatterns=[
    path('Registro/', views.Vregistro.as_view(), name='Registro'),
    path('CerrarSesion/', views.cerrarSesion, name='cerrarsesion'),
    path('InicioSesion/', views.inicioDeSesion, name='inicioSesion'),

]