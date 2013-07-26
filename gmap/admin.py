from django.contrib.gis import admin
from util.utils_admin import PointAdminBase, PhotoInlineBase
from models import Point, Photo


class PhotoInline(PhotoInlineBase):
    models = Photo


class PointAdmin(PointAdminBase):
    inlines = [PhotoInline]

admin.site.register(Point, PointAdmin)
