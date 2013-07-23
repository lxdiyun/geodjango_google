from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.conf import settings


dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'geodjango.views.home', name='home'),
                       # url(r'^geodjango/', include('geodjango.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^gmap/', include('gmap.urls')),
                       url(dajaxice_config.dajaxice_url,
                           include('dajaxice.urls')),
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT,
                              'show_indexes': True}),
                            )
