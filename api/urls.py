from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CarritoViewSet, ItemCarritoViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'carritos', CarritoViewSet)
router.register(r'items-carrito', ItemCarritoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = router.urls
