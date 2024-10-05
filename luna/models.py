from django.db import models
from django.contrib.auth.models import User

class pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class estado(models.Model):
    nombre = models.CharField(max_length=100)
    pais =models.ForeignKey(pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Task(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='título')
    description = models.TextField(blank=True, verbose_name='descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    dateCompleted = models.DateTimeField(null=True, verbose_name='Fecha terminado')
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)#borrar todos los dattos relacionados
    pais = models.ForeignKey(pais, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(estado, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title + ' by ' + self.user.username
  
# Create your models here
