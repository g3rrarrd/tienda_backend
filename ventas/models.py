from django.db import models
from empleado.models import empleado
from credito.models import credito
from producto.models import producto

class venta(models.Model):
    METODO_CHOICES = (
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia')
    )

    codigo_venta = models.CharField(max_length=10, primary_key=True)
    empleado = models.ForeignKey(
        empleado,
        on_delete=models.PROTECT
    )
    credito = models.ForeignKey(
        credito,
        on_delete=models.CASCADE,
        null=True
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, choices=METODO_CHOICES)
    fecha = models.DateField()

class venta_x_producto(models.Model):
    venta = models.ForeignKey(
        venta,
        on_delete=models.CASCADE,
        to_field='codigo_venta'
    )
    producto = models.ForeignKey(
        producto,
        on_delete=models.PROTECT
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)