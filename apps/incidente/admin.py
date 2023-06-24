from django.contrib import admin
from .models import *

admin.site.register(NivelSeguridad)
admin.site.register(NivelPeligrosidad)
admin.site.register(Incidente)
admin.site.register(Tecnologia)
admin.site.register(ClasificacionIncidente)
admin.site.register(Entidad)