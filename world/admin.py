from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from models import WorldBorder

# Can also set GOOGLE_MAPS_API_KEY in settings
GMAP = GoogleMap(key='AIzaSyC0EnKraozzSAB8B5fqSN3w-vFWChYdWIQ')


class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'

admin.site.register(WorldBorder, GoogleAdmin)
