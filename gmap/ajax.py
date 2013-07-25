from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from util.models import Point


@dajaxice_register
def display_point(request, point_id):
    pid = int(point_id)
    photos = None
    point = None

    try:
        point = Point.objects.get(id=pid)
    except ObjectDoesNotExist:
        point = None

    if point is not None:
        photos = point.photos.all()

    render = render_to_string('gmap/intra_point_info.html',
                              {'point': point,
                               'photos': photos})

    dajax = Dajax()
    dajax.assign('#point_info', 'innerHTML', render)
    return dajax.json()
