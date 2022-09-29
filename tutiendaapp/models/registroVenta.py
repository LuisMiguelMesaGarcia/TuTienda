from tutiendaapp import models
from django.db import models
from .venta import Venta
from .user import User
from .producto import Producto

class RegistroVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name="venta", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name="producto", on_delete=models.CASCADE)