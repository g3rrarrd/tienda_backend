from rest_framework import serializers
from .models import producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ['codigo_producto', 'inventario', 'tipo_producto', 'talla', 'color']