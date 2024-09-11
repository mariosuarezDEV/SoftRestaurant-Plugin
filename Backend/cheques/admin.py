from itertools import product

from django.contrib import admin
from django.db import models
from django.db.models import F, Q
import datetime

from decimal import Decimal

from .forms import ChequesForm, ChequesdetForm

from rest_framework.authtoken.views import obtain_auth_token

#Configuracion de desarrollador
from .configuracion.developer_settings import ajustes_empresa

dev_conf = ajustes_empresa("034003", "042035", "V007021")

# Modelos de la app de cheques
from .models import Cheques, Cheqdet, Productos, Productosdetalle, cheques_proxy, chequedet_proxy


def sustituir_producto_uno(modeladmin, request, queryset):
    productos = Productosdetalle.objects.get(idproducto="034003")

    for objeto in queryset:  # Cambiar los cheques
        objeto.cierre = objeto.fecha + datetime.timedelta(minutes=3)
        objeto.mesa = "P/LL"
        objeto.nopersonas = 1
        objeto.cambio = 0
        objeto.descuento = 0
        objeto.usuariodescuento = ""
        objeto.idtipodescuento = ""
        objeto.tarjetadescuento = 0
        objeto.totalarticulos = 1
        objeto.subtotal = productos.precio
        objeto.total = productos.precio
        objeto.totalconpropina = productos.precio + objeto.propina
        objeto.totalimpuesto1 = 0  # Duda
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
        objeto.totaldescuentos = 0  # Duda
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
            cheqdet.idtipodescuento = ""
            cheqdet.preciocatalogo = productos.precio

            cheqdet.save()
    modeladmin.message_user(request, "El mantenimiento de la venta se hizo correctamente")


def sustituir_producto_dos(modeladmin, request, queryset):
    productos = Productosdetalle.objects.get(idproducto="042035")

    for objeto in queryset:  # Cambiar los cheques
        objeto.cierre = objeto.fecha + datetime.timedelta(minutes=3)
        objeto.mesa = "P/LL"
        objeto.nopersonas = 1
        objeto.cambio = 0
        objeto.descuento = 0
        objeto.usuariodescuento = ""
        objeto.idtipodescuento = ""
        objeto.tarjetadescuento = 0
        objeto.totalarticulos = 1
        objeto.subtotal = productos.precio
        objeto.total = productos.precio
        objeto.totalconpropina = productos.precio + objeto.propina
        objeto.totalimpuesto1 = 0  # Duda
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
        objeto.totaldescuentos = 0  # Duda
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

    for objeto in queryset:  # Cambiar los cheques
        objeto.cierre = objeto.fecha + datetime.timedelta(minutes=5)
        objeto.mesa = "P/LL"
        objeto.nopersonas = 1
        objeto.cambio = 0
        objeto.descuento = 0
        objeto.usuariodescuento = ""
        objeto.idtipodescuento = ""
        objeto.tarjetadescuento = 0
        objeto.totalarticulos = 2
        objeto.subtotal = productos.preciosinimpuestos * objeto.totalarticulos
        objeto.total = productos.precio * objeto.totalarticulos
        objeto.totalconpropina = objeto.total + objeto.propina
        objeto.totalimpuesto1 = (productos.precio * Decimal(0.16)) * objeto.totalarticulos
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
        objeto.totaldescuentos = 0  # Duda
        objeto.totaldescuentoalimentos = 0
        objeto.totaldescuentobebidas = 0
        objeto.totaldescuentootros = 0
        objeto.totalcortesias = 0
        objeto.totalcortesiaalimentos = 0
        objeto.totalcortesiabebidas = 0
        objeto.totalcortesiaotros = 0
        objeto.totalalimentossindescuentos = 0
        objeto.totalbebidasindescuentos = 0

        objeto.totaldescuentoycortesia = 0
        objeto.totalalimentossindescuentos = 0
        objeto.totalbebidassindescuentos = 0
        objeto.totalotrossindescuentos = 0
        objeto.descuentocriterios = 0

        objeto.totalotrosindescuentos = objeto.total
        objeto.desc_imp_original = 0
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
            cheqdet.cantidad = 2
            try:
                producto = Productos.objects.get(idproducto="V007021")
            except Productos.DoesNotExist:
                modeladmin.message_user(request, "El producto con id 'V007021' no existe.")
                return

            cheqdet.idproducto = producto
            cheqdet.descuento = 0
            cheqdet.precio = productos.precio * 2
            cheqdet.impuesto1 = (productos.precio * Decimal(0.16)) * 2
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


def sustituir_producto_cuatro(modeladmin, request, queryset):
    productos = Productosdetalle.objects.get(idproducto="13005")

    for objeto in queryset:  # Cambiar los cheques
        objeto.cierre = objeto.fecha + datetime.timedelta(minutes=5)
        objeto.mesa = "P/LL"
        objeto.nopersonas = 1
        objeto.cambio = 0
        objeto.descuento = 0
        objeto.usuariodescuento = ""
        objeto.idtipodescuento = ""
        objeto.tarjetadescuento = 0
        objeto.totalarticulos = 1
        objeto.subtotal = productos.preciosinimpuestos * objeto.totalarticulos
        objeto.total = productos.precio * objeto.totalarticulos
        objeto.totalconpropina = objeto.total + objeto.propina
        objeto.totalimpuesto1 = (productos.precio * Decimal(0.16)) * objeto.totalarticulos
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
        objeto.totaldescuentos = 0  # Duda
        objeto.totaldescuentoalimentos = 0
        objeto.totaldescuentobebidas = 0
        objeto.totaldescuentootros = 0
        objeto.totalcortesias = 0
        objeto.totalcortesiaalimentos = 0
        objeto.totalcortesiabebidas = 0
        objeto.totalcortesiaotros = 0
        objeto.totalalimentossindescuentos = 0
        objeto.totalbebidasindescuentos = 0

        objeto.totaldescuentoycortesia = 0
        objeto.totalalimentossindescuentos = 0
        objeto.totalbebidassindescuentos = 0
        objeto.totalotrossindescuentos = 0
        objeto.descuentocriterios = 0

        objeto.totalotrosindescuentos = objeto.total
        objeto.desc_imp_original = 0
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
            cheqdet.cantidad = 2
            try:
                producto = Productos.objects.get(idproducto="13005")
            except Productos.DoesNotExist:
                modeladmin.message_user(request, "El producto con id '13005' no existe.")
                return

            cheqdet.idproducto = producto
            cheqdet.descuento = 0
            cheqdet.precio = productos.precio
            cheqdet.impuesto1 = (productos.precio * Decimal(0.16))
            cheqdet.preciosinimpuestos = productos.preciosinimpuestos
            cheqdet.modificador = False
            cheqdet.comentario = ""
            cheqdet.usuariodescuento = ""
            cheqdet.comentariodescuento = ""
            cheqdet.comentario = ""
            cheqdet.idtipodescuento = ""
            cheqdet.preciocatalogo = productos.precio

            cheqdet.save()
    modeladmin.message_user(request, "El mantenimiento de la venta se hizo correctamente")


def mantenimiento_cheque(producto_id, cantidad, folio):
    #Obtener los detalles del cheque
    detalles = Cheqdet.objects.filter(foliodet=folio)
    # Eliminar todos los movimientos de los detalles menos el primero
    for detalle in detalles[1:]:
        detalle.delete()
    # Ahora modificar el primer detalle
    try:
        # Aquí se cambia la información del detalle
        detalles[0].idproducto = Productos.objects.get(idproducto=producto_id).idproducto
        detalles[0].descuento = 0
        detalles[0].precio = Productosdetalle.objects.get(idproducto=producto_id).precio
        detalles[0].impuesto1 = Productosdetalle.objects.get(idproducto=producto_id).impuesto1
        detalles[0].preciosinimpuestos = Productosdetalle.objects.get(idproducto=producto_id).preciosinimpuestos
        detalles[0].modificador = False
        detalles[0].comentario = ""
        detalles[0].usuariodescuento = ""
        detalles[0].comentariodescuento = ""
        detalles[0].idtipodescuento = ""
        detalles[0].preciocatalogo = Productosdetalle.objects.get(idproducto=producto_id).precio
        detalles[0].save()
        pass
    except Exception as e:
        return f"Error al modificar el detalle: {e}"


def configuracion_cheque(folio, precio, cantidad):
    #Obtener el cheque con el folio
    cheque = Cheques.objects.get(folio=folio)

    #Actualizar la informacion del cheque

    cheque.cambio = 0
    cheque.descuento = 0
    cheque.usuariodescuento = ""
    # Obtener la suma de la cantidad de todos los detalles
    cheque.totalarticulos = sum([detalle.cantidad for detalle in Cheqdet.objects.filter(foliodet=folio)])
    # Obtener la suma de todos los precios de los detalles
    cheque.subtotal = (sum([detalle.precio for detalle in
                            Cheqdet.objects.filter(foliodet=folio)])) / Decimal(1.16)
    cheque.total = sum([detalle.precio for detalle in Cheqdet.objects.filter(foliodet=folio)])
    cheque.totalconpropina = cheque.total + cheque.propina
    cheque.totalimpuesto1 = (sum([detalle.precio for detalle in
                                  Cheqdet.objects.filter(foliodet=folio)])) / Decimal(1.16) * Decimal(0.16)
    cheque.cargo = 0
    cheque.totalconcargo = cheque.total + cheque.cargo
    cheque.totalconpropinacargo = cheque.total + cheque.propina + cheque.cargo
    cheque.descuentoimporte = 0
    cheque.efectivo = cheque.total
    cheque.tarjeta = 0
    cheque.vales = 0
    cheque.otros = 0

    cheque.totalsindescuento = cheque.total
    cheque.totalbebidas = cheque.totalbebidas + (precio * cantidad)
    cheque.totaldescuentos = 0
    cheque.totaldescuentoalimentos = 0
    cheque.totaldescuentobebidas = 0
    cheque.totaldescuentootros = 0

    cheque.totalcortesias = 0
    cheque.totalcortesiaalimentos = 0
    cheque.totalcortesiabebidas = 0
    cheque.totalcortesiaotros = 0
    cheque.totaldescuentoycortesia = 0

    cheque.totalbebidassindescuentos = cheque.totalbebidas
    cheque.descuentocriterio = 0
    cheque.descuentomonedero = 0
    cheque.subtotalcondescuento = cheque.subtotal

    try:
        cheque.save()
        return f"La información del cheque {folio} se actualizó correctamente."
    except Exception as e:
        return f"Ocurrió un error al actualizar la información del cheque: {e}"


def sustituye_inversa(produto_id, cantidad, detalles, folio):
    try:
        producto = Productos.objects.get(idproducto=produto_id)
        p_d = Productosdetalle.objects.get(idproducto=produto_id)
    except Productos.DoesNotExist:
        print(f"El producto con id '{produto_id}' no existe.")
        return False

    for detalle in detalles:
        detalle.cantida = cantidad
        detalle.idproducto = Productos.objects.get(idproducto=produto_id)
        detalle.descuento = 0
        detalle.precio = p_d.precio
        detalle.impuesto1 = p_d.impuesto1
        detalle.preciosinimpuestos = p_d.preciosinimpuestos
        detalle.modficador = False
        detalle.mitad = False
        detalle.comentario = ""
        detalle.usuariodescuento = ""
        detalle.comentariodescuento = ""
        detalle.idtipodescuento = ""
        detalle.idproductocompuesto = ""
        detalle.productocompuestoprincipal = False
        detalle.preciocatalogo = p_d.precio
        detalle.idcortesia = 0
        try:
            detalle.save()
            # Ahora se debe ajiustar la información del cheque
            try:
                configuracion_cheque(folio, p_d.precio, cantidad)
            except Exception as e:
                return f"Error al guardar la configuración del cheque: {e} del folio {folio}"
        except models.Model.DoesNotExist as e:
            return f"Error al guardar el detalle: {e} del folio {detalle.foliodet}"

    return f'El producto {producto.descripcion} se sustituyó correctamente en el folio {folio}'


def sustituye_por_Botella_don_julio(modeladmin, request, queryset):
    for cheque in queryset:  # Recorrer cheqdet
        # Obtener los detalles del cheque (cuando movimiento sea igual a 1)
        detalles = Cheqdet.objects.filter(foliodet=cheque.folio, movimiento=1)
        restconf = sustituye_inversa("13005", 1, detalles, cheque.folio)
        if restconf:
            modeladmin.message_user(request, restconf)
        else:
            modeladmin.message_user(request, restconf)


def sustituye_por_cafe_en_grano(modeladmin, request, queryset):
    #Recibe los cheques a los que se les va a cambiar el producto
    for cheque in queryset:  # Recorrer los cheques
        # Aplicar el menteimiento al cheque
        mmnt = mantenimiento_cheque("034003", 1, cheque.folio)


sustituir_producto_uno.short_description = "Sustituir por Café en grano 1/4"
sustituir_producto_dos.short_description = "Sustituir por Pan para llevar"
sustituir_producto_tres.short_description = "Sustituir por Cargas de café"
sustituye_por_Botella_don_julio.short_description = "Sustituir por Botella Tequilia Don Julio 70 Aniversario"


def mantenimiento_detalles(producto_id, cantidad, folio, es_inverso):
    try:
        # Obtener la instancia del producto
        try:
            producto = Productos.objects.get(idproducto=producto_id)
        except Exception as e:
            return f"Error al obtener el producto: {e}"

        detalles = Cheqdet.objects.filter(foliodet=folio, movimiento=1).update(
            idproducto=producto,
            descuento=0,
            precio=Productosdetalle.objects.get(idproducto=producto_id).precio,
            impuesto1=0,
            preciosinimpuestos=Productosdetalle.objects.get(idproducto=producto_id).preciosinimpuestos,
            modificdor=False
        )
    except Exception as e:
        return f"Error al actualizar: {e}"


def mantenimiento_cheque(producto_id, cantidad, folio):
    pass


def test_producto_uno(modeladmin, request, queryset):
    # Obtener los cheques a los que se les hará el mantenimiento
    for cheques in queryset:
        # Emplezar por los detalles
        try:
            print(dev_conf.producto_uno)
            mantenimiento_detalles(dev_conf.get_producto_uno, 1, cheques.folio, False)
            modeladmin.message_user(request, f"El mantenimiento del cheque {cheques.folio} se hizo correctamente.")
        except Exception as e:
            modeladmin.message_user(request, f"Error al modificar los detalles: {e}")


test_producto_uno.short_description = "Sustituir por Café en grano 1/4 (testing)"


class TotalImpuesto1Filter(admin.SimpleListFilter):
    title = 'Impuesto'  # Nombre que se mostrara en el filtro
    parameter_name = 'totalimpuesto1'  # Nombre del parametro que se enviara por POST y GET (este campo es la columna en la base de datos)

    def lookups(self, request, model_admin):
        return (  # Devuelve una lista de tuplas
            ('0', 'Tasa 0'),
            # El primer valor es el valor que se enviara por POST y GET, el segundo valor es el que se mostrara en el filtro
            ('not_0', 'Tasa 16 efectivo'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(totalimpuesto1=0)
        elif self.value() == 'not_0':
            return queryset.exclude(totalimpuesto1=0).filter(efectivo__gt=0, tarjeta=0)
        return queryset


class ver_solo_cuentas_efectivo_no_facturadas_mayores_120(admin.SimpleListFilter):
    title = 'Tipos de cuentas'  # Nombre que se mostrara en el filtro
    parameter_name = 'tipo_de_cuenta'  # Identificador del filtro en la url

    def lookups(self, request, model_admin):
        return (
            ('efectivo_no_facturado', 'Cuentas en efectivo no facturadas mayores a $120'),
            ('cero', 'Cuentas en cero'),
            ('inversa', 'Cuentas en efectivo no facturadas menores a $300'),
            ('moficadas', 'Con mantenimiento de venta'),

        )

    def queryset(self, request, queryset):
        if self.value() == 'efectivo_no_facturado':
            return queryset.filter(efectivo__gt=120, tarjeta=0, facturado=False)
        elif self.value() == 'moficadas':
            return queryset.filter(facturado=False, mesa__icontains="P/LL")
        elif self.value() == 'cero':
            return queryset.filter(efectivo=0, tarjeta=0, total=0)
        elif self.value() == 'inversa':
            return queryset.filter(efectivo__lt=300, tarjeta=0, facturado=False)

        return queryset


@admin.register(cheques_proxy)
class ChequesAdminProxy(admin.ModelAdmin):
    form = ChequesForm
    list_filter = (TotalImpuesto1Filter, ver_solo_cuentas_efectivo_no_facturadas_mayores_120,)
    date_hierarchy = "fecha"
    search_fields = ("folio", "mesa",)
    list_display = ("folio", "fecha", "mesa", "facturado", "totalarticulos", "subtotal", "total", "efectivo", "tarjeta",
                    "totalimpuesto1")
    actions = [sustituir_producto_uno, sustituir_producto_dos, sustituir_producto_tres,
               sustituye_por_Botella_don_julio, ]  # admin1233


@admin.register(Cheques)
class ChequesAdmin(admin.ModelAdmin):
    list_filter = (TotalImpuesto1Filter, ver_solo_cuentas_efectivo_no_facturadas_mayores_120,)
    date_hierarchy = "fecha"
    search_fields = ("folio", "mesa",)
    list_display = ("folio", "fecha", "mesa", "facturado", "totalarticulos", "subtotal", "total", "efectivo", "tarjeta",
                    "totalimpuesto1")
    actions = [sustituir_producto_uno, sustituir_producto_dos, sustituir_producto_tres,
               sustituye_por_Botella_don_julio, test_producto_uno, ]


@admin.register(chequedet_proxy)
class CheqdetAdmin(admin.ModelAdmin):
    form = ChequesdetForm
    search_fields = ("foliodet",)
    list_display = ("foliodet", "cantidad", "idproducto", "precio", "impuesto1", "preciosinimpuestos")


@admin.register(Cheqdet)
class CheqdetAdmin(admin.ModelAdmin):
    search_fields = ("foliodet",)
    list_display = ("foliodet", "cantidad", "idproducto", "precio", "impuesto1", "preciosinimpuestos")


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    search_fields = ("idproducto", "descripcion",)
    list_display = ("idproducto", "descripcion",)


@admin.register(Productosdetalle)
class ProductosdetalleAdmin(admin.ModelAdmin):
    search_fields = ("idproducto",)
    list_display = ("idproducto", "precio", "impuesto1", "preciosinimpuestos",)
    list_filter = ("idproducto",)
