from django.conf.urls import patterns, url
from gmap.views import GmapView

urlpatterns = patterns('',
                       url(r'^$',
                           GmapView.as_view(),
                           name='gmap'),
                       )
