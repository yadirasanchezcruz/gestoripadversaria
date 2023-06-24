from django.urls import path
from apps.incidente.api.views.general_views import TecnologiaSerializerListAPIView, ClasificacionIncidenteSerializerListAPIView, EntidadSerializerListAPIView, NivelPeligrosidadSerializerListAPIView, NivelSeguridadSerializerListAPIView
from apps.incidente.api.views.incidente_views import IncidenteListAPIView




urlpatterns = [
    path('tecnologia/', TecnologiaSerializerListAPIView.as_view(), name = 'tecnologia'),
    path('clasificacionincidente/', ClasificacionIncidenteSerializerListAPIView.as_view(), name = 'clasificacionincidente'),
    path('entidad/', EntidadSerializerListAPIView.as_view(), name = 'entidad'),
    path('nivelpeligrosidad/', NivelPeligrosidadSerializerListAPIView.as_view(), name = 'nivelpeligrocidad'),
    path('nivelseguridad/', NivelSeguridadSerializerListAPIView.as_view(), name = 'nivelseguridad'),
    
    path('incidente/', IncidenteListAPIView.as_view(), name = 'incidente')
]
