from django.db import models
from usuario.models import usuario

class proveedor(models.Model):
    usuario = models.OneToOneField(
        usuario,
        on_delete=models.CASCADE,
        primary_key=True
    )
    codigo = models.CharField(max_length=10)
    fecha_cobro = models.DateField()


