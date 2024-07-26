from django import forms
from django.contrib.gis.geos import Point
from django.utils.safestring import mark_safe
from django.conf import settings

class AMapWidget(forms.TextInput):
    template_name = 'amap_widget.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if isinstance(value, Point):
            context['widget']['value'] = f"{value.y},{value.x}"  # lat, lng

        context['AMAP_SECURITY_JS_CODE'] = settings.AMAP_SECURITY_JS_CODE
        context['AMAP_API_KEY'] = settings.AMAP_API_KEY
        lat, lng = settings.DEFAULT_AMAP_CENTER.split(',')
        context['DEFAULT_AMAP_CENTER'] = f'{{latitude: {lat}, longitude: {lng}}}'

        return context

    def value_from_datadict(self, data, files, name):
        value = context = super().value_from_datadict(data, files, name)
        x, y = value.split(',')

        return Point(float(y), float(x))
