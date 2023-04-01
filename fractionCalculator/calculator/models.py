from django.db import models

# Create your models here.
class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)  
    num_lista = models.IntegerField()


class Usuarios(models.Model):
    password = models.CharField(max_length=30)


class Partidas(models.Model):
    fecha = models.CharField(max_length=10)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    minutos_jugados = models.IntegerField()
    puntaje =  models.IntegerField()
    


