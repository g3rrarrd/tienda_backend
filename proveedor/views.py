from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import proveedor
from .serializers import ProveedorSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = proveedor.objects.all()
    serializer_class = ProveedorSerializer

class GetProveedorView(APIView):
    def post(self, request):
        try:

            proveedor_obj = proveedor.objects.get(codigo=request.data.get('codigo'))

            serializer = ProveedorSerializer(proveedor_obj)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except proveedor.DoesNotExist:
            return Response(
                {"error": "Proveedor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UpdatePayDatProveedorView(APIView):
    def put(self, request):
        try:

            codigo_proveedor = request.data.get('codigo')
            nueva_fecha_cobro = request.data.get('fecha_cobro')

            if not codigo_proveedor or not fecha_cobro:
                return Response(
                    {'error' : 'campos `codigo_proveedor, fecha_cobro` son requeridos'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            proveedor_obj = proveedor.objects.get(codigo = codigo_proveedor)
            proveedor_obj.fecha_cobro = nueva_fecha_cobro
            proveedor_obj.save()

            serializer = ProveedorSerializer(proveedor_obj)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except proveedor.DoesNotExist:
            return Response(
                {"error": "Proveedor no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )