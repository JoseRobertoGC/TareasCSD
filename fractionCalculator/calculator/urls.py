from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'jugador',views.JugadoresViewSet)
router.register(r'usuario',views.UsuariosViewSet)
router.register(r'partida',views.PartidasViewSet)

urlpatterns = [
    path('api',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.index,name='index'),
    path('suma',views.suma, name = 'suma'),
    path('resta',views.resta, name = 'resta'),
    path('multiplicacion',views.multiplicacion, name = 'multiplicacion'),
    path('division', views.division, name = 'division' ),
    path('usuarios',views.usuarios,name="usuarios"),
    path('usuarios_p',views.usuarios_p,name='usuarios_p'),
    path('usuarios_d',views.usuarios_d,name='usuarios_d'),
    path('valida_usuario',views.valida_usuario,name='valida_usuario'),
    path('barras',views.barras,name='barras'),
    path('grafica_barras',views.grafica_barras,name='grafica_barras'),
    path('consultar_db',views.consultar_db,name='consultar_db'), 
    path('tabla',views.tabla,name='tabla'),
    
] 