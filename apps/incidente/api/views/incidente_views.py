from rest_framework import generics

from apps.base.api import GeneralListApiView
from apps.incidente.api.serializers.incidente_serializer import IncidenteSerializer


class IncidenteListAPIView(GeneralListApiView):
    serializer_class = IncidenteSerializer


