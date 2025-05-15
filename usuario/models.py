from django.db import models

class usuario(models.Model):
    identidad = models.CharField(max_length=15, primary_key=True) 
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50, unique=True)  
    telefono = models.CharField(max_length=15)  
    contrasenia = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.identidad} - {self.nombres} {self.apellidos}"
    

