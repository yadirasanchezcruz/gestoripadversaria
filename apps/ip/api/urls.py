from django.urls import path
from apps.ip.api.views.general_views import PaisListAPIView
from apps.ip.api.views.direccionip_views import DireccionIPListAPIView




urlpatterns = [
    path('pais/', PaisListAPIView.as_view(), name = 'pais'),
    path('direccionip/', DireccionIPListAPIView.as_view(), name = 'direccionip')
]
