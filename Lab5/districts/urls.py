from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("districts", views.DistrictViewSet)

urlpatterns = [
    path("", views.map_page, name="map"),
    path("api/", include(router.urls)),
]
