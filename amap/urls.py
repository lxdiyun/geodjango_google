
from django.urls import path
from .views import gmap_points_view, amap_points_view

urlpatterns = [
    # ... your other url patterns
    path('gmap_points/', gmap_points_view, name='gmap_for_amap_points'),
    path('amap_points/', amap_points_view, name='amap_for_amap_points'),
]
