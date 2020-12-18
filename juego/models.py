# -*- coding: utf-8 -*-
from django.db import models

from tinymce.models import HTMLField
from django.utils.html import mark_safe
from django.utils.encoding import smart_unicode

class Jugador(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    puntaje = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['puntaje']

    def __unicode__(self):
        return "%s" % (smart_unicode(self.nombre,encoding='utf-8'))

SELECCION_ALTERNATIVA = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E')
)

class Pregunta(models.Model):
    texto = HTMLField(null=True, blank=True)
    imagen = models.ImageField(upload_to='images/juego/', null=True, blank=True)
    alternativa_a = HTMLField(null=True, blank=True)
    alternativa_b = HTMLField(null=True, blank=True)
    alternativa_c = HTMLField(null=True, blank=True)
    alternativa_d = HTMLField(null=True, blank=True)
    alternativa_e = HTMLField(null=True, blank=True)
    correcta = models.CharField(max_length=3,choices=SELECCION_ALTERNATIVA, null=True, blank=True)

    def textoHtml(self):

        return mark_safe(self.texto)
    textoHtml.short_description = "Contenido"
    textoHtml.allow_tags= True

    def __unicode__(self):
        return self.textoHtml()

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    jugador = models.ForeignKey(Jugador)
    alternativa = models.CharField(max_length=3,choices=SELECCION_ALTERNATIVA, null=True, blank=True)

    def __unicode__(self):
        return "%s - %s - %s" % (self.alternativa, smart_unicode(self.jugador,encoding='utf-8'), smart_unicode(self.pregunta,encoding='utf-8'))


class Ranking(models.Model):
    jugador = models.ForeignKey(Jugador)
    puntaje = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s = %s" % (smart_unicode(self.jugador,encoding='utf-8'), self.puntaje)