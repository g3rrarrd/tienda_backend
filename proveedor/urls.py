from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, GetProveedorView, UpdatePayDatProveedorView

router = DefaultRouter()
router.register(r'proveedor', ProveedorViewSet)

urlpatterns = [
    path('proveedor/get/', GetProveedorView.as_view()),
    path('proveedor/update/payday/', UpdatePayDatProveedorView.as_view()),
    path('', include(router.urls)),
]