from rest_framework import viewsets
from .models import compra, compra_x_producto
from .serializers import CompraSerializer, CompraxProductoSerializer


class CompraViewSet(viewsets.ModelViewSet):
    queryset = compra.objects.all()
    serializer_class = CompraSerializer

class CompraxProductoViewSet(viewsets.ModelViewSet):
    queryset = compra_x_producto.objects.all()
    serializer_class = CompraxProductoSerializer