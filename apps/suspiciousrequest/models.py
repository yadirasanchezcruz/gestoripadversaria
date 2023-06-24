from django.db import models
from apps.base.models import BaseModel
from apps.ip.models import DireccionIP
from django.db.models import ForeignKey


class MetodoHTTP(BaseModel):

    metodo_HTTP = models.CharField(
        'Descripción', max_length=100, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Método HTTP'
        verbose_name_plural = 'Métodos HTTP'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.metodo_HTTP)


class VersionHTTP(BaseModel):

    version_HTTP = models.CharField(
        'Descripción', max_length=50, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Versión del Protocolo HTTP'
        verbose_name_plural = 'Versiones del protocolo HTTP'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.version_HTTP)


class CodigoRespuestaHTTP(BaseModel):

    codigo_respuesta_HTTP = models.CharField(
        'Descripción', max_length=50, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Código de Respuesta HTTP'
        verbose_name_plural = 'Códigos de Respuesta HTTP'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.codigo_respuesta_HTTP)


class CodigoRespuestaServidor(BaseModel):

    codigo_respuesta_servidor = models.IntegerField(
        'Descripción', blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Código de respuesta del servidor'
        verbose_name_plural = 'Códigos de respuesta del servidor'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.codigo_respuesta_servidor)


class UserAgent(BaseModel):

    user_agent = models.CharField(
        'Descripción', max_length=1000, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Agente de Usuario'
        verbose_name_plural = 'Agentes de usuario'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.user_agent)


class Referer(BaseModel):

    referer = models.CharField(
        'Descripción', max_length=1000, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Referencia'
        verbose_name_plural = 'Referencias'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.referer)


class Recurso(BaseModel):

    recurso = models.CharField(
        'Descripción', max_length=500, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.recurso)


class Dominio(BaseModel):

    dominio = models.CharField(
        'Descripción', max_length=100, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Dominio'
        verbose_name_plural = 'Dominios'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.dominio)


class Peticion(BaseModel):

    tamano_respuesta = models.IntegerField('Tamaño Respuesta', default=0)
    fecha = models.DateTimeField('Fecha de la peticion HTTP')

    metodo_HTTP = models.ForeignKey( MetodoHTTP, on_delete=models.CASCADE)
    versionHTTP = models.ForeignKey(VersionHTTP, on_delete=models.CASCADE)
    codigo_respuesta_HTTP = models.ForeignKey( CodigoRespuestaHTTP, on_delete=models.CASCADE)
    codigo_Respuesta_Servidor = models.ForeignKey(CodigoRespuestaServidor, on_delete=models.CASCADE)
    user_agent = models.ForeignKey(UserAgent, on_delete=models.CASCADE)
    referer = models.ForeignKey(Referer, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    dominio: ForeignKey = models.ForeignKey(Dominio, on_delete=models.CASCADE)
    direccion_IP = models.ForeignKey(DireccionIP, on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Petición'
        verbose_name_plural = 'Peticiones'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.dominio)
