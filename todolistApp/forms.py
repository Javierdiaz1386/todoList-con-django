
from django import forms
from .models import tareasTable

class TodoListForm(forms.ModelForm):
    class Meta:
        model = tareasTable
        fields = '__all__'