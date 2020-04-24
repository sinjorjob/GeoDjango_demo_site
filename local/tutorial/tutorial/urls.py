from django.contrib import admin
from django.urls import path
from map import views #追加


urlpatterns = [
   path('admin/', admin.site.urls),
   path('map/', views.Home.as_view(), name='map')   #追加
]