from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',

        ]
        labels={
            'first_name': 'Primer Nombre:',
            'last_name' : 'Segundo Nombre:',
            'email': 'Correo:',
            'username': 'Usuario',

        }