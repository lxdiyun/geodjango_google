from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.gis.maps.google.gmap import GoogleMapException


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

        return context
