from django.db import models

class inventario(models.Model):
    codigo_inventario = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=20)
    imagen = models.BinaryField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)



