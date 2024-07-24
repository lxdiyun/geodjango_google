from django.urls import path
from .views import map_points_view

urlpatterns = [
    # ... your other url patterns
    path('map_points/', map_points_view, name='map_points'),
]
