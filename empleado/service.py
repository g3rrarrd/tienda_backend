from .models import empleado
from .serializers import EmpleadoSerializer  
from rest_framework.exceptions import NotFound, ValidationError

def actualizar_estado_empleado(codigo_empleado, estado):
    if not codigo_empleado or not estado:
        raise ValidationError("Campos `codigo_empleado` y `estado` son requeridos")

    try:
        emp = empleado.objects.get(codigo_empleado=codigo_empleado)
    except empleado.DoesNotExist:
        raise NotFound("Empleado no encontrado")

    emp.estado = estado
    emp.save()

    return EmpleadoSerializer(emp).data
