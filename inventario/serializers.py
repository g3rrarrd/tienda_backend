from rest_framework import serializers
from .models import inventario

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventario
        fields = ['codigo_inventario', 'nombre','imagen', 'precio_compra', 'precio_venta']