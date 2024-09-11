
# Modelos para obtener los productos de la empresa

from cheques.models import Productos, Productosdetalle


class ajustes_empresa:

    def __init__(self, producto_uno, producto_dos, producto_tres):
        self.producto_uno = producto_uno
        self.producto_dos = producto_dos
        self.producto_tres = producto_tres

    def get_producto_uno(self):
        try:
            insumo = Productos.objects.get(idproducto=self.producto_uno).idproducto
            return insumo
        except Productos.DoesNotExist:
            return None

    def get_producto_dos(self):
        try:
            insumo = Productos.objects.get(idproducto=self.producto_dos).idproducto
            return insumo
        except Productos.DoesNotExist:
            return None

    def get_producto_tres(self):
        try:
            insumo = Productos.objects.get(idproducto=self.producto_tres).idproducto
            return insumo
        except Productos.DoesNotExist:
            return None