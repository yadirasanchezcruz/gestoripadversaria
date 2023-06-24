from apps.incidente.models import Tecnologia, ClasificacionIncidente, Entidad, NivelPeligrosidad, NivelSeguridad
from rest_framework import serializers


class TecnologiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tecnologia
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class ClasificacionIncidenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClasificacionIncidente
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EntidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entidad
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        
        
class NivelPeligrosidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NivelPeligrosidad
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        

class NivelSeguridadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NivelSeguridad
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
