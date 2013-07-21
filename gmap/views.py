from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.gis.maps.google.gmap import GoogleMapException
from util.models import Point


class GmapView(TemplateView):
    template_name = "gmap/gmap.html"

    def get_context_data(self, **kwargs):
        context = super(GmapView, self).get_context_data(**kwargs)
        try:
            key = settings.GOOGLE_MAPS_API_KEY
        except AttributeError:
            raise GoogleMapException('Google Maps API Key not found (try '
                                     'adding GOOGLE_MAPS_API_KEY to your '
                                     'settings).')

        context['GOOGLE_MAPS_API_KEY'] = key

        points = Point.objects.all()

        context['points'] = points

        return context


class GmapSimpleView(GmapView):
    template_name = "gmap/gmap_simple.html"
