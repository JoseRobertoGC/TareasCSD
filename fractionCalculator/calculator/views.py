from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JugadorSerializer, UsuarioSerializer, PartidaSerializer
from .models import Jugadores, Usuarios, Partidas
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3

# Create your views here.

class Fraccion:
    def __init__(self,num,den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    r_denominador = 0 
    r_numerador = 0

    if denominador1 == denominador2:
        r_denominador = denominador1
        r_numerador = numerador1 + numerador2
    else:
        r_denominador = denominador1 * denominador2
        r_numerador = int(((r_denominador/denominador1)*numerador1) + ((r_denominador/denominador2)*numerador2))

    resultado = Fraccion(r_numerador,r_denominador)
    json_resultado = resultado.toJSON()

    return HttpResponse(json_resultado,content_type = "text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    r_denominador = 0 
    r_numerador = 0

    if denominador1 == denominador2:
        r_denominador = denominador1
        r_numerador = numerador1 - numerador2
    else:
        r_denominador = denominador1 * denominador2
        r_numerador = int(((r_denominador/denominador1)*numerador1) - ((r_denominador/denominador2)*numerador2))

    resultado = Fraccion(r_numerador,r_denominador)
    json_resultado = resultado.toJSON()

    return HttpResponse(json_resultado,content_type = "text/json-comment-filtered")

@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    r_denominador = denominador1 * denominador2
    r_numerador = numerador1 * numerador2

    resultado = Fraccion(r_numerador,r_denominador)
    json_resultado = resultado.toJSON()

    return HttpResponse(json_resultado,content_type = "text/json-comment-filtered")


@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    r_denominador = denominador1 * numerador2
    r_numerador = numerador1 * denominador2

    resultado = Fraccion(r_numerador,r_denominador)
    json_resultado = resultado.toJSON()

    return HttpResponse(json_resultado,content_type = "text/json-comment-filtered")

# def usuarios(request):
#     con = sqlite3.connect("db.sqlite3")
#     cur = con.cursor()
#     res = cur.execute("SELECT * FROM usuarios")
#     resultado = res.fetchall()
#     lista =[]  
#     for registro in resultado:
#         id,grupo,grado,numero = registro
#         diccionario = {"id":id,"grupo":grupo,"grado":grado,"num_lista":numero}
#         lista.append(diccionario)
#     registros =[{"id":1,"grupo":"A","grado":6,"num_lista":4},{"id":2,"grupo":"B","grado":6,"num_lista":2}] 
#     registros = lista
#     return render(request, 'usuarios.html',{'lista_usuarios':registros})

def usuarios(request):
    if request.method == 'GET':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM usuarios")
        resultado = res.fetchall()
        lista =[]  
        for registro in resultado:
            id,grupo,grado,numero = registro
            diccionario = {"id":id,"grupo":grupo,"grado":grado,"num_lista":numero}
            lista.append(diccionario)
        registros =[{"id":1,"grupo":"A","grado":6,"num_lista":4},{"id":2,"grupo":"B","grado":6,"num_lista":2}] 
        registros = lista
        return render(request, 'usuarios.html',{'lista_usuarios':registros})
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = loads(body_unicode)
        grado = body['grado']
        grupo = body['grupo']
        num_lista = body['num_lista']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("INSERT INTO usuarios (grupo,num_lista,grado) VALUES(?,?,?)",(grupo,num_lista,grado))
        con.commit()
        print(str(grado)+grupo+str(num_lista))
        return HttpResponse("OK")
    elif request.method == 'DELETE':
        return(usuarios_d(request))




@csrf_exempt
def usuarios_p(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    grado = body['grado']
    grupo = body['grupo']
    num_lista = body['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO usuarios (grupo,num_lista,grado) VALUES(?,?,?)",(grupo,num_lista,grado))
    con.commit()
    print(str(grado)+grupo+str(num_lista))
    return HttpResponse("OK")

    

@csrf_exempt
def usuarios_d(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    id = body['id']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("DELETE FROM usuarios WHERE id_usuario=?", (str(id)))
    con.commit()
    return HttpResponse('OK, usuario borrado' + str(id))


@csrf_exempt
def valida_usuario(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    usuario = eljson['id_usuario']
    contrasenia = eljson['pass']
    print(usuario+contrasenia)
    #con = sqlite3.connect("db.sqlite3")
    #cur = con.cursor()
    #res = cur.execute("SELECT * FROM usuarios WHERE id_usuario=? AND password=?" , (str(usuario),str(contrasenia)))
    #si el usuario es correcto regresar respuesta existosa 200 ok
    #en caso contrario, regresar estatus false
    return HttpResponse('{"estatus":True}')


class JugadoresViewSet(viewsets.ModelViewSet):
    queryset = Jugadores.objects.all()
    serializer_class = JugadorSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer


class PartidasViewSet(viewsets.ModelViewSet):
    queryset = Partidas.objects.all()
    serializer_class = PartidaSerializer