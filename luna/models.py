from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='título')
    description = models.TextField(blank=True, verbose_name='descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    dateCompleted = models.DateTimeField(null=True, verbose_name='Fecha terminado')
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)#borrar todos los dattos relacionados
    def __str__(self):
        return self.title + ' by ' + self.user.username
  
# Create your models here
