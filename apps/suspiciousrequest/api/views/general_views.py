from rest_framework import generics

from apps.base.api import GeneralListApiView

##from apps.suspiciousrequest.models import CodigoRespuestaHTTP, CodigoRespuestaServidor, Dominio, MetodoHTTP, Recurso, Referer, UserAgent, VersionHTTP

from apps.suspiciousrequest.api.serializers.general_serializers import CodigoRespuestaHTTPSerializer, CodigoRespuestaServidorSerializer, DominioSerializer, MetodoHTTPSerializer, RecursoSerializer, RefererSerializer, UserAgentSerializer, VersionHTTPSerializer


class CodigoRespuestaHTTPSerializerListAPIView(GeneralListApiView):
    serializer_class = CodigoRespuestaHTTPSerializer


class CodigoRespuestaServidorSerializerListAPIView(GeneralListApiView):
    serializer_class = CodigoRespuestaServidorSerializer


class DominioSerializerListAPIView(GeneralListApiView):
    serializer_class = DominioSerializer


class MetodoHTTPSerializerListAPIView(GeneralListApiView):
    serializer_class = MetodoHTTPSerializer


class RecursoSerializerListAPIView(GeneralListApiView):
    serializer_class = RecursoSerializer


class RefererSerializerListAPIView(GeneralListApiView):
    serializer_class = RefererSerializer


class UserAgentSerializerListAPIView(GeneralListApiView):
    serializer_class = UserAgentSerializer


class VersionHTTPSerializerListAPIView(GeneralListApiView):
    serializer_class = VersionHTTPSerializer
