from django.shortcuts import render
from django.core.serializers import serialize
import json
from .models import MapPoint

def map_points_view(request):
    map_points = MapPoint.objects.all()
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

    return render(request, 'map_points.html', {'map_points': json.dumps(geojson)})
