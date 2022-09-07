from django.db import models

class tareasTable(models.Model):
    id = models.AutoField(primary_key=True)
    nombreTarea = models.CharField(max_length=40, verbose_name = 'Nombre de la Tarea')
    fechaIncio = models.DateField(auto_now=True,auto_now_add=False, verbose_name='fechaIncio')
    plazoParaTerminar = models.DateField(auto_now=False,auto_now_add=False, verbose_name='Plazo Para terminar AAAA-MM-DD')
    usuario = models.CharField(max_length=50, null=True, verbose_name='usuario')
    def __str__(self):
        return self.nombreTarea
