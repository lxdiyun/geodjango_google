from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


# Create your models here.
class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField("Population 2005")
    fips = models.CharField("FIPS Code", max_length=2, null=True)
    iso2 = models.CharField("2 Digit ISO", max_length=2)
    iso3 = models.CharField("3 Digit ISO", max_length=3)
    un = models.IntegerField("United Nations Code")
    region = models.IntegerField("Region Code")
    subregion = models.IntegerField("Sub-Region Code")
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class MapPoint(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Map Points"

class MapPointImage(models.Model):
    map_point = models.ForeignKey(MapPoint, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='map_images/')

    def __str__(self):
        return f"Image for {self.map_point.name}"
