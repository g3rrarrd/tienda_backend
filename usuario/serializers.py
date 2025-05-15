from rest_framework import serializers
from .models import usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['identidad', 'nombres', 'apellidos', 'correo', 'telefono']
        