from django.contrib import admin
from django.contrib.auth.models import *
from django.contrib.sites.models import Site
from nequeweb.models import *
from juego.models import *
from django.forms import SelectMultiple

class ImagenObraInline(admin.TabularInline):
    model = ImagenObra

class VideoObraInline(admin.TabularInline):
    model = VideoObra

class ObraAdmin(admin.ModelAdmin):
    inlines = [
        ImagenObraInline,
        VideoObraInline,
        ]

class ImagenTallerInline(admin.TabularInline):
    model = ImagenTaller

class VideoTallerInline(admin.TabularInline):
    model = VideoTaller

class TallerAdmin(admin.ModelAdmin):
    inlines = [
        ImagenTallerInline,
        VideoTallerInline,
        ]

admin.site.register(Obra, ObraAdmin)
admin.site.register(Taller, TallerAdmin)
admin.site.register(Noticia)
admin.site.register(Integrante)
admin.site.register(Contenido)

admin.site.register(ImagenObra)
admin.site.register(VideoObra)
admin.site.register(ImagenTaller)
admin.site.register(VideoTaller)

admin.site.register(Jugador)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Ranking)


