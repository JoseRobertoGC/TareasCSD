from rest_framework import serializers
from .models import Jugadores, Usuarios, Partidas

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id','grupo','num_lista')


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id','password')


class PartidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partidas
        fields = ('id_usuario','fecha','minutos_jugados','puntaje')

        