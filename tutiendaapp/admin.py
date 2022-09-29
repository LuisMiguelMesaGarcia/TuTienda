from django.contrib import admin
from .models import User
from .models import Venta
from .models import Producto
from .models import RegistroVenta

admin.site.register(User)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(RegistroVenta)
# Register your models here.
