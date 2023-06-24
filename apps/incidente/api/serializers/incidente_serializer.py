
from rest_framework import serializers

from apps.incidente.models import Tecnologia, ClasificacionIncidente, Entidad, Incidente
from apps.incidente.api.serializers.general_serializers import TecnologiaSerializer, ClasificacionIncidenteSerializer, EntidadSerializer, NivelPeligrosidadSerializer, NivelSeguridadSerializer


class IncidenteSerializer(serializers.ModelSerializer):
    tecnologia = TecnologiaSerializer()
    clasificacion_incidente = ClasificacionIncidenteSerializer()
    entidad = EntidadSerializer()
    nivel_peligrosidad = NivelPeligrosidadSerializer()
    nivel_seguridad = NivelSeguridadSerializer()

    class Meta:
        model = Incidente
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre_corto': instance.nombre_corto,
            'descripcion': instance.descripcion,
            'fecha': instance.fecha,

            'nivel_peligrosidad': instance.nivel_peligrosidad.descripcion,
            'nivel_seguridad': instance.nivel_seguridad.descripcion,
            'tecnologia': instance.tecnologia.descripcion,
            'clasificacion_incidente': instance.clasificacion_incidente.descripcion,
            'entidad': instance.entidad.nombre
        }