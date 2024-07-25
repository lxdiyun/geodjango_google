from django import forms
from django.contrib.gis.geos import Point
from django.utils.safestring import mark_safe
from django.conf import settings

class GoogleMapsWidget(forms.TextInput):
    template_name = 'google_maps_widget.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if isinstance(value, Point):
            context['widget']['value'] = f"{value.y},{value.x}"  # lat, lng

        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY
        lat, lng = settings.DEFAULT_GMAP_CENTER.split(',')
        context['DEFAULT_GMAP_CENTER'] = f'{{lat: {lat}, lng: {lng}}}'

        return context

    def value_from_datadict(self, data, files, name):
        value = context = super().value_from_datadict(data, files, name)
        x, y = value.split(',')

        return Point(float(y), float(x))
