from django.conf.urls import patterns, url
from gmap.views import GmapView, GmapSimpleView

urlpatterns = patterns('',
                       url(r'^$',
                           GmapView.as_view(),
                           name='gmap'),
                       url(r'^simple$',
                           GmapSimpleView.as_view(),
                           name='gmap_simple'),
                       )
