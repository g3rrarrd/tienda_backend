from rest_framework import serializers
from .models import compra, compra_x_producto
from proveedor.serializers import ProveedorSerializer
from producto.serializers import ProductoSerializer

class CompraSerializer(serializers.ModelSerializer):

    proveedor_detalle = ProveedorSerializer(source='proveedor', read_only=True)

    class Meta():
        
        model = compra
        fields = ['codigo_compra', 'proveedor', 'proveedor_detalle', 'monto', 'metodo_pago', 'tipo_compra', 'fecha_compra']


class CompraxProductoSerializer(serializers.ModelSerializer):
    compra_detalle = CompraSerializer(source='compra', read_only=True  )
    producto_detalle = ProductoSerializer(source='producto', read_only=True)

    class Meta:

        model = compra_x_producto
        fields = ['compra', 'compra_detalle', 'producto', 'producto_detalle','cantidad', 'precio_unitario','monto']