from django.conf import settings

def maps(request):
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
        'DEFAULT_MAP_CENTER': settings.DEFAULT_GMAP_CENTER,
        'AMAP_SECURITY_JS_CODE': settings.AMAP_SECURITY_JS_CODE,
        'AMAP_API_KEY': settings.AMAP_API_KEY,
    }

    return context
