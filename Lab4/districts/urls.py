from django.urls import path

from . import views


urlpatterns = [
    path("", views.map_page, name="map"),
    path("api/where/", views.district_at, name="district-at"),
    path(
        "api/districts/",
        views.districts_geojson,
        name="districts-geojson",
        
    ),
]