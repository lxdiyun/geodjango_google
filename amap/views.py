from django.shortcuts import render
from django.core.serializers import serialize
import json
from .models import AMapPoint

def gmap_points_view(request):
    map_points = AMapPoint.objects.all()
    features = []
    for point in map_points:
        point_dict = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [point.location.x, point.location.y]
            },
            "properties": {
                "name": point.name,
                "images": [img.image.url for img in point.images.all()]
            }
        }
        features.append(point_dict)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'gmap_points.html', {'gmap_points': json.dumps(geojson), 'title': 'Google Maps for AMapPoints'})

def amap_points_view(request):
    map_points = AMapPoint.objects.all()
    features = []
    for point in map_points:
        point_dict = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [point.location.x, point.location.y]
            },
            "properties": {
                "name": point.name,
                "images": [img.image.url for img in point.images.all()]
            }
        }
        features.append(point_dict)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'amap_points.html', {'amap_points': json.dumps(geojson), 'title': 'AMap for AMapPoints'})


# Create your views here.
