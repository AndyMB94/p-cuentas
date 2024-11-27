from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, ClienteViewSet, ProveedorViewSet, FacturaViewSet, UserViewSet

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'clientes', ClienteViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'facturas', FacturaViewSet, basename='facturas')
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
]
