from django.forms import ModelForm
from django import forms
from .models import Task, pais, estado

class TaskForm(ModelForm):

    pais = forms.ModelChoiceField(queryset=pais.objects.all(), empty_label="Seleccione un país")
    estado = forms.ModelChoiceField(queryset=estado.objects.all(), empty_label="Seleccione un estado")

    class  Meta:
        model = Task
        fields = ['title', 'description', 'important', 'pais', 'estado' ]
        
