from models import Point, Photo
from utils.views import GmapViewBase
from django.views.generic import TemplateView


class GmapView(GmapViewBase):
    template_name = "gmap/gmap.html"

    def get_context_data(self, **kwargs):
        context = super(GmapView, self).get_context_data(**kwargs)

        points = Point.objects.all()

        context['points'] = points

        return context


class GmapSimpleView(GmapView):
    template_name = "gmap/gmap_simple.html"


class GmapIndexView(GmapView):
    template_name = "gmap/index.html"


class GalleryView(TemplateView):
    template_name = "gmap/gallery.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)

        photos = Photo.objects.all()
        context['photos'] = photos

        print(context)

        return context
