from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JugadorSerializer, UsuarioSerializer, PartidaSerializer
from .models import Jugadores, Usuarios, Partidas
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3
import requests
import string

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


def barras(request):
    '''
    data = [
          ['Jugador', 'Minutos Jugados'],
          ['Ian', 1000],
          ['Héctor', 1170],
          ['Alan', 660],
          ['Manuel', 1030]
        ]
    '''
    data = []
    data.append(['Jugador', 'Minutos Jugados'])
    resultados = Partidas.objects.all() #select * from reto;
    titulo = 'Videojuego Odyssey'
    titulo_formato = dumps(titulo)
    subtitulo= 'Total de minutos por jugador'
    subtitulo_formato = dumps(subtitulo)
    if len(resultados)>0:
        for registro in resultados:
            nombre = registro.puntaje
            minutos = registro.minutos_jugados
            data.append([nombre,minutos])
        data_formato = dumps(data) #formatear los datos en string para JSON
        elJSON = {'losDatos':data_formato,'titulo':titulo_formato,'subtitulo':subtitulo_formato}
        return render(request,'barras.html',elJSON)
    else:
        return HttpResponse("<h1> No hay registros a mostrar</h1>")
    

def dastabase_consult(request):
    resultados = Partidas.objects.all()
    data = [['Puntaje', 'Minutos jugados']]
    for registro in resultados:
        puntaje = registro.puntaje
        minutos = registro.minutos_jugados
        data.append([puntaje, minutos])
    data_json = dumps({'losDatos': data})
    return HttpResponse(data_json, content_type='application/json')

@csrf_exempt
def consultar_db(request):
    if(request.method == 'POST'):
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        puntaje_min = eljson['puntaje_minimo']
        
        resultados = Partidas.objects.filter(puntaje__gt=puntaje_min)
        data = [['ID_Usuario','Puntaje', 'Minutos jugados','Fecha']]
        for registro in resultados:
            usuario_id = str(registro.id_usuario)
            puntaje = registro.puntaje
            minutos = registro.minutos_jugados
            fecha = str(registro.fecha)
            data.append([usuario_id ,puntaje, minutos, fecha])
        data_json = dumps({'losDatos': data})
        return HttpResponse(data_json, content_type='application/json')
    return HttpResponse("La solicitud no es de tipo POST", status=400)



@csrf_exempt
def grafica_barras(request):
    url = "http://127.0.0.1:8000/consultar_db"
    response = requests.get(url)
    data = loads(response.content)['losDatos']
    titulo = 'Videojuego Odyssey'
    titulo_formato = dumps(titulo)
    subtitulo= 'Total de minutos por jugador'
    subtitulo_formato = dumps(subtitulo)
    elJSON = {'losDatos': data, 'titulo': titulo_formato, 'subtitulo': subtitulo_formato}
    return render(request,'barras.html',elJSON)



@csrf_exempt
def table(request):
    url = "http://127.0.0.1:8000/consultar_db"
    response = requests.get(url)
    data = loads(response.content)['losDatos']
    titulo = 'Videojuego Odyssey'
    titulo_formato = dumps(titulo)
    subtitulo= 'Total de minutos por jugador'
    subtitulo_formato = dumps(subtitulo)
    elJSON = {'losDatos': data, 'titulo': titulo_formato, 'subtitulo': subtitulo_formato}
    return render(request,'tabla.html',elJSON)


@csrf_exempt
def tabla(request):
    url = "http://127.0.0.1:8000/consultar_db"
    header = {
        "Content-Type":"application/json"
    }
    payload = {
        "puntaje_minimo":"500"
    }
    response = requests.post(url, data=dumps(payload), headers=header)
    if response.status_code == 200:
        data = loads(response.content)['losDatos']
        titulo = 'Videojuego Odyssey'
        titulo_formato = dumps(titulo)
        subtitulo= 'Total de minutos por jugador'
        subtitulo_formato = dumps(subtitulo)
        elJSON = {'losDatos': data, 'titulo': titulo_formato, 'subtitulo': subtitulo_formato}
        return render(request,'tabla.html',elJSON)
