from rest_framework import viewsets
from tutiendaapp.serializers import ProductoSerializer
from tutiendaapp.models import Producto


class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()