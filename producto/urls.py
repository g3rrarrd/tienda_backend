from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

router = DefaultRouter()
router.register(r'producto', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls))
]