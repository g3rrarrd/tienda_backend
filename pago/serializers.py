from rest_framework import serializers
from .models import PagoEmpleado, PagoProveedor, PagoCredito
from empleado.serializers import EmpleadoSerializer 
from proveedor.serializers import ProveedorSerializer
from usuario.serializers import UsuarioSerializer

class PagoBaseSerializer(serializers.ModelSerializer):
    metodo_pago_display = serializers.CharField(
        source='get_metodo_pago_display', 
        read_only=True
    )
    
    class Meta:
        fields = [
            'id',
            'monto',
            'fecha_pago',
            'metodo_pago',
            'metodo_pago_display',
            'referencia'
        ]

class PagoEmpleadoSerializer(PagoBaseSerializer):
    empleado_detalle = EmpleadoSerializer(source='empleado', read_only=True)
    
    class Meta(PagoBaseSerializer.Meta):
        model = PagoEmpleado
        fields = PagoBaseSerializer.Meta.fields + [
            'empleado',
            'empleado_detalle',
            'concepto_nomina'
        ]

class PagoProveedorSerializer(PagoBaseSerializer):
    proveedor_detalle = ProveedorSerializer(source='proveedor', read_only=True)
    
    class Meta(PagoBaseSerializer.Meta):
        model = PagoProveedor
        fields = PagoBaseSerializer.Meta.fields + [
            'proveedor',
            'proveedor_detalle',
            'factura',
            'iva'
        ]

class PagoCreditoSerializer(PagoBaseSerializer):
    usuario_detalle = UsuarioSerializer(source='usuario', read_only=True)
    
    class Meta(PagoBaseSerializer.Meta):
        model = PagoCredito
        fields = PagoBaseSerializer.Meta.fields + [
            'usuario',
            'usuario_detalle',
        ]