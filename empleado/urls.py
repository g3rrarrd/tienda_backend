from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, RolViewSet, GetEmpleadoView, GetEmpleadoActivoView,UpdateSalaryEmpleadoView, UpdateStateEmpleadoView,UpdateRolEmpleadoView

router = DefaultRouter()
router.register(r'employee', EmpleadoViewSet)
router.register(r'rol', RolViewSet)

urlpatterns = [
    path('employee/get/', GetEmpleadoView.as_view()),
    path('employee/get/activate/', GetEmpleadoActivoView.as_view()),
    path('employee/update/salary/', UpdateSalaryEmpleadoView.as_view()),
    path('employee/update/state/', UpdateStateEmpleadoView.as_view()),
    path('employee/update/rol/', UpdateRolEmpleadoView.as_view()),
    path('', include(router.urls)),
]