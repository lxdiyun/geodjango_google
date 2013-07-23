from util.models import Point
from util.views import GmapBaseView


class GmapView(GmapBaseView):
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
