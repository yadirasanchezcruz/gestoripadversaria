from rest_framework import generics

from apps.base.api import GeneralListApiView

from apps.suspiciousrequest.api.serializers.peticion_serializer import PeticionSerializer

class PeticionSerializerListAPIView(GeneralListApiView):
    serializer_class = PeticionSerializer
