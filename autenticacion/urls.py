from django.urls import path
from . import views

urlpatterns=[
    path('Autenticacion/', views.RegistoUsuario.as_view(), name='autenticacion'),
]