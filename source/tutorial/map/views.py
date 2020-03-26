from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Evacuation
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

#新宿
longitude = 35.80127657
latitude = 139.1811832

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Evacuation
    #context_object_name = 'locations'
    queryset = Evacuation.objects.all()
    template_name = 'map/index.html'


