from rest_framework import serializers

from apps.suspiciousrequest.models import Peticion



class PeticionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Peticion
        exclude = ('state','created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'metodo_HTTP': instance.metodo_HTTP.metodo_HTTP,
            'versionHTTP': instance.versionHTTP.version_HTTP,
        'codigo_respuesta_HTTP': instance.codigo_respuesta_HTTP.codigo_respuesta_HTTP,
        'codigo_Respuesta_Servidor': instance.codigo_Respuesta_Servidor.codigo_respuesta_servidor,
        'user_agent': instance.user_agent.user_agent,
        'referer': instance.referer.referer,
        'recurso': instance.recurso.recurso,
        'dominio': instance.dominio.dominio,
        'direccion_IP' :instance.direccion_IP.direccion_IP
        }