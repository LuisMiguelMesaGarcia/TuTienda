from rest_framework import viewsets
from tutiendaapp.serializers import VentaSerializer
from tutiendaapp.models import Venta


class VentaView(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()