from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import usuario
from .serializers import UsuarioSerializer
import json

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer

class ValidateUser(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)

            identidad = data.get('identidad')
            contrasenia = data.get('contrasenia')

            if not identidad or not contrasenia:
                return Response(
                    {'error': 'campo identidad y cotrasenia son requqeridos'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            usr = usuario.objects.exists(identidad=identidad, contrasenia=contrasenia)
            serializer = UsuarioSerializer(usr)

            return Response(
                serializer.data, status=status.HTTP_200_OK
            )
            
        except usuario.DoesNotExist:
            return Response(
                {"error": "Empleado no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )

class GetCustomer(APIView):
    def get(self, request):
        try:
            identidad = json.load(request.body).get('identidad')

            if not identidad:
                return Response(
                    {'error' : 'Campo identidad es requerido'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            cliente = usuario.objects.get(identidad=identidad)
            serializer = UsuarioSerializer(cliente);

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except usuario.DoesNotExist:
            return Response(
                {'error': 'Cliente no existe'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error' : str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )