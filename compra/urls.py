from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CompraViewSet, CompraxProductoViewSet

router = DefaultRouter()
router.register(r'compra', CompraViewSet)
router.register(r'compra_x_producto', CompraxProductoViewSet)

urlpatterns = [
    path('', include(router.urls))
]