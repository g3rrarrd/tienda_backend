from rest_framework import serializers
from .models import empleado, rol
from usuario.serializers import UsuarioSerializer

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = ['id', 'rol']  

class EmpleadoSerializer(serializers.ModelSerializer):
    
    rol_detalle = RolSerializer(source='rol', read_only=True)
    usuario_detalle = UsuarioSerializer(source='usuario', read_only=True)
    
    class Meta:
        model = empleado
        fields = ['codigo_empleado', 'usuario', 'usuario_detalle', 'rol', 'rol_detalle', 'fecha_contrato', 'salario', 'estado']