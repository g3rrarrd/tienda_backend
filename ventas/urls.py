from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VentaViewSet, VentaxProductoViewSet

router = DefaultRouter()
router.register(r'venta', VentaViewSet)
router.register(r'venta_x_producto', VentaxProductoViewSet)

urlpatterns = [
    path('', include(router.urls))
]