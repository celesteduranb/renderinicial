from rest_framework import serializers
from .models import Producto, Carrito, ItemCarrito, Pedido, PedidoItem

class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Producto
        fields = '__all__'

class ItemCarritoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), source='producto', write_only=True
    )

    class Meta:
        model = ItemCarrito
        fields = ['id', 'producto', 'producto_id', 'cantidad', 'subtotal']

    subtotal = serializers.SerializerMethodField()

    def get_subtotal(self, obj):
        return obj.subtotal()

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(many=True, read_only=True)

    class Meta:
        model = Carrito
        fields = ['id', 'fecha_creacion', 'items']


class PedidoItemSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        source='producto',
        write_only=True
    )

    class Meta:
        model = PedidoItem
        fields = ['producto', 'producto_id', 'cantidad', 'precio']


class PedidoSerializer(serializers.ModelSerializer):
    items = PedidoItemSerializer(many=True)
    

    class Meta:
        model = Pedido
        fields = ['id', 'nombre', 'telefono', 'direccion', 'total', 'estado', 'items']

    def create(self, validated_data):
        try:
            items_data = validated_data.pop('items')
            pedido = Pedido.objects.create(**validated_data)
            for item in items_data:
                PedidoItem.objects.create(pedido=pedido, **item)
            return pedido
        except Exception as e:
            print("🚨 ERROR al crear pedido:", e)
            raise e


