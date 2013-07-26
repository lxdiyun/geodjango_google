from django.conf.urls import patterns, url
from gmap.views import *

urlpatterns = patterns('',
                       url(r'^gmap$',
                           GmapView.as_view(),
                           name='gmap'),
                       url(r'^simple$',
                           GmapSimpleView.as_view(),
                           name='gmap_simple'),
                       url(r'^gallery$',
                           GalleryView.as_view(),
                           name='gmap_gallery'),
                       url(r'^$',
                           GmapIndexView.as_view(),
                           name='gmap_index'),
                       )
