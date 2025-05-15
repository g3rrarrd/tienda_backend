from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PagoEmpleado, PagoProveedor, PagoCredito
from .serializers import PagoEmpleadoSerializer, PagoProveedorSerializer, PagoCreditoSerializer
import json

class PagoEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = PagoEmpleado.objects.select_related('empleado', 'empleado__usuario')
    serializer_class = PagoEmpleadoSerializer
    filterset_fields = ['empleado', 'concepto_nomina', 'fecha_pago']

class PagoProveedorViewSet(viewsets.ModelViewSet):
    queryset = PagoProveedor.objects.select_related('proveedor')
    serializer_class = PagoProveedorSerializer
    filterset_fields = ['proveedor', 'factura', 'fecha_pago']

class PagoCreditoViewSet(viewsets.ModelViewSet):
    queryset = PagoCredito.objects.select_related('usuario')
    serializer_class = PagoCreditoSerializer
    filterset_fields = ['usuario', 'fecha_pago']

class GetPayByYear(APIView):
    def get(self, request):
        try:
            year = request.query_params.get('anio')

            if not year:
                return Response(
                    {'error': 'Campo anio es requerido'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                year = int(year)
            except ValueError:
                return Response(
                    {'error': 'Campo anio debe ser un número'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            list_pagos = PagoCredito.objects.filter(fecha_pago__year=year)

            if not list_pagos.exists():
                return Response(
                    {'message': 'No se encontraron pagos de crédito para ese año'},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = PagoCreditoSerializer(list_pagos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': f'Error inesperado: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LastPay(APIView):
    def get(self, request):
        try:
            identidad = request.query_params.get('identidad')

            if not identidad:
                return Response(
                    {'error': 'Campo identidad requerido'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            pagos = PagoCredito.objects.filter(identidad=identidad).order_by('-fecha_pago')
            ultimo_pago = pagos.first()

            if not ultimo_pago:
                return Response(
                    {'message': 'No se encontraron pagos para esta identidad'},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = PagoCreditoSerializer(ultimo_pago)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': f'Error inesperado: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )