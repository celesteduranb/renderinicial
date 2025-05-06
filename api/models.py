from django.db import models

# Modelo para los productos
class Producto(models.Model):
    CATEGORIAS = [
        ('entradas', 'Entradas'),
        ('pizzas', 'Pizzas'),      # Este es una tupla de opciones
        ('bebidas', 'Bebidas'),
        ('postres', 'Postres'),
    ] 
    
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='imagenes/')  
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo para el carrito de compras
class Carrito(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito #{self.id}"

# Modelo para los items del carrito
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre}"

    def subtotal(self):
        return self.producto.precio * self.cantidad
    
    # Modelo para el pedido confirmado
class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.nombre}"

# Modelo para los items del pedido
class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)  # Precio en el momento del pedido

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} - Pedido #{self.pedido.id}"