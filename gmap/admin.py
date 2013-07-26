from django.contrib.gis import admin
from utils.admin import PointAdminBase, PhotoInlineBase
from models import Point, Photo


class PhotoInline(PhotoInlineBase):
    model = Photo


class PointAdmin(PointAdminBase):
    inlines = [PhotoInline]

admin.site.register(Point, PointAdmin)
