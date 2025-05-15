from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VentaSerializer, VentaxProductoSerializer
from .models import venta, venta_x_producto

class VentaViewSet(viewsets.ModelViewSet):
    queryset = venta.objects.all()
    serializer_class = VentaSerializer

class VentaxProductoViewSet(viewsets.ModelViewSet):
    queryset = venta_x_producto.objects.all()
    serializer_class = VentaxProductoSerializer

class UpdateSell(APIView):
    def put(self, request):
        try:
            codigo_venta = request.data.get('codigo_venta')
            new_monto = request.data.get('monto')

            if not codigo_venta:
                return Response(
                    {'error': 'codigo_venta requerido'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if new_monto is None:
                return Response(
                    {'error': 'monto requerido'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            try:
                sell = venta.objects.get(codigo_venta=codigo_venta)
            except venta.DoesNotExist:
                return Response(
                    {'error': 'Venta no encontrada'},
                    status=status.HTTP_404_NOT_FOUND
                )

            sell.monto = new_monto
            sell.save()

            serializer = VentaSerializer(sell)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': f'Error inesperado: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    