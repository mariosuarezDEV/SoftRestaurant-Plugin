from itertools import product

from django.contrib import admin
from django.db import models
import datetime

from rest_framework.authtoken.views import obtain_auth_token

# Modelos de la app de cheques
from .models import Cheques, Cheqdet, Productos, Productosdetalle

def sustituir_producto_uno(modeladmin, request, queryset):
    productos = Productosdetalle.objects.get(idproducto="034003")

    for objeto in queryset: # Cambiar los cheques
        objeto.cierre = objeto.fecha + datetime.timedelta(minutes=3)
        objeto.mesa = "P/LL"
        objeto.nopersonas = 1
        objeto.cambio = 0
        objeto.descuento = 0
        objeto.usuariodescuento = ""
        objeto.idtipodescuento= ""
        objeto.tarjetadescuento = 0
        objeto.totalarticulos = 1
        objeto.subtotal = productos.precio
        objeto.total = productos.precio
        objeto.totalconpropina = productos.precio + objeto.propina
        objeto.totalimpuesto1 = 0 #Duda
        objeto.totalconcargo = productos.precio + objeto.cargo
        objeto.totalconpropinacargo = productos.precio + objeto.propina + objeto.cargo
        objeto.descuentoimporte = 0
        objeto.efectivo = productos.precio
        objeto.tarjeta = 0
        objeto.vales = 0
        objeto.otros = 0
        objeto.totalsindescuento = productos.precio
        objeto.totalalimentos = 0
        objeto.totalbebidas = 0
        objeto.totalotros = productos.precio
        objeto.totaldescuentos = 0 #Duda
        objeto.totaldescuentoalimentos = 0
        objeto.totaldescuentobebidas = 0
        objeto.totaldescuentootros = 0
        objeto.totalalimentossindescuentos = 0
        objeto.totalbebidasindescuentos = 0
        objeto.totalotrosindescuentos = productos.precio
        objeto.save()

        # Ahora actualiza los registros en Cheqdet
        for objeto in queryset:
            # Obtén los IDs de Cheqdet relacionados con el folio
            cheqdet_ids = list(Cheqdet.objects.filter(foliodet=objeto.folio).values_list('id', flat=True))

            if not cheqdet_ids:
                continue

            # Si hay más de un ID, elimina todos menos el primero
            if len(cheqdet_ids) > 1:
                ids_to_delete = cheqdet_ids[1:]  # Excluye el primero
                Cheqdet.objects.filter(id__in=ids_to_delete).delete()

            # Modifica el primer registro
            cheqdet = Cheqdet.objects.get(id=cheqdet_ids[0])
            cheqdet.cantidad = 1
            try:
                producto = Productos.objects.get(idproducto="034003")
            except Productos.DoesNotExist:
                modeladmin.message_user(request, "El producto con id '034003' no existe.")
                return

            cheqdet.idproducto = producto
            cheqdet.descuento = 0
            cheqdet.precio = productos.precio
            cheqdet.impuesto1 = 0
            cheqdet.preciosinimpuestos = productos.precio
            cheqdet.modificador = False
            cheqdet.comentario = ""
            cheqdet.usuariodescuento = ""
            cheqdet.comentariodescuento = ""
            cheqdet.comentario = ""
            cheqdet.idtipodescuento = ""
            cheqdet.preciocatalogo = productos.precio

            cheqdet.save()
    modeladmin.message_user(request, "El mantenimiento de la venta se hizo correctamente")

def sustituir_producto_dos(modeladmin, request, queryset):
    productos = Productosdetalle.objects.get(idproducto="042035")

    for objeto in queryset: # Cambiar los cheques
        objeto.cierre = objeto.fecha + datetime.timedelta(minutes=3)
        objeto.mesa = "P/LL"
        objeto.nopersonas = 1
        objeto.cambio = 0
        objeto.descuento = 0
        objeto.usuariodescuento = ""
        objeto.idtipodescuento= ""
        objeto.tarjetadescuento = 0
        objeto.totalarticulos = 1
        objeto.subtotal = productos.precio
        objeto.total = productos.precio
        objeto.totalconpropina = productos.precio + objeto.propina
        objeto.totalimpuesto1 = 0 #Duda
        objeto.totalconcargo = productos.precio + objeto.cargo
        objeto.totalconpropinacargo = productos.precio + objeto.propina + objeto.cargo
        objeto.descuentoimporte = 0
        objeto.efectivo = productos.precio
        objeto.tarjeta = 0
        objeto.vales = 0
        objeto.otros = 0
        objeto.totalsindescuento = productos.precio
        objeto.totalalimentos = 0
        objeto.totalbebidas = 0
        objeto.totalotros = productos.precio
        objeto.totaldescuentos = 0 #Duda
        objeto.totaldescuentoalimentos = 0
        objeto.totaldescuentobebidas = 0
        objeto.totaldescuentootros = 0
        objeto.totalalimentossindescuentos = 0
        objeto.totalbebidasindescuentos = 0
        objeto.totalotrosindescuentos = productos.precio
        objeto.save()

        # Ahora actualiza los registros en Cheqdet
        for objeto in queryset:
            # Obtén los IDs de Cheqdet relacionados con el folio
            cheqdet_ids = list(Cheqdet.objects.filter(foliodet=objeto.folio).values_list('id', flat=True))

            if not cheqdet_ids:
                continue

            # Si hay más de un ID, elimina todos menos el primero
            if len(cheqdet_ids) > 1:
                ids_to_delete = cheqdet_ids[1:]  # Excluye el primero
                Cheqdet.objects.filter(id__in=ids_to_delete).delete()

            # Modifica el primer registro
            cheqdet = Cheqdet.objects.get(id=cheqdet_ids[0])
            cheqdet.cantidad = 1
            try:
                producto = Productos.objects.get(idproducto="042035")
            except Productos.DoesNotExist:
                modeladmin.message_user(request, "El producto con id '042035' no existe.")
                return

            cheqdet.idproducto = producto
            cheqdet.descuento = 0
            cheqdet.precio = productos.precio
            cheqdet.impuesto1 = 0
            cheqdet.preciosinimpuestos = productos.precio
            cheqdet.modificador = False
            cheqdet.comentario = ""
            cheqdet.usuariodescuento = ""
            cheqdet.comentariodescuento = ""
            cheqdet.comentario = ""
            cheqdet.idtipodescuento = ""
            cheqdet.preciocatalogo = productos.precio

            cheqdet.save()
    modeladmin.message_user(request, "El mantenimiento de la venta se hizo correctamente")

def sustituir_producto_tres(modeladmin, request, queryset):
    productos = Productosdetalle.objects.get(idproducto="V007021")

    for objeto in queryset: # Cambiar los cheques
        objeto.cierre = objeto.fecha + datetime.timedelta(minutes=5)
        objeto.mesa = "P/LL"
        objeto.nopersonas = 1
        objeto.cambio = 0
        objeto.descuento = 0
        objeto.usuariodescuento = ""
        objeto.idtipodescuento= ""
        objeto.tarjetadescuento = 0
        objeto.totalarticulos = 2
        objeto.subtotal = productos.preciosinimpuestos * objeto.totalarticulos
        objeto.total = productos.precio * objeto.totalarticulos
        objeto.totalconpropina = objeto.total + objeto.propina
        objeto.totalimpuesto1 = (productos.precio * 0.16) * objeto.totalarticulos
        objeto.totalconcargo = objeto.total + objeto.cargo
        objeto.totalconpropinacargo = objeto.total + objeto.propina + objeto.cargo
        objeto.descuentoimporte = 0
        objeto.efectivo = objeto.total
        objeto.tarjeta = 0
        objeto.vales = 0
        objeto.otros = 0
        objeto.totalsindescuento = objeto.total
        objeto.totalalimentos = 0
        objeto.totalbebidas = 0
        objeto.totalotros = objeto.total
        objeto.totaldescuentos = 0 #Duda
        objeto.totaldescuentoalimentos = 0
        objeto.totaldescuentobebidas = 0
        objeto.totaldescuentootros = 0
        objeto.totalalimentossindescuentos = 0
        objeto.totalbebidasindescuentos = 0
        objeto.totalotrosindescuentos = objeto.total
        objeto.save()

        # Ahora actualiza los registros en Cheqdet
        for objeto in queryset:
            # Obtén los IDs de Cheqdet relacionados con el folio
            cheqdet_ids = list(Cheqdet.objects.filter(foliodet=objeto.folio).values_list('id', flat=True))

            if not cheqdet_ids:
                continue

            # Si hay más de un ID, elimina todos menos el primero
            if len(cheqdet_ids) > 1:
                ids_to_delete = cheqdet_ids[1:]  # Excluye el primero
                Cheqdet.objects.filter(id__in=ids_to_delete).delete()

            # Modifica el primer registro
            cheqdet = Cheqdet.objects.get(id=cheqdet_ids[0])
            cheqdet.cantidad = 1
            try:
                producto = Productos.objects.get(idproducto="V007021")
            except Productos.DoesNotExist:
                modeladmin.message_user(request, "El producto con id 'V007021' no existe.")
                return

            cheqdet.idproducto = producto
            cheqdet.descuento = 0
            cheqdet.precio = productos.precio * 2
            cheqdet.impuesto1 = productos.impuesto1 * 2
            cheqdet.preciosinimpuestos = productos.preciosinimpuestos * 2
            cheqdet.modificador = False
            cheqdet.comentario = ""
            cheqdet.usuariodescuento = ""
            cheqdet.comentariodescuento = ""
            cheqdet.comentario = ""
            cheqdet.idtipodescuento = ""
            cheqdet.preciocatalogo = productos.precio

            cheqdet.save()
    modeladmin.message_user(request, "El mantenimiento de la venta se hizo correctamente")

sustituir_producto_uno.short_description = "Sustituir por Café en grano 1/4"
sustituir_producto_dos.short_description = "Sustituir por Pan para llevar"
sustituir_producto_tres.short_description = "Sustituir por Cargas de café"

class TotalImpuesto1Filter(admin.SimpleListFilter):
    title = 'Impuesto' # Nombre que se mostrara en el filtro
    parameter_name = 'totalimpuesto1' # Nombre del parametro que se enviara por POST y GET (este campo es la columna en la base de datos)

    def lookups(self, request, model_admin):
        return ( # Devuelve una lista de tuplas
            ('0', 'Tasa 0'), # El primer valor es el valor que se enviara por POST y GET, el segundo valor es el que se mostrara en el filtro
            ('not_0', 'Tasa 16 efectivo'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(totalimpuesto1=0)
        elif self.value() == 'not_0':
            return queryset.exclude(totalimpuesto1=0).filter(efectivo__gt=0, tarjeta=0)
        return queryset

class ver_solo_cuentas_efectivo_no_facturadas_mayores_120(admin.SimpleListFilter):
    title = 'Tipos de cuentas' # Nombre que se mostrara en el filtro
    parameter_name = 'tipo_de_cuenta' # Identificador del filtro en la url

    def lookups(self, request, model_admin):
        return (
            ('efectivo_no_facturado', 'Cuentas en efectivo no facturadas mayores a $120'),
            ('cero', 'Cuentas en cero'),
            ('moficadas', 'Con mantenimiento de venta'),

        )

    def queryset(self, request, queryset):
        if self.value() == 'efectivo_no_facturado':
            return queryset.filter(efectivo__gt=120, tarjeta=0, facturado=False)
        elif self.value() == 'moficadas':
            return queryset.filter(facturado=False, mesa__icontains="P/LL")
        elif self.value() == 'cero':
            return queryset.filter(efectivo=0, tarjeta=0, total=0)

        return queryset


@admin.register(Cheques)
class ChequesAdmin(admin.ModelAdmin):
    list_filter = (TotalImpuesto1Filter, ver_solo_cuentas_efectivo_no_facturadas_mayores_120,)
    date_hierarchy = "fecha"
    search_fields = ("folio", "mesa", )
    list_display=("folio", "fecha", "mesa", "facturado", "totalarticulos", "subtotal", "total", "efectivo", "tarjeta", "totalimpuesto1" )
    actions = [sustituir_producto_uno, sustituir_producto_dos, sustituir_producto_tres,]

@admin.register(Cheqdet)
class CheqdetAdmin(admin.ModelAdmin):
    search_fields = ("foliodet",)
    list_display=("foliodet",)


admin.site.register(Productos)
admin.site.register(Productosdetalle)