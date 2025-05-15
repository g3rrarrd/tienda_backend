from rest_framework import serializers
from .models import proveedor
from usuario.serializers import UsuarioSerializer

class ProveedorSerializer(serializers.ModelSerializer):

    usuario_detalle = UsuarioSerializer(source='usuario', read_only=True)

    class Meta:

        model = proveedor
        fields = ['usuario', 'usuario_detalle', 'codigo', 'fecha_cobro']
