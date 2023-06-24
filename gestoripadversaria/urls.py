from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.users.api.urls')),
    path('pais/', include('apps.ip.api.urls')),
    path('direccionip/', include('apps.ip.api.urls')),
    path('CodigoRespuestaHTTP/', include('apps.suspiciousrequest.api.urls')),
    path('CodigoRespuestaServidor/', include('apps.suspiciousrequest.api.urls')),
    path('Dominio/', include('apps.suspiciousrequest.api.urls')),
    path('MetodoHTTP/', include('apps.suspiciousrequest.api.urls')),
    path('Recurso/', include('apps.suspiciousrequest.api.urls')),
    path('Referer/', include('apps.suspiciousrequest.api.urls')),
    path('UserAgent/', include('apps.suspiciousrequest.api.urls')),
    path('VersionHTTP/', include('apps.suspiciousrequest.api.urls')),
    path('peticion/', include('apps.suspiciousrequest.api.urls')),
    
    
    path('tecnologia/', include('apps.incidente.api.urls')),
    path('clasificacionincidente/', include('apps.incidente.api.urls')),
    path('entidad/', include('apps.incidente.api.urls')),
    path('nivelpeligrosidad/', include('apps.incidente.api.urls')),
    path('nivelseguridad/', include('apps.incidente.api.urls')),
    
    path('incidente/', include('apps.incidente.api.urls')),
    

]
