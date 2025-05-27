from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from .models import Producto, Carrito, ItemCarrito, Pedido, PedidoItem 
from .serializers import PedidoSerializer, ProductoSerializer, CarritoSerializer, ItemCarritoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class ItemCarritoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer

class NoHTMLFilterBrowsableAPIRenderer(BrowsableAPIRenderer):
    def get_filter_form(self, data, view, request):
        return None  # 👈 Esto evita que intente renderizar la plantilla HTML

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado', 'nombre']
    renderer_classes = [NoHTMLFilterBrowsableAPIRenderer, JSONRenderer]


