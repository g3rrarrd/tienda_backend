from django.db import models
from proveedor.models import proveedor
from producto.models import producto

class compra(models.Model):
    METODO_CHOICES = (
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia')
    )

    COMPRA_CHOICES = (
        ('credito', 'Credito'),
        ('contado', 'Contado')
    )

    codigo_compra = models.CharField(max_length=10, primary_key=True)
    proveedor = models.ForeignKey(
        proveedor,
        on_delete=models.PROTECT
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, choices=METODO_CHOICES)
    tipo_compra = models.CharField(max_length=20, choices=COMPRA_CHOICES)
    fecha_compra = models.DateField()

class compra_x_producto(models.Model):
    compra = models.ForeignKey(
        compra,
        on_delete=models.CASCADE,
        to_field='codigo_compra'
    )
    producto = models.ForeignKey(
        producto,
        on_delete=models.PROTECT
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    monto = models.DecimalField(max_digits=10, decimal_places=2)