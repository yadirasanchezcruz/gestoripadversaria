from django.contrib import admin

from .models import *

admin.site.register(MetodoHTTP)
admin.site.register(VersionHTTP)
admin.site.register(CodigoRespuestaHTTP)
admin.site.register(CodigoRespuestaServidor)
admin.site.register(UserAgent)
admin.site.register(Referer)
admin.site.register(Recurso)
admin.site.register(Dominio)
admin.site.register(Peticion)