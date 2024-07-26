from django.contrib import admin

from django.contrib.gis import admin
from django.contrib.gis.db import models
from django.utils.html import format_html
from .models import AMapPoint, AMapPointImage
from .widgets import AMapWidget

class AMapPointImageInline(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = AMapPointImage
    extra = 1  # How many extra forms to show

    fields = ('image', 'image_thumbnail',)  # Add the thumbnail field
    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, instance):
        """Displays a thumbnail for the given image instance."""
        if instance.image:
            # Assuming 'image' is a FileField or ImageField on your AMapPointImage model
            # Adjust the width/height as needed
            return format_html('<img src="{}" width="100" height="auto" />', instance.image.url)
        return ""

    image_thumbnail.short_description = "Thumbnail"


@admin.register(AMapPoint)
class AMapPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [AMapPointImageInline]
    formfield_overrides = {
        models.PointField: {"widget": AMapWidget}
    }

