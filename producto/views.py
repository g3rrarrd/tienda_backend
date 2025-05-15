from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializers import ProductoSerializer
from .models import producto

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

class GetRequeirimiento(APIView):
    def get(self, request):

        try:
            codigo_inventario = request.data.get('codigo_inventario')
            requerimiento = request.data.get('requerimiento')

            if not codigo_inventario:
                return Response(
                    {'error': "Campo 'codigo_inventario' es requerido"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            productos = producto.objects.filter(codigo_inventario=codigo_inventario)
            informacion = [getattr(prod, requerimiento) for prod in productos]

            return Response(
                {'data' : informacion},
                status=status.HTTP_200_OK
            )
        
        except producto.DoesNotExist:
            return Response(
                {'error' : 'No existen productos del inventario'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error' : str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

