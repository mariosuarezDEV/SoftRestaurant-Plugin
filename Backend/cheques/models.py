from django.db import models

# Create your models here.


#Modelo que obtiene la información de las ventas
class cheque_detalle(models.Model):
    folio_det = models.AutoField(primary_key=True, verbose_name='Folio detalle')
    cheque_folio = models.IntegerField(verbose_name='Folio cheque', null=False, blank=False)
    movimiento = models.IntegerField(verbose_name='Movimiento', null=False, blank=False)
    cantidad = models.IntegerField(verbose_name='Cantidad', null=False, blank=False)
    id_producto = models.IntegerField(verbose_name='ID Producto', null=False, blank=False)
    precio = models.FloatField(verbose_name='Precio', null=False, blank=False)
    impuesto_uno = models.FloatField(verbose_name='Impuesto uno', null=False, blank=False)
    precio_sin_impuestos = models.FloatField(verbose_name='Precio sin impuestos', null=False, blank=False)

# Modelo que maneja las acciones de facturación
class cheque(models.Model):
    folio = models.AutoField(primary_key=True, verbose_name='Folio')
    num_cheque = models.IntegerField(verbose_name='Número de cheque', null=False, blank=False)
    fecha_movimiento = models.DateField(verbose_name='Fecha de movimiento', null=False, blank=False)
    mesa = models.IntegerField(verbose_name='Mesa', null=False, blank=False)
    facturado = models.BooleanField(verbose_name='Estado de facturación', null=False, blank=False)
    total_articulos = models.IntegerField(verbose_name='Total de artículos', null=False, blank=False) # Estos campos se pueden calcular de acuerdo a el miismo folio de cheque_detalle
    subtotal = models.FloatField(verbose_name='Subtotal', null=False, blank=False)


    def __str__(self):
        return self.folio

