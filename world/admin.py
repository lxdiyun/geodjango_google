from django.contrib.gis import admin
from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin
import admin_thumbnails
from .models import MapPoint, WorldBorder, MapPointImage
from .widgets import GoogleMapsWidget

from .models import MapPoint, MapPointImage


@admin_thumbnails.thumbnail('image')
class MapPointImageInline(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = MapPointImage
    extra = 1  # How many extra forms to show


@admin.register(MapPoint)
class MapPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [MapPointImageInline]
    formfield_overrides = {
        models.PointField: {"widget": GoogleMapsWidget}
    }

@admin.register(WorldBorder)
class WorldBorderAdmin(OSMGeoAdmin):
    pass


