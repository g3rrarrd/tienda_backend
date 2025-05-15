from django.db import models
from usuario.models import usuario

class credito(models.Model):
    codigo_credito = models.CharField(max_length=10, primary_key=True)
    usuario = models.ForeignKey(
        usuario,
        on_delete=models.PROTECT
    )
    descripcion = models.CharField(max_length=100)
    
