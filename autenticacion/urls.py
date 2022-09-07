from django.urls import path
from . import views

urlpatterns=[
    path('Autenticacion/', views.Autenticacion, name='autenticacion'),
]