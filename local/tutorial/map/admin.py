#from django.contrib import admin
from django.contrib.gis import admin
from map.models import Evacuation
from leaflet.admin import LeafletGeoAdmin   #追加

 #admin.site.register(Evacuation, admin.GeoModelAdmin)   #コメントアウト
admin.site.register(Evacuation, LeafletGeoAdmin)   #追加