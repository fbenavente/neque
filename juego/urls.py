from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       (r'^$', 'juego.views.index_juego'),
                       (r'^inscribir_jugador/(?P<nombre>.+)/$', 'juego.views.inscribir_jugador'),
                       (r'^generar_pregunta/(?P<id_jugador>.+)/$', 'juego.views.generar_pregunta'),
                       (r'^evaluar_respuesta/(?P<id_pregunta>.+)/(?P<id_jugador>.+)/(?P<respuesta>.+)/$', 'juego.views.evaluar_respuesta'),

)

