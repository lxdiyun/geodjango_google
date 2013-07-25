from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from models import WorldBorder
from django.conf import settings
from django.contrib.gis.maps.google.gmap import GoogleMapException

try:
    key = settings.GOOGLE_MAPS_API_KEY
except AttributeError:
    raise GoogleMapException('Google Maps API Key not found (try '
                             'adding GOOGLE_MAPS_API_KEY to your '
                             'settings).')
# Can also set GOOGLE_MAPS_API_KEY in settings
GMAP = GoogleMap(key=key)


class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'

admin.site.register(WorldBorder, GoogleAdmin)
