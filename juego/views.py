# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from juego.models import *
from django.utils import simplejson


def index_juego(request):

    return render_to_response('juego/index_juego.html')


def inscribir_jugador(request, nombre):
    try:
        jugador = Jugador(nombre=nombre)
        jugador.save()
        respuesta = jugador.pk
    except Exception, e:
        respuesta = "error"

    return HttpResponse(respuesta)


def obtener_puntaje(id_jugador):
    respuestas = Respuesta.objects.filter(jugador__pk=id_jugador)
    puntaje = 0
    for respuesta in respuestas:
        if respuesta.alternativa == respuesta.pregunta.correcta:
            puntaje +=10

    return puntaje


def generar_pregunta(request, id_jugador):
    jugador = Jugador.objects.get(pk=id_jugador)
    universo_preguntas = Pregunta.objects.all()
    totalPreguntas = len(universo_preguntas)
    preguntas_usadas = Pregunta.objects.filter(respuesta__jugador=jugador).distinct()
    puntaje = 0
    ranking = ""

    if len(preguntas_usadas) > 0:
        preguntas = Pregunta.objects.exclude(pk__in=preguntas_usadas).order_by("?")
    else:
        preguntas = Pregunta.objects.all().order_by("?")
    if len(preguntas) > 0:
        nueva_pregunta = preguntas[0]
        id_pregunta = preguntas[0].pk
    else:
        nueva_pregunta = "no"
        puntaje = obtener_puntaje(id_jugador)
        ingresarRanking = Ranking(jugador=jugador,puntaje=puntaje)
        ingresarRanking.save()
        ranking = Ranking.objects.all().order_by("-puntaje")[:40]

    numero_pregunta = len(preguntas_usadas) + 1
    return render_to_response('juego/generar_pregunta.html',{'pregunta':nueva_pregunta,
                                                             'numero_pregunta':numero_pregunta,
                                                             'totalPreguntas':totalPreguntas,
                                                             'jugador':jugador,
                                                             'ranking':ranking,
                                                             'puntaje':puntaje})


def evaluar_respuesta(request, id_pregunta, id_jugador, respuesta):
    jugador = Jugador.objects.get(pk=id_jugador)
    pregunta = Pregunta.objects.get(pk=id_pregunta)
    nueva_respuesta = Respuesta(jugador=jugador, pregunta=pregunta, alternativa=respuesta)
    nueva_respuesta.save()
    respuestas = Respuesta.objects.filter(jugador=jugador)
    correctas = 0
    falsas = 0
    for respuesta in respuestas:
        if respuesta.alternativa == respuesta.pregunta.correcta:
            correctas+=1
        else:
            falsas+=1
    array = simplejson.dumps({"list" : [correctas, falsas]})
    return HttpResponse(array, content_type ="application/json")