from django.contrib.gis import admin
from map.models import Evacuation
from leaflet.admin import LeafletGeoAdmin
 
admin.site.register(Evacuation, LeafletGeoAdmin)

