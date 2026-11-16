from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from rest_framework_gis.filters import InBBoxFilter

from .models import Facility

from .serializers import FacilitySerializer


class FacilityViewSet(viewsets.ModelViewSet):

    queryset = Facility.objects.all()

    serializer_class = FacilitySerializer

    http_method_names = ["get", "post", "head", "options"]

    filter_backends = [
        InBBoxFilter,
        DjangoFilterBackend
    ]

    bbox_filter_field = "geom"

    filterset_fields = ["kind"]