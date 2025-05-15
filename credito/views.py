from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreditoSerializer
from .models import credito
import json

class CreditoViewSet(viewsets.ModelViewSet):
    queryset = credito.objects.all()
    serializer_class = CreditoSerializer

class GetCreditByDate(APIView):
    def get(self, request):
        try:
            fecha_ini = request.query_params.get('inicio')
            fecha_fin = request.query_params.get('final')

            queryset = credito.objects.all()

            if fecha_ini and fecha_fin:
                queryset = queryset.filter(fecha__range=[fecha_ini, fecha_fin])
            elif fecha_ini:
                queryset = queryset.filter(fecha__gte=fecha_ini)
            elif fecha_fin:
                queryset = queryset.filter(fecha__lte=fecha_fin)
            else:
                return Response(
                    {'error': 'Debe proporcionar al menos una fecha (inicio o final)'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer = CreditoSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"Error inesperado: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class GetCreditByDni(APIView):
    def get(self, request):
        try:

            identidad = request.query_params.get('identidad')

            if not identidad:
                return Response(
                    {'error' : 'Campo identidad requerido'},
                    status=status.HTTP_200_OK
                )
            
            list_credito = credito.objects.filter(identidad)

            if not list_credito.exists():
                return Response(
                    {'message': 'No se encontraron créditos para esta identidad'},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = CreditoSerializer(list_credito)

            return Response(
                serializer.data, status=status.HTTP_200_OK
               )
    
        except Exception as e:
            return Response(
                {'error' : str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )