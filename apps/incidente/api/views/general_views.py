from apps.base.api import GeneralListApiView
from apps.incidente.api.serializers.general_serializers import TecnologiaSerializer, ClasificacionIncidenteSerializer, EntidadSerializer, NivelPeligrosidadSerializer, NivelSeguridadSerializer

class TecnologiaSerializerListAPIView(GeneralListApiView):
    serializer_class = TecnologiaSerializer
    
class ClasificacionIncidenteSerializerListAPIView(GeneralListApiView):
    serializer_class = ClasificacionIncidenteSerializer
    
class EntidadSerializerListAPIView(GeneralListApiView):
    serializer_class = EntidadSerializer

class NivelPeligrosidadSerializerListAPIView(GeneralListApiView):
    serializer_class = NivelPeligrosidadSerializer
    
class NivelSeguridadSerializerListAPIView(GeneralListApiView):
    serializer_class = NivelSeguridadSerializer