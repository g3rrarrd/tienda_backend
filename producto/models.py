from django.db import models
from inventario.models import inventario

class producto(models.Model):
    PRODUCTO_CHOICES = (
        ('calzado', 'Calzado'),
        ('ropa', 'Ropa'),
        ('deporte', 'Deportes'),
        ('lociones', 'Lociones'),
        ('llaveros', 'Llaveros'),
        ('vasos', 'Vasos'),
        ('varios', 'Varios')
    )
    COLOR_CHOICES = (
        ('Rojo', 'rojo'),
        ('Azul', 'azul'),
        ('Verde', 'verde'),
        ('Morado', 'morado'),
        ('Negro', 'negro'),
        ('Beige', 'beige'),
        ('Cafe', 'cafe'),
        ('Celeste', 'celeste'),
        ('Blanco', 'blanco')
    )

    codigo_producto = models.CharField(max_length=10, primary_key=True)
    inventario = models.ForeignKey(
        inventario,
        on_delete=models.PROTECT
    )
    tipo_producto = models.CharField(max_length=10, choices=PRODUCTO_CHOICES)
    talla = models.CharField(max_length=5)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
