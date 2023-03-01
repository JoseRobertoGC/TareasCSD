from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps

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



