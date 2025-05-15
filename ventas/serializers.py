from rest_framework import serializers
from .models import venta, venta_x_producto
from empleado.serializers import EmpleadoSerializer
from credito.serializers import CreditoSerializer
from producto.serializers import ProductoSerializer

class VentaSerializer(serializers.ModelSerializer):
    empleado_detalle = EmpleadoSerializer(source='empleado', read_only=True)
    credito_detalle = CreditoSerializer(source='credito', read_only=True)

    class Meta:
        model = venta
        fields = [
            'codigo_venta',
            'empleado',
            'empleado_detalle',
            'credito',
            'credito_detalle',
            'monto',
            'metodo_pago',
            'fecha'
        ]

class VentaxProductoSerializer(serializers.ModelSerializer):

    venta_detalle = VentaSerializer(source='venta', read_only=True  )
    producto_detalle = ProductoSerializer(source='producto', read_only=True)

    class Meta:

        model = venta_x_producto
        fields = ['venta', 'venta_detalle', 'producto', 'producto_detalle','cantidad','precio_unitario', 'descuento']
