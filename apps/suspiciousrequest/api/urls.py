from django.urls import path
from apps.suspiciousrequest.api.views.general_views import CodigoRespuestaHTTPSerializerListAPIView, CodigoRespuestaServidorSerializerListAPIView, DominioSerializerListAPIView, MetodoHTTPSerializerListAPIView, RecursoSerializerListAPIView, RefererSerializerListAPIView, UserAgentSerializerListAPIView, VersionHTTPSerializerListAPIView
from apps.suspiciousrequest.api.views.peticion_views import PeticionSerializerListAPIView

urlpatterns = [
    path('CodigoRespuestaHTTP/', CodigoRespuestaHTTPSerializerListAPIView.as_view(), name='CodigoRespuestaHTTP'),
    path('CodigoRespuestaServidor/', CodigoRespuestaServidorSerializerListAPIView.as_view(), name='CodigoRespuestaServidor'),
    path('Dominio/', DominioSerializerListAPIView.as_view(), name='Dominio'),
    path('MetodoHTTP/', MetodoHTTPSerializerListAPIView.as_view(), name='MetodoHTTP'),
    path('Recurso/', RecursoSerializerListAPIView.as_view(), name='Recurso'),
    path('Referer/', RefererSerializerListAPIView.as_view(), name='Referer'),
    path('UserAgent/', UserAgentSerializerListAPIView.as_view(), name='UserAgent'),
    path('VersionHTTP/', VersionHTTPSerializerListAPIView.as_view(), name='VersionHTTP'),
    path('peticion/', PeticionSerializerListAPIView.as_view(), name='Peticion'),
]
