from django.db import models

# MODELO: CLIENTE_GLOBAL
class ClienteGlobal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais_residencia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=15, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

# ===================
# MODELO: PEDIDO (Corresponde a la tabla PEDIDOS)
# ===================
class Pedido(models.Model):
    # pedido_id (PK) es automático por defecto en Django
    fecha_hora = models.DateTimeField(auto_now_add=True)
    total_neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    metodo_pago = models.CharField(max_length=50)
    estado_pedido = models.CharField(max_length=50, default='Pendiente')
    impuesto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    direccion_envio = models.CharField(max_length=255)

    # RELACIÓN 1 a N: Un cliente puede tener varios pedidos.
    cliente = models.ForeignKey(
        ClienteGlobal,
        on_delete=models.CASCADE,
        related_name="pedidos"
    )

    def __str__(self):
        return f"Pedido #{self.pk} - Cliente: {self.cliente.apellido}"