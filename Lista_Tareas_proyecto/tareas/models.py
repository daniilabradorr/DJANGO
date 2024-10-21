from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#Creamos el diccionario de prioridades para luego poder ponerlas a elegir.
PRIORIDADES=[
    ('A','ALTA'),
    ('M','MEDIA'),
    ('B','BAJA'),
]

#Creamos la clase tarea con título,descripcion,prioridad y si esta completada o no.
class Tarea(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.TextField(blank=True)
    prioridad=models.CharField(max_length=1,choices=PRIORIDADES)
    completada=models.BooleanField(default=False)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE) #Relacionamos la tarea con el usuario.
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_completada = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.titulo

