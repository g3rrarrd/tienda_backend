from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import inventario
from .serializers import InventarioSerializer
from producto.models import producto
import json

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = inventario.objects.all()
    serializer_class = InventarioSerializer

class UpdateStorage(APIView):

    def put(self, request):
        try:

            codigo_inventario = request.data.get('codigo_producto')

            if not codigo_inventario:
                return Response(
                    {"error" : "campo codigo_inventario es requerido"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            inv = inventario.objects.get(codigo_inventario=codigo_inventario)

            for campo in request:
                if campo:
                    inv.campo = campo

            inv.save()
            
            return Response({'message' : True}, status=status.HTTP_200_OK)
        
        except inventario.DoesNotExist:
            return Response({'error' : 'El inventario no existe'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RegisterStorageProduct(APIView):
    def post(self, request):
        try:
            data = request.data
            inv_data = data.get('inventario')
            productos_data = data.get('productos')

            if not inv_data:
                return Response(
                    {"error": "Campo `inventario` es requerido"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            inv = inventario.objects.create(**inv_data)

            for prod in productos_data:
                producto.objects.create(inventario=inv, **prod)

            return Response({"message": True}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )