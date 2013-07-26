from django.contrib.contenttypes import generic
from util.utils_models import PointBase, PhotoBase


class Point(PointBase):
    photos = generic.GenericRelation('Photo',
                                     content_type_field='content_type',
                                     object_id_field='object_id')


class Photo(PhotoBase):
    pass
