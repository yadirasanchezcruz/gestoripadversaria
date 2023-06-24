from django.db import models
from apps.base.models import BaseModel
from django.db.models import ForeignKey

class Pais(BaseModel):
    
    nombre = models.CharField('Nombre', max_length=50, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.nombre)
    
    
class DireccionIP(BaseModel):

    direccion_IP = models.GenericIPAddressField('Dirección IP',  blank=False, null=False, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
        
    class Meta:
        verbose_name = 'Dirección IP'
        verbose_name_plural = 'Direcciones IP'

    def __str__(self):
        cadena = "{0}"
        #return cadena.format(self.direccion_IP)
        return f'{self.direccion_IP}'
    


    
       

