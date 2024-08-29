from cheques.models import Productos, Productosdetalle
# Funcion para obtener los productos de la base de datos

class Filtrado_productos:
    def __init__(self):
        pass

    def producto_aleatorio(self):
        # Obtener los productos que valgan menos de 150 pesos
        try:
            productos = Productosdetalle.objects.filter(precio__lt=150)
            # Escoger un producto aleatorio
            productos = productos.order_by('?')[:1]
            return productos
        except Exception as e:
            return str(e)

    def obtener_producto_lista_uno(self,idproducto):
        # Obtener el producto solicitada
        #Convertir el idproducto a entero
        try:
            nombre_producto = Productosdetalle.objects.get(idproducto=idproducto)
            return nombre_producto
        except Exception as e:
            return str(e)