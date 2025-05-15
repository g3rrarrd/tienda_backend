from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, GetRequeirimiento, GetProductsByStorage

router = DefaultRouter()
router.register(r'producto', ProductoViewSet)

urlpatterns = [
    path('requerimiento/', GetRequeirimiento.as_view()),
    path('inventario/', GetProductsByStorage.as_view()),
    path('', include(router.urls)),
]