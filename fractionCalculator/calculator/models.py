from django.db import models

# Create your models here.
class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)  
    num_lista = models.IntegerField()
