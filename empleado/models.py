from django.db import models
from usuario.models import usuario

class rol(models.Model): 
    rol = models.CharField(max_length=10, unique=True)  

    def __str__(self):
        return self.rol
    
class empleado(models.Model): 
    usuario = models.OneToOneField(
        usuario,
        on_delete=models.CASCADE,
        primary_key=True  
    )
    rol = models.ForeignKey( 
        rol,
        on_delete=models.PROTECT 
    )
    codigo_empleado = models.CharField(max_length=15, unique=True)
    fecha_contrato = models.DateField()
    salario = models.DecimalField( 
        max_digits=10,
        decimal_places=2
    )
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.codigo_empleado} - {self.rol.rol}"
