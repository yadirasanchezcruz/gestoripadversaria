
from rest_framework import serializers

from apps.ip.models import Pais, DireccionIP
from apps.ip.api.serializers.general_serializers import PaisSerializer


class DireccionIPSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()

    class Meta:
        model = DireccionIP
        exclude = ('state','created_date', 'modified_date','deleted_date')
        

    def to_representation(self,instance):
        return {
            'id': instance.id,
            'direccion_IP': instance.direccion_IP,
            'pais': instance.pais.nombre
        }
        