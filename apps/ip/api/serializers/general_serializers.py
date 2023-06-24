from apps.ip.models import Pais
from rest_framework import serializers


class PaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pais
        exclude = ('state','created_date', 'modified_date', 'deleted_date')
