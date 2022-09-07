from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('MisTareas/', views.tareas, name='tareas'),
    path('AgregarTareas/', views.crearTarea, name='crearTarea'),
    path('EditarTareas/', views.editarTarea, name='editarTarea'),
    path('EliminarTareas/<int:id>', views.eliminarTareas, name='eliminarTarea'),
    path('EditarTareas/<int:id>', views.editarTarea, name='editarTarea'),
    path('Nosotros/', views.nosotros, name='nosotros'),

]
