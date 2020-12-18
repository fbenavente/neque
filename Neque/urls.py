import os
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from nequeweb.admin import admin_talleres, admin_nequeweb

ROOT_PATH = os.path.dirname(__file__)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Neque.views.home', name='home'),
    # url(r'^Neque/', include('Neque.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': ROOT_PATH+'/site_media/', 'show_indexes': True}),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin_nequeweb.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^talleres/', include(admin_talleres.urls)),
    url(r'^$', 'nequeweb.views.index_fullscreen'),
    url(r'^nequeweb/', include('nequeweb.urls')),
    url(r'^juego/', include('juego.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^pucon$', 'nequeweb.views.pucon'),
    url(r'^camilo$', 'nequeweb.views.camilo'),
    url(r'^cunco$', 'nequeweb.views.cunco'),
    url(r'^holzapfel$', 'nequeweb.views.holzapfel'),
    url(r'^liquen$', 'nequeweb.views.liquen'),
)
