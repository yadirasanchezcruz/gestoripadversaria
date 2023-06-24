from rest_framework import generics

from apps.base.api import GeneralListApiView
from apps.ip.api.serializers.general_serializers import PaisSerializer


class PaisListAPIView(GeneralListApiView):
    serializer_class = PaisSerializer


