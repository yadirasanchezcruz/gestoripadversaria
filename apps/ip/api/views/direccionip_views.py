from apps.base.api import GeneralListApiView
from apps.ip.api.serializers.direccionip_serializer import DireccionIPSerializer

class DireccionIPListAPIView(GeneralListApiView):
    serializer_class = DireccionIPSerializer