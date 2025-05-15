from django.db import models
from proveedor.models import proveedor 
from empleado.models import empleado  
from usuario.models import usuario 

class PagoBase(models.Model):
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Monto del pago'
    )
    fecha_pago = models.DateField(
        verbose_name='Fecha de pago'
    )
    metodo_pago = models.CharField(
        max_length=20,
        choices=[
            ('EFECTIVO', 'Efectivo'),
            ('TRANSFERENCIA', 'Transferencia'),
            ('CHEQUE', 'Cheque'),
        ],
        default='EFECTIVO',
        verbose_name='Método de pago'
    )
    referencia = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Número de referencia'
    )

    class Meta:
        abstract = True  

class PagoEmpleado(PagoBase):
    empleado = models.ForeignKey(
        empleado, 
        on_delete=models.PROTECT,
        related_name='pagos_empleado'
    )
    concepto_nomina = models.CharField(
        max_length=100,
        verbose_name='Concepto de nómina'
    )

class PagoCredito(PagoBase):
    usuario = models.ForeignKey(
        usuario,
        on_delete=models.PROTECT,
        related_name='pagos_credito'
    )

class PagoProveedor(PagoBase):
    proveedor = models.ForeignKey(
        proveedor,
        on_delete=models.PROTECT,
        related_name='pagos_proveedor'
    )
    factura = models.CharField(
        max_length=20,
        verbose_name='Número de factura'
    )
    iva = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='IVA aplicado'
    )