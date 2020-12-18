from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       (r'^$', 'nequeweb.views.index_fullscreen'),
                       (r'^modulo_carousel/(?P<id_obra>.+)/$', 'nequeweb.views.modulo_carousel'),
                       (r'^modulo_imagen/(?P<id_obra>.+)/$', 'nequeweb.views.modulo_imagen'),
                       (r'^modulo_video/(?P<id_obra>.+)/$', 'nequeweb.views.modulo_video'),
                       (r'^modulo_noticia/(?P<id_noticia>.+)/$', 'nequeweb.views.modulo_noticia'),

)

