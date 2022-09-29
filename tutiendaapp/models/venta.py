from django.db import models

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    hora = models.TimeField('Hora')
    fecha = models.DateField('Fecha')

  