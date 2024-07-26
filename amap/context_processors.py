from django.conf import settings

def amaps(request):
    context = {
        'AMAP_SECURITY_JS_CODE': settings.AMAP_SECURITY_JS_CODE,
        'AMAP_API_KEY': settings.AMAP_API_KEY,
        'DEFAULT_AMAP_CENTER': settings.DEFAULT_AMAP_CENTER,
    }

    return context
