from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import empleado, rol
from .service import actualizar_estado_empleado
from .serializers import EmpleadoSerializer, RolSerializer
import json

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = empleado.objects.all()
    serializer_class = EmpleadoSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = rol.objects.all()
    serializer_class = RolSerializer

class GetEmpleadoActivoView(APIView):
    def get(self, request):  
        try:
            
            emps = empleado.objects.filter(estado=True) 
            
            serializer = EmpleadoSerializer(emps, many=True)
            
            return Response({
                "success": True,
                "data": serializer.data,
                "count": len(serializer.data) 
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "success": False,
                "error": f"Error al obtener empleados: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetEmpleadoView(APIView):

    def post(self, request):
        try:
            data = json.loads(request.body)

            codigo_empleado = data.get('codigo_empleado')

            if not codigo_empleado:
                return Response(
                    {'error' : "El campo 'codigo_empleado' es requerido"},
                    status = status.HTTP_400_BAD_REQUEST
                )
            
            emp = empleado.objects.get(codigo_empleado=codigo_empleado)
            serializer = EmpleadoSerializer(emp)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except empleado.DoesNotExist:
            return Response(
                {"error": "Empleado no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class UpdateSalaryEmpleadoView(APIView):

    def put(self, request):
        try:
            
            codigo_empleado = request.data.get('codigo_empleado')
            salario = request.data.get('salario')

            if not codigo_empleado or salario is None:
                return Response(
                    {'error': "Los campos 'codigo_empleado' y 'salario' son requeridos"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            emp = empleado.objects.get(codigo_empleado=codigo_empleado)
            emp.salario = salario
            emp.save()

            serializer = EmpleadoSerializer(emp)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except empleado.DoesNotExist:
            return Response(
                {"error": "Empleado no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"Error inesperado: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class UpdateStateEmpleadoView(APIView):
    def post(self, request):
        try:
            data = json.load(request)

            identidad = data.get('identidad')
            identidad_jefe = data.get('identidad_jefe')

            if not identidad or not identidad_jefe:
                return Response(
                    {'error' : 'campo identidad y identidad_jefe requerido'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            rol = empleado.objects.get(identidad=identidad_jefe).rol_detalle

            if rol.rol != 'Jefe':
                return Response(
                    {'error': 'No tiene los permisos suficientes'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            emp = empleado.objects.get(identidad=identidad)

            data = actualizar_estado_empleado(emp.codigo_empleado, False)

            return Response(
                {'message': 'Empleado actualizado'},
                status=status.HTTP_200_OK
            )
        
        except empleado.DoesNotExist:
            return Response(
                {'errror' : 'Empleado no existe'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error' : f'Empleado no actualizado {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

    
    def put(self, request):
        try:

            codigo_empleado = request.data.get('codigo_empleado')
            estado = request.data.get('estado')

            data = actualizar_estado_empleado(codigo_empleado, estado)
            
            return Response(data, status=status.HTTP_200_OK)

        except empleado.DoesNotExist:
            return Response(
                {"error": "Empleado no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"Error inesperado: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UpdateRolEmpleadoView(APIView):
    def put(self, request):
        try:

            codigo_empleado = request.data.get('codigo_empleado')
            nuevo_rol_id = request.data.get('rol')

            if not codigo_empleado or not rol:
                return Response(
                    {'error' : "campos 'codigo_empleado, rol' son necesarios"},
                    status = status.HTTP_400_BAD_REQUEST
                )
            
            empleado_obj = empleado.objects.get(codigo_empleado=codigo_empleado)
            rol_obj = rol.objects.get(pk=nuevo_rol_id)
            
            empleado_obj.rol = rol_obj
            empleado_obj.save()
            
            serializer = EmpleadoSerializer(empleado_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except empleado.DoesNotExist:
            return Response(
                {"error": "Empleado no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"Error inesperado: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )