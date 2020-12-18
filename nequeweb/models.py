# -*- coding: utf-8 -*-
from django.db import models

from tinymce.models import HTMLField
from django.utils.html import mark_safe
from django.utils.encoding import smart_unicode



class Obra(models.Model):
    nombre = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    imagen_principal = models.ImageField(upload_to='images/obras/',null=True, blank=True)
    imagen_video = models.ImageField(upload_to='images/obras/',null=True, blank=True)
    orden = models.IntegerField(null=True, blank=True)
    descripcion = HTMLField(null=True, blank=True)
    resena = models.TextField(null=True, blank=True)
    cuadernillo = models.FileField(upload_to='images/obras/cuadernillos/', null=True, blank=True)
    carpeta = models.FileField(upload_to='images/obras/carpetas/', null=True, blank=True)
    fecha_modificacion = models.DateField("Fecha modificación")

    class Meta:
        ordering = ['orden']

    def breve_resena(self):
        return smart_unicode(self.resena[:100]+"...",encoding='utf-8')

    def __unicode__(self):
        return "%s" % (smart_unicode(self.nombre,encoding='utf-8'))

class ImagenObra(models.Model):
    imagen = models.ImageField(upload_to='images/obras/')
    obra = models.ForeignKey(Obra)
    orden = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['orden']

class VideoObra(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.TextField()
    codigo_corto = models.CharField(max_length=250)
    obra = models.ForeignKey(Obra)
    orden = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['orden']

    def __unicode__(self):
        return "%s" % (smart_unicode(self.nombre,encoding='utf-8'))


class Taller(models.Model):
    nombre = models.CharField(max_length=50)
    imagen_principal = models.ImageField(upload_to='images/talleres/')
    orden = models.IntegerField(null=True, blank=True)
    descripcion = HTMLField(null=True, blank=True)
    descripcion_corta = models.TextField(null=True, blank=True)
    carpeta = models.FileField(upload_to='images/talleres/carpetas/',null=True, blank=True)
    fecha_modificacion = models.DateField("Fecha modificación")

    class Meta:
        ordering = ['nombre']

    def breve_descripcion(self):
        return smart_unicode(self.descripcion_corta[:150]+"...",encoding='utf-8')

    def __unicode__(self):
        return "%s" % (smart_unicode(self.nombre,encoding='utf-8'))


class ImagenTaller(models.Model):
    imagen = models.ImageField(upload_to='images/talleres/')
    taller = models.ForeignKey(Taller)
    orden = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['orden']

class VideoTaller(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.TextField()
    codigo_corto = models.CharField(max_length=250)
    obra = models.ForeignKey(Taller)
    orden = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['orden']

    def __unicode__(self):
        return "%s" % (smart_unicode(self.nombre,encoding='utf-8'))

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    descripcion = HTMLField(null=True, blank=True)
    descripcion_corta = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='images/noticias/',null=True, blank=True)
    orden = models.IntegerField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['fecha']

    def breve_descripcion(self):
        return smart_unicode(self.descripcion_corta[:150]+"...",encoding='utf-8')

    def __unicode__(self):
        return "%s" % (smart_unicode(self.titulo,encoding='utf-8'))


class Integrante(models.Model):
    nombre = models.CharField(max_length=50)
    curriculum = HTMLField(null=True, blank=True)
    imagen = models.ImageField(upload_to='images/integrantes/',null=True, blank=True)
    rol = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254, null=True, blank=True)

    def __unicode__(self):
        return "%s" % (smart_unicode(self.nombre,encoding='utf-8'))


class Contenido(models.Model):
    titulo = models.CharField(max_length=50)
    texto = HTMLField(null=True, blank=True)
    imagen = models.ImageField(upload_to='images/contenidos/',null=True, blank=True)

    def __unicode__(self):
        return "%s" % (smart_unicode(self.titulo,encoding='utf-8'))
