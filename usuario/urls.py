from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ValidateUser, GetCustomer

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('validar/', ValidateUser.as_view()),
    path('cliente/', GetCustomer.as_view())
]