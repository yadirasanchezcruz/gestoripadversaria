from django.db import models
from apps.base.models import BaseModel
from django.db.models import ForeignKey

class Tecnologia(BaseModel):
    
    descripcion = models.CharField('Descripción', max_length=200, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Tecnología'
        verbose_name_plural = 'Tecnologías'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.descripcion)
    
    
class ClasificacionIncidente(BaseModel):
    
    descripcion = models.CharField('Descripción', max_length=200, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Clasificación del incidente'
        verbose_name_plural = 'Clasificaciones de incidentes'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.descripcion)
    
    
class Entidad(BaseModel):
    
    nombre = models.CharField('Nombre', max_length=200, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.nombre)
    
    
    
class NivelPeligrosidad(BaseModel):
    
    descripcion = models.CharField('Descripción', max_length=200, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Nivel de peligrosidad'
        verbose_name_plural = 'Niveles de peligrosidad'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.descripcion)    
    
    
    
class NivelSeguridad(BaseModel):
    
    descripcion = models.CharField('Descripción', max_length=200, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Nivel de seguridad'
        verbose_name_plural = 'Niveles de seguridad'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.descripcion)    
    
    
class Incidente(BaseModel):

    nombre_corto = models.CharField('Nombre', max_length=150, blank=False, null=False)
    descripcion = models.CharField('Descripcion', max_length=400, blank=False, null=False)
    fecha = models.DateTimeField('Fecha del incidente', auto_now=False, auto_now_add=True, null=False)
    
    nivel_peligrosidad = models.ForeignKey(NivelPeligrosidad, on_delete=models.CASCADE)
    nivel_seguridad = models.ForeignKey(NivelSeguridad, on_delete=models.CASCADE)
    
    tecnologia = models.ForeignKey(Tecnologia, on_delete=models.CASCADE)
    clasificacion_incidente = models.ForeignKey(ClasificacionIncidente, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
        
    class Meta:
        verbose_name = 'Incidente'
        verbose_name_plural = 'Incidentes'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.nombre_corto)
    


    
       

