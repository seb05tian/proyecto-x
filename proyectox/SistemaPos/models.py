from django.db import models
from django.conf import settings


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imprime_en_cocina = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Sala(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    ESTADO_CHOICES = [
        ('libre', 'Libre'),
        ('ocupada', 'Ocupada'),
        ('espera', 'En espera'),
    ]

    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    numero = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='libre')

    class Meta:
        unique_together = ('sala', 'numero')

    def __str__(self):
        return f"Mesa {self.numero} - {self.sala.nombre}"


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('enviado', 'Enviado'),
        ('cobrado', 'Cobrado'),
    ]

    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierto')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - Mesa {self.mesa.numero}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    nota = models.TextField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.precio_unitario = self.producto.precio
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"


class MovimientoCaja(models.Model):
    TIPO_CHOICES = [
        ('Venta', 'Venta'),
    ]

    fecha = models.DateTimeField(auto_now_add=True)
    tipo_movimiento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    concepto = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.monto}"


class Licencia(models.Model):
    codigo = models.CharField(max_length=255)
    fecha_activacion = models.DateTimeField()
    fecha_expiracion = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=[('activa', 'Activa'), ('inactiva', 'Inactiva')], default='activa')

    def __str__(self):
        return f"Licencia {self.codigo} ({self.estado})"
