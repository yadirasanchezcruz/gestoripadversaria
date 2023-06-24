from apps.suspiciousrequest.models import CodigoRespuestaHTTP, CodigoRespuestaServidor, Dominio, MetodoHTTP, Recurso, Referer, UserAgent, VersionHTTP
from rest_framework import serializers


class CodigoRespuestaHTTPSerializer(serializers.ModelSerializer):

    class Meta:
        model = CodigoRespuestaHTTP
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class CodigoRespuestaServidorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CodigoRespuestaServidor
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class DominioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dominio
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class MetodoHTTPSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetodoHTTP
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class RecursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recurso
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class RefererSerializer(serializers.ModelSerializer):

    class Meta:
        model = Referer
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class UserAgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAgent
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class VersionHTTPSerializer(serializers.ModelSerializer):

    class Meta:
        model = VersionHTTP
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
