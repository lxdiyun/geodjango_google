from django.conf import settings

def google_maps(request):
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
        'DEFAULT_MAP_CENTER': settings.DEFAULT_GMAP_CENTER,
    }

    return context
