from rest_framework import serializers
from .models import credito

class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = credito
        fields = ['codigo_credito', 'usuario', 'descripcion']