from django.db import models

# Create your models here.

# Modelo para cheque detalles

# Modelo para cheque
class cheque_venta(models.Model):
    cheque_folio = models.AutoField(primary_key=True)
    folio = models.IntegerField() # Este numero debe ser el mismo que el de cheque_detalle
    fecha_movimiento = models.DateField() # Fecha del movimiento
    mesa = models.CharField(max_length=6) # Mesa del cliente
    factura = models.BooleanField() # Saber si esta facturado o no
    total_articulos = models.IntegerField() # Total de articulos pedidos ( esta información se toma de la cantidad de productos pedidos en cheque det en cada movimiento )
    subtotal = models.DecimalField(max_digits=10, decimal_places=2) # Subtotal de la cuenta
    total = models.DecimalField(max_digits=10, decimal_places=2) # Total de la cuenta
    tipo_pago = models.CharField(max_length=50, choices=[('Efectivo', 'Efectivo'), ('Tarjeta Débito', 'Tarjeta Débito'), ('Tarjeta Crédito', 'Tarjeta Crédito') ]) # Tipo de pago ( efectivo, tarjeta, cheque, etc )
    
class detalle_cheque(models.Model):
    cheque_folio = models.AutoField(primary_key=True)
    folio_det = models.IntegerField() # Este numero debe ser el mismo que el de cheque_venta
    movimiento = models.CharField(max_length=50) # Este campo es el indexado de el movimiento por cada producto pedido (1: cafe - $45 - 2 productos)
    cantidad = models.IntegerField() # Cantidad de productos pedidos
    id_producto = models.IntegerField() # ID del producto pedido
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Precio del producto pedido ( es el precio por unidad )
    impuesto_uno = models.DecimalField(max_digits=10, decimal_places=2) # Impuesto total del producto pedido
    precio_sin_impuesto = models.DecimalField(max_digits=10, decimal_places=2) # Precio sin impuesto del producto pedido
        
# El cheque folio es el id para cada uno de los modelos
# El folio debe ser igual para ambos modelos (el registro debe ser el mismo)

# El movimiento almacena datos como el nombre del producto, el precio y la cantidad de productos pedidos