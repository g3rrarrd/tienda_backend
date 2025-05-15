from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PagoEmpleadoViewSet, PagoProveedorViewSet, PagoCreditoViewSet

router = DefaultRouter()
router.register(r'empleados', PagoEmpleadoViewSet, basename='pago-empleado')
router.register(r'proveedores', PagoProveedorViewSet, basename='pago-proveedor')
router.register(r'credito', PagoCreditoViewSet, basename='pago-credito')

urlpatterns = [
    path('', include(router.urls)),
]