from rest_framework import serializers
from tutiendaapp.models import RegistroVenta


class RegistroVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVenta
        fields = '__all__'