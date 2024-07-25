from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import WorldBorder

@admin.register(WorldBorder)
class WorldBorderAdmin(OSMGeoAdmin):
    pass

