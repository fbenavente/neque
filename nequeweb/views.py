# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import force_unicode, smart_unicode
from django.utils.datastructures import SortedDict
from nequeweb.models import *

def index(request):
    return render_to_response('nequeweb/index.html')


def index_fullscreen(request):
    integrantes = Integrante.objects.all().order_by("-nombre")
    obras = Obra.objects.all().order_by("orden")
    noticias = Noticia.objects.all().order_by("-fecha")[:3]
    talleres = Taller.objects.all().order_by("orden")
    return render_to_response('nequeweb/index-fullscreen.html',{'integrantes':integrantes,
                                                                'obras':obras,
                                                                'noticias':noticias,
                                                                'talleres':talleres})


def modulo_carousel(request,id_obra):
    obra = Obra.objects.get(pk=id_obra)
    return render_to_response('nequeweb/modulo_carousel.html',{'obra':obra})


def modulo_imagen(request,id_obra):
    obra = Obra.objects.get(pk=id_obra)
    return render_to_response('nequeweb/modulo_imagen.html',{'obra':obra})


def modulo_video(request,id_obra):
    obra = Obra.objects.get(pk=id_obra)
    return render_to_response('nequeweb/modulo_video.html',{'obra':obra})


def modulo_noticia(request, id_noticia):
    noticia = Noticia.objects.get(pk=id_noticia)
    return render_to_response('nequeweb/modulo_noticia.html',{'noticia':noticia})

def pucon(request):
    return render_to_response('nequeweb/pucon.html')

def camilo(request):
    return render_to_response('nequeweb/camilo.html')

def holzapfel(request):
    return render_to_response('nequeweb/holzapfel.html')

def cunco(request):
    return render_to_response('nequeweb/cunco.html')

def liquen(request):
    return render_to_response('nequeweb/liquen.html')
