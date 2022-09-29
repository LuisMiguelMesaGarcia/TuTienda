from rest_framework import viewsets
from tutiendaapp.serializers import RegistroVentaSerializer
from tutiendaapp.models import RegistroVenta


class RegistroVentaView(viewsets.ModelViewSet):
    serializer_class = RegistroVentaSerializer
    queryset = RegistroVenta.objects.all()