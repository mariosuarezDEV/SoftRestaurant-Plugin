# Modelos de la base de datos
from cheques.models import Productos, Productosdetalle, Cheques, Cheqdet

class sustituir_productos:
    def __init__(self, producto_id, cheques, cantidad_producto):
        self.producto_id = producto_id
        self.cheques = cheques
        self.cantidad_producto = cantidad_producto

    def get_producto_informacion(self):
        try:
            producto = Productos.objects.select_related('Productosdetalle').get(idproducto=self.producto_id)
            return {
                'descripcion': producto.descripcion,
                'precio': producto.Productosdetalle.precio,
                'impuesto': producto.Productosdetalle.impuesto1,
                'precio_sin_impuesto': producto.Productosdetalle.preciosinimpuestos
            }
        except Exception as e:
            return str(e)
    # Mantenimiento de folio de ventas
    def sustituir_detalles_cheque(self):  #Esto tiene una lista de folios de los cheques
        mi_producto = self.get_producto_informacion()
        Cheqdet.objects.filter(foliodet__in=self.cheques).update(cantidad=self.cantidad_producto,
                                                                 precio=mi_producto['precio'],
                                                                 impueto1=mi_producto['impuesto'],
                                                                 preciosinimpuestos=mi_producto['precio_sin_impuesto'],
                                                                 precioncatalogo=mi_producto['precio_sin_impuesto'])