from django.contrib.gis import admin
from django.contrib.gis.db import models
from django.utils.html import format_html
from .models import GMapPoint, GMapPointImage
from .widgets import GoogleMapsWidget

class GMapPointImageInline(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = GMapPointImage
    extra = 1  # How many extra forms to show

    fields = ('image', 'image_thumbnail',)  # Add the thumbnail field
    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, instance):
        """Displays a thumbnail for the given image instance."""
        if instance.image:
            # Assuming 'image' is a FileField or ImageField on your GMapPointImage model
            # Adjust the width/height as needed
            return format_html('<img src="{}" width="100" height="auto" />', instance.image.url)
        return ""

    image_thumbnail.short_description = "Thumbnail"


@admin.register(GMapPoint)
class GMapPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [GMapPointImageInline]
    formfield_overrides = {
        models.PointField: {"widget": GoogleMapsWidget}
    }

