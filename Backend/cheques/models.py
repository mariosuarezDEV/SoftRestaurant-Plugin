# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Axclaves(models.Model):
    axid = models.CharField(db_column='AxId', max_length=50)  # Field name made lowercase.
    nsid = models.CharField(db_column='NsId', max_length=15)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo')  # Field name made lowercase.
    grupoimpuestos = models.CharField(db_column='GrupoImpuestos', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AxClaves'


class Axconfig(models.Model):
    baseuri = models.CharField(db_column='BaseUri', max_length=250)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=200)  # Field name made lowercase.
    apiversion = models.CharField(db_column='ApiVersion', max_length=50)  # Field name made lowercase.
    compannia = models.CharField(db_column='Compannia', max_length=50)  # Field name made lowercase.
    ultimadescarga = models.DateTimeField(db_column='UltimaDescarga')  # Field name made lowercase.
    intervalodescarga = models.IntegerField(db_column='IntervaloDescarga')  # Field name made lowercase.
    activo = models.BooleanField(db_column='Activo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AxConfig'


class Axlog(models.Model):
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    tipoevento = models.IntegerField(db_column='TipoEvento')  # Field name made lowercase.
    servicio = models.IntegerField(db_column='Servicio')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200)  # Field name made lowercase.
    detalles = models.CharField(db_column='Detalles', max_length=3500, blank=True, null=True)  # Field name made lowercase.
    folio = models.CharField(db_column='Folio', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idturno = models.IntegerField(blank=True, null=True)
    enviado = models.BooleanField(blank=True, null=True)
    status = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    foliointerno = models.BigIntegerField(blank=True, null=True)
    cargo = models.BooleanField()
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    propina = models.BooleanField()
    ordenventa = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    total_enviado = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    transaction_id = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AxLog'


class Axpendientes(models.Model):
    nsid = models.CharField(db_column='NsId', max_length=15)  # Field name made lowercase.
    intento = models.IntegerField(db_column='Intento')  # Field name made lowercase.
    idlog = models.ForeignKey(Axlog, models.DO_NOTHING, db_column='IdLog')  # Field name made lowercase.
    idturno = models.IntegerField(blank=True, null=True)
    numcheque = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    servicio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AxPendientes'


class Cancellationreason(models.Model):
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fkversioncontrolid = models.BigIntegerField(db_column='FKVersionControlId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CancellationReason'


class Cashmovementstype(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=5)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    idaccount = models.CharField(db_column='IdAccount', max_length=5, blank=True, null=True)  # Field name made lowercase.
    isenabled = models.BooleanField(db_column='IsEnabled')  # Field name made lowercase.
    idcashmovtypecourier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CashMovementsType'


class Clasificacion(models.Model):
    idclasificacion = models.CharField(db_column='Idclasificacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    desc_clasificacion = models.CharField(db_column='Desc_Clasificacion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clasificacion'


class Cloudworkspacesettings(models.Model):
    defaultpricelist = models.ForeignKey('Pricelists', models.DO_NOTHING, db_column='DefaultPriceList', blank=True, null=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='CompanyId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    authorizedapp = models.CharField(db_column='AuthorizedApp', max_length=36, blank=True, null=True)  # Field name made lowercase.
    downloadsales = models.BooleanField(db_column='DownloadSales')  # Field name made lowercase.
    idempresa = models.CharField(db_column='IdEmpresa', max_length=15, blank=True, null=True)  # Field name made lowercase.
    defaultproductsatid = models.CharField(db_column='DefaultProductSatId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servicemachinename = models.CharField(db_column='ServiceMachineName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CloudWorkspaceSettings'


class Configcashmovtype(models.Model):
    idcashmovtypegratuities = models.IntegerField(db_column='IdcashmovtypeGratuities', blank=True, null=True)  # Field name made lowercase.
    idcashmovtypeagents = models.IntegerField(db_column='IdcashmovtypeAgents', blank=True, null=True)  # Field name made lowercase.
    idcashmovtypemoneysafeguard = models.IntegerField(db_column='IdcashmovtypeMoneysafeguard', blank=True, null=True)  # Field name made lowercase.
    idcashmovtypecourier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ConfigCashMovType'


class Configuracionkiosco(models.Model):
    idempresa = models.CharField(db_column='IdEmpresa', primary_key=True, max_length=255)  # Field name made lowercase.
    usarcomeraqui = models.BooleanField(db_column='UsarComerAqui', blank=True, null=True)  # Field name made lowercase.
    usarparallevar = models.BooleanField(db_column='UsarParaLlevar', blank=True, null=True)  # Field name made lowercase.
    usarnumeromesa = models.BooleanField(db_column='UsarNumeroMesa', blank=True, null=True)  # Field name made lowercase.
    usarpagarencaja = models.BooleanField(db_column='UsarPagarEnCaja', blank=True, null=True)  # Field name made lowercase.
    usarpagaraqui = models.BooleanField(db_column='UsarPagarAqui', blank=True, null=True)  # Field name made lowercase.
    segundostransicioninicio = models.IntegerField(db_column='SegundosTransicionInicio')  # Field name made lowercase.
    segundostransicionpromocional = models.IntegerField(db_column='SegundosTransicionPromocional')  # Field name made lowercase.
    tipofondopantalla = models.IntegerField(db_column='TipoFondoPantalla')  # Field name made lowercase.
    colorfondo = models.CharField(db_column='ColorFondo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    colortexto = models.CharField(db_column='ColorTexto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desglosarproductosticketpagarcaja = models.BooleanField(db_column='DesglosarProductosTicketPagarCaja', blank=True, null=True)  # Field name made lowercase.
    imprimircomandapagarcaja = models.BooleanField(db_column='ImprimirComandaPagarCaja', blank=True, null=True)  # Field name made lowercase.
    tipotecladonumeromesa = models.IntegerField(db_column='TipoTecladoNumeroMesa')  # Field name made lowercase.
    tipotecladonumeroorden = models.IntegerField(db_column='TipoTecladoNumeroOrden')  # Field name made lowercase.
    usarnumeroorden = models.BooleanField(db_column='UsarNumeroOrden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfiguracionKiosco'


class Country(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    zipcodepattern = models.CharField(db_column='ZipCodePattern', max_length=100)  # Field name made lowercase.
    taxidpatter = models.CharField(db_column='TaxIdPatter', max_length=100)  # Field name made lowercase.
    taxidvalidation = models.CharField(db_column='TaxIdValidation', max_length=100)  # Field name made lowercase.
    alliances = models.CharField(db_column='Alliances', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'


class Currency(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    decimals = models.IntegerField(db_column='Decimals')  # Field name made lowercase.
    changepercent = models.DecimalField(db_column='ChangePercent', max_digits=16, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Currency'


class Erpconfig(models.Model):
    baseuri = models.CharField(db_column='BaseUri', max_length=250)  # Field name made lowercase.
    compania = models.CharField(db_column='Compania', max_length=250)  # Field name made lowercase.
    tiposervicio = models.IntegerField(blank=True, null=True)
    field_resource = models.CharField(db_column='_resource', max_length=250, blank=True, null=True)  # Field renamed because it started with '_'.
    content_type = models.CharField(db_column='Content_Type', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ERPConfig'


class ErpSettings(models.Model):
    idcatalogo = models.ForeignKey(Erpconfig, models.DO_NOTHING, db_column='Idcatalogo')  # Field name made lowercase.
    descripcion = models.CharField(max_length=250)
    keyconfig = models.CharField(max_length=250)
    valueconfig = models.CharField(max_length=350, blank=True, null=True)
    tipoconfiguracion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ERP_settings'


class FecolDatosfijos(models.Model):
    iddatosfijos = models.BigAutoField(db_column='IdDatosFijos', primary_key=True)  # Field name made lowercase.
    posicioneslayoutcarvajal = models.CharField(db_column='PosicionesLayoutCarvajal', max_length=100)  # Field name made lowercase.
    valor = models.TextField(db_column='Valor')  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numerogrupo = models.IntegerField(db_column='NumeroGrupo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FECol_DatosFijos'


class FecolDatosidentidad(models.Model):
    iddatosidentidad = models.BigAutoField(db_column='IdDatosIdentidad', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre')  # Field name made lowercase.
    empresa = models.TextField(db_column='Empresa')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100)  # Field name made lowercase.
    nit = models.CharField(db_column='Nit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountId', max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=100)  # Field name made lowercase.
    ciiu = models.CharField(db_column='CIIU', max_length=6)  # Field name made lowercase.
    actividad_economica = models.CharField(max_length=20)
    matricula = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'FECol_DatosIdentidad'


class FecolResultadoejecucion(models.Model):
    idresultadoejecucion = models.CharField(db_column='IdResultadoEjecucion', primary_key=True, max_length=36)  # Field name made lowercase.
    estadoenvio = models.CharField(db_column='EstadoEnvio', max_length=100, blank=True, null=True)  # Field name made lowercase.
    layoutcarvajal = models.TextField(db_column='LayoutCarvajal', blank=True, null=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='Respuesta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechaejecucion = models.DateTimeField(db_column='FechaEjecucion', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=512, blank=True, null=True)
    folio = models.CharField(db_column='Folio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mensajeerror = models.CharField(db_column='MensajeError', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FECol_ResultadoEjecucion'


class Factortype(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactorType'


class Functionsprofilesr(models.Model):
    code = models.CharField(primary_key=True, max_length=250)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FunctionsProfileSR'


class Horariocorte(models.Model):
    horainicial = models.CharField(max_length=11, blank=True, null=True)
    horafinal = models.CharField(max_length=11, blank=True, null=True)
    horaenvio = models.CharField(max_length=11, blank=True, null=True)
    diasiguiente = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HORARIOCORTE'


class Historialactualizaciones(models.Model):
    idanterior = models.CharField(db_column='IdAnterior', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idactual = models.CharField(db_column='IdActual', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idproducto = models.CharField(db_column='IdProducto', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idgrupo = models.CharField(db_column='IdGrupo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=250, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.DecimalField(db_column='Clasificacion', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perfil = models.CharField(db_column='Perfil', max_length=60, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciosinimpuestos = models.DecimalField(db_column='PrecioSinImpuestos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fondo = models.DecimalField(db_column='Fondo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    apertura = models.DateTimeField(db_column='Apertura', blank=True, null=True)  # Field name made lowercase.
    cierre = models.DateTimeField(db_column='Cierre', blank=True, null=True)  # Field name made lowercase.
    estacion = models.CharField(db_column='Estacion', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cajero = models.CharField(db_column='Cajero', max_length=15, blank=True, null=True)  # Field name made lowercase.
    efectivo = models.DecimalField(db_column='Efectivo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tarjeta = models.DecimalField(db_column='Tarjeta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vales = models.DecimalField(db_column='Vales', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    credito = models.DecimalField(db_column='Credito', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipooperacion = models.CharField(db_column='TipoOperacion', max_length=1)  # Field name made lowercase.
    entidad = models.CharField(db_column='Entidad', max_length=20)  # Field name made lowercase.
    fechaactualizacion = models.DateTimeField(db_column='FechaActualizacion', blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=6, decimal_places=2)  # Field name made lowercase.
    actualizado = models.BooleanField(db_column='Actualizado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistorialActualizaciones'


class Imageneskiosco(models.Model):
    idimagen = models.CharField(db_column='IdImagen', primary_key=True, max_length=36)  # Field name made lowercase.
    idempresa = models.CharField(db_column='IdEmpresa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imagen = models.TextField(db_column='Imagen', blank=True, null=True)  # Field name made lowercase.
    tipoimagen = models.IntegerField(db_column='TipoImagen', blank=True, null=True)  # Field name made lowercase.
    accionimagen = models.IntegerField(db_column='AccionImagen', blank=True, null=True)  # Field name made lowercase.
    accionidrelacionado = models.CharField(db_column='AccionIdRelacionado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    priorityorder = models.IntegerField(db_column='PriorityOrder', blank=True, null=True)  # Field name made lowercase.
    tipovisibilidad = models.IntegerField(db_column='TipoVisibilidad', blank=True, null=True)  # Field name made lowercase.
    aplicalunes = models.BooleanField(db_column='AplicaLunes', blank=True, null=True)  # Field name made lowercase.
    aplicamartes = models.BooleanField(db_column='AplicaMartes', blank=True, null=True)  # Field name made lowercase.
    aplicamiercoles = models.BooleanField(db_column='AplicaMiercoles', blank=True, null=True)  # Field name made lowercase.
    aplicajueves = models.BooleanField(db_column='AplicaJueves', blank=True, null=True)  # Field name made lowercase.
    aplicaviernes = models.BooleanField(db_column='AplicaViernes', blank=True, null=True)  # Field name made lowercase.
    aplicasabado = models.BooleanField(db_column='AplicaSabado', blank=True, null=True)  # Field name made lowercase.
    aplicadomingo = models.BooleanField(db_column='AplicaDomingo', blank=True, null=True)  # Field name made lowercase.
    lunesinicio = models.CharField(db_column='LunesInicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lunesfin = models.CharField(db_column='LunesFin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    martesinicio = models.CharField(db_column='MartesInicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    martesfin = models.CharField(db_column='MartesFin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    miercolesinicio = models.CharField(db_column='MiercolesInicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    miercolesfin = models.CharField(db_column='MiercolesFin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    juevesinicio = models.CharField(db_column='JuevesInicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    juevesfin = models.CharField(db_column='JuevesFin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    viernesinicio = models.CharField(db_column='ViernesInicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    viernesfin = models.CharField(db_column='ViernesFin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sabadoinicio = models.CharField(db_column='SabadoInicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sabadofin = models.CharField(db_column='SabadoFin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    domingoinicio = models.CharField(db_column='DomingoInicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    domingofin = models.CharField(db_column='DomingoFin', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImagenesKiosco'


class Mercadopagosettings(models.Model):
    idempresa = models.CharField(db_column='IdEmpresa', max_length=15, blank=True, null=True)  # Field name made lowercase.
    usemercadopagoqrsoftrestaurant = models.BooleanField(db_column='UseMercadoPagoQRSoftRestaurant', blank=True, null=True)  # Field name made lowercase.
    usemercadopagoqrcomandero = models.BooleanField(db_column='UseMercadoPagoQRComandero', blank=True, null=True)  # Field name made lowercase.
    usemercadopagoqrmenudigital = models.BooleanField(db_column='UseMercadoPagoQRMenuDigital', blank=True, null=True)  # Field name made lowercase.
    usemercadopagoqrkiosco = models.BooleanField(db_column='UseMercadoPagoQRKiosco', blank=True, null=True)  # Field name made lowercase.
    mercadopagostoreid = models.CharField(db_column='MercadoPagoStoreId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    defaultsrpaymentmethod = models.CharField(db_column='DefaultSRPaymentMethod', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MercadoPagoSettings'


class Modifierspricelists(models.Model):
    modifierpricelistid = models.CharField(db_column='ModifierPriceListId', primary_key=True, max_length=36)  # Field name made lowercase.
    fkidmodificador = models.ForeignKey('Productos', models.DO_NOTHING, db_column='FKidmodificador')  # Field name made lowercase.
    precio = models.DecimalField(max_digits=19, decimal_places=6)
    fkpricelist = models.ForeignKey('Pricelists', models.DO_NOTHING, db_column='FKPriceList')  # Field name made lowercase.
    fkidgrupomodificadoresproductos = models.ForeignKey('Gruposmodificadoresproductos', models.DO_NOTHING, db_column='FKidgrupomodificadoresproductos', to_field='workspaceid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModifiersPriceLists'


class Month(models.Model):
    code = models.CharField(db_column='Code', max_length=4, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fkversioncontrolid = models.BigIntegerField(db_column='FKVersionControlId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Month'


class Paymentmethod(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    isunbanked = models.IntegerField(db_column='IsUnbanked')  # Field name made lowercase.
    ismandatorytransactionnumber = models.IntegerField(db_column='IsMandatoryTransactionNumber')  # Field name made lowercase.
    originator_ismandatoryaccounttaxid = models.IntegerField(db_column='Originator_IsMandatoryAccountTaxId')  # Field name made lowercase.
    originator_ismandatoryaccount = models.IntegerField(db_column='Originator_IsMandatoryAccount')  # Field name made lowercase.
    originator_accountpattern = models.CharField(db_column='Originator_AccountPattern', max_length=100)  # Field name made lowercase.
    beneficiary_ismandatoryaccounttaxid = models.IntegerField(db_column='Beneficiary_IsMandatoryAccountTaxId')  # Field name made lowercase.
    beneficiary_ismandatoryaccount = models.IntegerField(db_column='Beneficiary_IsMandatoryAccount')  # Field name made lowercase.
    beneficiary_accountpattern = models.CharField(db_column='Beneficiary_AccountPattern', max_length=100)  # Field name made lowercase.
    ismandatorykindofpaymentstring = models.IntegerField(db_column='IsMandatoryKindofPaymentString')  # Field name made lowercase.
    ismandatoryforeignissuingbank = models.IntegerField(db_column='IsMandatoryForeignIssuingBank')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentMethod'


class Paymentmethodsrapp(models.Model):
    paymentmethodid = models.IntegerField(db_column='PaymentMethodId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statuspayment = models.BooleanField(db_column='StatusPayment', blank=True, null=True)  # Field name made lowercase.
    idformadepago = models.ForeignKey('Formasdepago', models.DO_NOTHING, db_column='idformadepago', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PaymentMethodSRAPP'


class Paymenttype(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentType'


class Periodicity(models.Model):
    code = models.CharField(db_column='Code', max_length=4, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fkversioncontrolid = models.BigIntegerField(db_column='FKVersionControlId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Periodicity'


class Pricelists(models.Model):
    pricelistid = models.CharField(db_column='PriceListId', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isenabled = models.BooleanField(db_column='IsEnabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriceLists'


class Product(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    hastransferredtax = models.IntegerField(db_column='HasTransferredTax')  # Field name made lowercase.
    hastransferredieps = models.IntegerField(db_column='HasTransferredIEPS')  # Field name made lowercase.
    complement = models.CharField(db_column='Complement', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Productpricelists(models.Model):
    productpricelistid = models.CharField(db_column='ProductPriceListId', primary_key=True, max_length=36)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=19, decimal_places=6)  # Field name made lowercase.
    isopenprice = models.BooleanField(db_column='IsOpenPrice')  # Field name made lowercase.
    isuse = models.BooleanField(db_column='isUse')  # Field name made lowercase.
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto')
    fkpricelist = models.ForeignKey(Pricelists, models.DO_NOTHING, db_column='FKPriceList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductPriceLists'


class Productosagruparconfig(models.Model):
    productosagruparconfigid = models.AutoField(db_column='ProductosAgruparConfigID', primary_key=True)  # Field name made lowercase.
    fkidproductoprincipal = models.ForeignKey('Productos', models.DO_NOTHING, db_column='FKidproductoPrincipal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductosAgruparConfig'


class Productosequivalenciasconfig(models.Model):
    productosequivalenciasconfigid = models.AutoField(db_column='ProductosEquivalenciasConfigID', primary_key=True)  # Field name made lowercase.
    fkproductosagruparconfig = models.ForeignKey(Productosagruparconfig, models.DO_NOTHING, db_column='FKProductosAgruparConfig')  # Field name made lowercase.
    fkidproductoequivalente = models.ForeignKey('Productos', models.DO_NOTHING, db_column='FKidproductoEquivalente')  # Field name made lowercase.
    equivalencia = models.DecimalField(max_digits=10, decimal_places=6)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductosEquivalenciasConfig'


class Prooftype(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    maxvalue = models.DecimalField(db_column='MaxValue', max_digits=16, decimal_places=6)  # Field name made lowercase.
    maxvaluends = models.DecimalField(db_column='MaxValueNdS', max_digits=16, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProofType'


class Proofuse(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    isusedbylegalperson = models.BooleanField(db_column='IsUsedByLegalPerson')  # Field name made lowercase.
    isusedbylegalentity = models.BooleanField(db_column='IsUsedByLegalEntity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProofUse'


class Relationshiptype(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelationshipType'


class Salesareapricelist(models.Model):
    salesareapricelistid = models.CharField(db_column='SalesAreaPriceListId', max_length=36)  # Field name made lowercase.
    fkidarearestaurant = models.ForeignKey('Areasrestaurant', models.DO_NOTHING, db_column='FKIdarearestaurant')  # Field name made lowercase.
    fkpricelist = models.ForeignKey(Pricelists, models.DO_NOTHING, db_column='FKPriceList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesAreaPriceList'


class Serviceworkspacesettings(models.Model):
    service = models.IntegerField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.CharField(db_column='IdEmpresa', max_length=15, blank=True, null=True)  # Field name made lowercase.
    updateminutes = models.IntegerField(db_column='UpdateMinutes')  # Field name made lowercase.
    limitsyncschedule = models.BooleanField(db_column='LimitSyncSchedule')  # Field name made lowercase.
    schedulestarttime = models.TimeField(db_column='ScheduleStartTime', blank=True, null=True)  # Field name made lowercase.
    scheduleendtime = models.TimeField(db_column='ScheduleEndTime', blank=True, null=True)  # Field name made lowercase.
    limitsyncday = models.BooleanField(db_column='LimitSyncDay')  # Field name made lowercase.
    syncmonday = models.BooleanField(db_column='SyncMonday')  # Field name made lowercase.
    synctuesday = models.BooleanField(db_column='SyncTuesday')  # Field name made lowercase.
    syncwednesday = models.BooleanField(db_column='SyncWednesday')  # Field name made lowercase.
    syncthursday = models.BooleanField(db_column='SyncThursday')  # Field name made lowercase.
    syncfriday = models.BooleanField(db_column='SyncFriday')  # Field name made lowercase.
    syncsaturday = models.BooleanField(db_column='SyncSaturday')  # Field name made lowercase.
    syncsunday = models.BooleanField(db_column='SyncSunday')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    application = models.IntegerField(db_column='Application')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceWorkspaceSettings'


class Synclog(models.Model):
    machinename = models.CharField(db_column='MachineName', max_length=50)  # Field name made lowercase.
    logged = models.CharField(db_column='Logged', max_length=100)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=50)  # Field name made lowercase.
    message = models.TextField(db_column='Message')  # Field name made lowercase.
    logger = models.CharField(db_column='Logger', max_length=250, blank=True, null=True)  # Field name made lowercase.
    exception = models.TextField(db_column='Exception', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SyncLog'


class Syncronizationcontrol(models.Model):
    syncronizationcontrolid = models.CharField(db_column='SyncronizationControlId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='CompanyId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isconfiguration = models.BooleanField(db_column='IsConfiguration', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=70, blank=True, null=True)  # Field name made lowercase.
    ismigration = models.BooleanField(db_column='IsMigration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SyncronizationControl'


class Tax(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    iswithholdingtax = models.BooleanField(db_column='IsWithholdingTax')  # Field name made lowercase.
    istransferredtax = models.BooleanField(db_column='IsTransferredTax')  # Field name made lowercase.
    isfederaltax = models.BooleanField(db_column='IsFederalTax')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tax'


class Taxrate(models.Model):
    isfixed = models.BooleanField(db_column='IsFixed')  # Field name made lowercase.
    israte = models.BooleanField(db_column='IsRate')  # Field name made lowercase.
    istransferredtax = models.BooleanField(db_column='IsTransferredTax')  # Field name made lowercase.
    iswithholdingtax = models.BooleanField(db_column='IsWithholdingTax')  # Field name made lowercase.
    maxvalue = models.DecimalField(db_column='MaxValue', max_digits=16, decimal_places=6)  # Field name made lowercase.
    minvalue = models.DecimalField(db_column='MinValue', max_digits=16, decimal_places=6)  # Field name made lowercase.
    factortype = models.CharField(db_column='FactorType', max_length=50)  # Field name made lowercase.
    tax = models.CharField(db_column='Tax', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxRate'


class Taxregime(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    isusedbylegalperson = models.BooleanField(db_column='IsUsedByLegalPerson')  # Field name made lowercase.
    isusedbylegalentity = models.BooleanField(db_column='IsUsedByLegalEntity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxRegime'


class Taxsubject(models.Model):
    code = models.CharField(db_column='Code', max_length=4, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fkversioncontrolid = models.BigIntegerField(db_column='FKVersionControlId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxSubject'


class Unitofmeasure(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnitOfMeasure'


class Visibilidadareaparaventa(models.Model):
    fkidtiposervicio = models.DecimalField(db_column='FKidtiposervicio', max_digits=1, decimal_places=0)  # Field name made lowercase.
    fkidarearestaurant = models.ForeignKey('Areasrestaurant', models.DO_NOTHING, db_column='FKidarearestaurant')  # Field name made lowercase.
    fkapp = models.ForeignKey('AppList', models.DO_NOTHING, db_column='FKapp_id', to_field='app_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisibilidadAreaParaVenta'


class Workspacecontrol(models.Model):
    idsoftrestaurant = models.CharField(db_column='IdSoftrestaurant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workspaceid = models.CharField(db_column='WorkSpaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    forsync = models.BooleanField(db_column='ForSync', blank=True, null=True)  # Field name made lowercase.
    datecreate = models.DateTimeField(db_column='DateCreate', blank=True, null=True)  # Field name made lowercase.
    datesync = models.DateTimeField(db_column='DateSync', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.
    datedelete = models.DateTimeField(db_column='DateDelete', blank=True, null=True)  # Field name made lowercase.
    datedeleteworkspace = models.DateTimeField(db_column='DateDeleteWorkspace', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkspaceControl'


class Actualizaciones(models.Model):
    sistema = models.CharField(max_length=250, blank=True, null=True)
    zip = models.BinaryField(blank=True, null=True)
    fecha = models.CharField(max_length=250, blank=True, null=True)
    cambios = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'actualizaciones'


class Actualizacionsucursales(models.Model):
    idempresa = models.CharField(max_length=15)
    fecharev = models.CharField(max_length=10, blank=True, null=True)
    permitiractualizar = models.BooleanField()
    programarhoractualizacion = models.BooleanField()
    horactualizacion = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'actualizacionsucursales'


class Acumuladoinsumos(models.Model):
    idinsumo = models.ForeignKey('Insumos', models.DO_NOTHING, db_column='idinsumo')
    idalmacen = models.ForeignKey('Almacen', models.DO_NOTHING, db_column='idalmacen')
    existencia = models.DecimalField(max_digits=14, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'acumuladoinsumos'


class Alertasantifraude(models.Model):
    fecha = models.DateTimeField()
    turno = models.BigIntegerField(blank=True, null=True)
    tipoalerta = models.IntegerField(blank=True, null=True)
    cantidadmax = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    valormaximo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    enviado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alertasantifraude'


class Almacen(models.Model):
    idalmacen = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    ultimofolio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    idempresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'almacen'


class AppList(models.Model):
    app_id = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_list'


class AppSettings(models.Model):
    app = models.ForeignKey(AppList, models.DO_NOTHING, to_field='app_id')
    field = models.CharField(max_length=100)
    field_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'app_settings'


class Areas(models.Model):
    idarea = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areas'


class Areasdetalle(models.Model):
    idarea = models.ForeignKey(Areas, models.DO_NOTHING, db_column='idarea')
    idempresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    descargar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areasdetalle'


class Areasrestaurant(models.Model):
    idarearestaurant = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    idtiposervicio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idareasr = models.AutoField(db_column='idAreaSR', primary_key=True) # Field name made lowercase.
    estatus = models.BooleanField(db_column='Estatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areasrestaurant'


class Areasrestaurantdetalle(models.Model):
    idarearestaurant = models.ForeignKey(Areasrestaurant, models.DO_NOTHING, db_column='idarearestaurant', blank=True, null=True)
    idempresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    descargar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areasrestaurantdetalle'


class AzbarLog(models.Model):
    idazbarlog = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    idturno = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    usuario = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    activetable = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'azbar_log'


class Bancos(models.Model):
    idbanco = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bancos'


class Bitacoraenvioventas(models.Model):
    idbitacora = models.BigAutoField(primary_key=True)
    fechaapertura = models.DateTimeField(blank=True, null=True)
    enviado = models.BooleanField(blank=True, null=True)
    fechaenviado = models.DateTimeField(blank=True, null=True)
    usuarioenvio = models.CharField(max_length=30, blank=True, null=True)
    offline = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacoraEnvioVentas'


class Bitacoraarchivopoliza(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacoraarchivopoliza'


class Bitacoracedixvirtual(models.Model):
    idbitacoracedix = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    numcheque = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    plataforma = models.CharField(max_length=20, blank=True, null=True)
    carrierid = models.CharField(max_length=5, blank=True, null=True)
    carriername = models.CharField(max_length=50, blank=True, null=True)
    productid = models.CharField(max_length=5, blank=True, null=True)
    productname = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    telefonoabonado = models.CharField(max_length=20, blank=True, null=True)
    transactionid = models.CharField(max_length=10, blank=True, null=True)
    aditionalinfo1 = models.CharField(max_length=100, blank=True, null=True)
    aditionalinfo2 = models.CharField(max_length=100, blank=True, null=True)
    aditionalinfo3 = models.CharField(max_length=100, blank=True, null=True)
    providerauthorization = models.CharField(max_length=50, blank=True, null=True)
    responsecode = models.CharField(max_length=10, blank=True, null=True)
    responsemessage = models.CharField(max_length=100, blank=True, null=True)
    legalinformation = models.TextField(blank=True, null=True)  # This field type is a guess.
    iniciooperacion = models.CharField(max_length=25, blank=True, null=True)
    finoperacion = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacoracedixvirtual'


class Bitacoracierresinventario(models.Model):
    mes = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    anio = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacoracierresinventario'


class Bitacoraeasygoband(models.Model):
    idbitacora = models.BigAutoField(primary_key=True)
    folio = models.BigIntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    idformadepago = models.CharField(max_length=5)
    servicecode = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=14, decimal_places=4)
    type = models.CharField(max_length=50)
    accountid = models.CharField(max_length=250)
    transactionid = models.CharField(max_length=250)
    guestid = models.CharField(max_length=250)
    transactionid_cancelled = models.CharField(max_length=250)
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4)
    exchange_currency_id = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'bitacoraeasygoband'


class Bitacorafiscal(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    fechainicial = models.DateTimeField(blank=True, null=True)
    fechafinal = models.DateTimeField(blank=True, null=True)
    cuentastotal = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    cuentasmodificadas = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    importeanterior = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    importenuevo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=10, blank=True, null=True)
    modificaventareal = models.BooleanField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacorafiscal'


class Bitacorasistema(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=60, blank=True, null=True)
    evento = models.CharField(max_length=50, blank=True, null=True)
    valores = models.CharField(max_length=254, blank=True, null=True)
    estacion = models.CharField(max_length=40, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    numcheque = models.BigIntegerField(blank=True, null=True)
    usuariosolicita = models.CharField(max_length=100, blank=True, null=True)
    tipoalerta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bitacorasistema'


class Bitacoratarjetacredito(models.Model):
    folio = models.BigIntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=15, blank=True, null=True)
    cuenta = models.CharField(max_length=20, blank=True, null=True)
    vencimiento = models.CharField(max_length=4, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    reimpresiones = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    mensajederespuesta = models.CharField(max_length=250, blank=True, null=True)
    procedimiento = models.CharField(max_length=20, blank=True, null=True)
    afiliacion = models.CharField(max_length=20, blank=True, null=True)
    statustransaccion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idtransaccion = models.CharField(max_length=30, blank=True, null=True)
    numerooperacion = models.CharField(max_length=10, blank=True, null=True)
    informaciontarjeta = models.CharField(max_length=100, blank=True, null=True)
    tipotarjeta = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    arqc = models.CharField(max_length=30, blank=True, null=True)
    apn = models.CharField(max_length=30, blank=True, null=True)
    apnlabel = models.CharField(max_length=30, blank=True, null=True)
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)
    transactiontype = models.CharField(max_length=50)
    applicationcryptogram = models.CharField(max_length=50)
    entrymethod = models.CharField(max_length=50)
    approvalcode = models.CharField(max_length=50)
    paymenttype = models.CharField(max_length=50)
    cardholderverificationmethod = models.SmallIntegerField()
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    marcatarjeta = models.CharField(max_length=100, blank=True, null=True)
    banco = models.CharField(max_length=100, blank=True, null=True)
    terminal = models.CharField(max_length=100, blank=True, null=True)
    foliokiosko = models.CharField(max_length=50, blank=True, null=True)
    tempnumcheque = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    referenciacomercio = models.CharField(max_length=25, blank=True, null=True)
    puntosredimidos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puntospesosredimidos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    saldodisponiblepuntos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    saldodisponiblepesos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    saldoanteriorpuntos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    saldoanteriorpesos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacoratarjetacredito'


class Bitacoratransacciones(models.Model):
    folio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    autorizacion = models.CharField(max_length=15, blank=True, null=True)
    referencia = models.CharField(max_length=15, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    reimpresiones = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    procedimiento = models.CharField(max_length=15, blank=True, null=True)
    datosenvio = models.CharField(max_length=254, blank=True, null=True)
    datosrespuesta = models.CharField(max_length=254, blank=True, null=True)
    medusafol_prov = models.CharField(max_length=15, blank=True, null=True)
    medusafol_ope = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacoratransacciones'


class Botonescomandero(models.Model):
    etiqueta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    descripcion = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    imagen = models.CharField(max_length=100, blank=True, null=True)
    posicion = models.IntegerField(blank=True, null=True)
    tiempo = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'botonescomandero'


class Cajones(models.Model):
    cajonactivo = models.BooleanField(blank=True, null=True)
    cajonascii = models.CharField(max_length=20, blank=True, null=True)
    cajonpuerto = models.IntegerField(blank=True, null=True)
    cajontipo = models.IntegerField(blank=True, null=True)
    cajontiempo = models.IntegerField(blank=True, null=True)
    cajonimpresora = models.CharField(max_length=50, blank=True, null=True)
    cajontipoconexion = models.IntegerField(blank=True, null=True)
    cajacomandero = models.CharField(max_length=80, blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    idestacion = models.CharField(max_length=40)
    nocajon = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    cajonenuso = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cajones'


class Cancela(models.Model):
    foliocheque = models.BigIntegerField()
    comanda = models.CharField(max_length=8, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    clave = models.CharField(max_length=15, blank=True, null=True)
    razon = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idmotivocancela = models.TextField(blank=True, null=True)  # This field type is a guess.
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancela'


class Cargosareas(models.Model):
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto')
    idarearestaurant = models.ForeignKey(Areasrestaurant, models.DO_NOTHING, db_column='idarearestaurant')

    class Meta:
        managed = False
        db_table = 'cargosareas'


class Carrierproducts(models.Model):
    carrierid = models.ForeignKey('Carriers', models.DO_NOTHING, db_column='carrierid', blank=True, null=True)
    productid = models.CharField(max_length=5, blank=True, null=True)
    productname = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    productoinfo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'carrierproducts'


class Carriers(models.Model):
    carrierid = models.CharField(primary_key=True, max_length=5)
    carriername = models.CharField(max_length=50, blank=True, null=True)
    plataforma = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carriers'


class Cfdirelacionados(models.Model):
    idfactura = models.DecimalField(max_digits=10, decimal_places=0)
    uuid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cfdirelacionados'


class Cheqdet(models.Model):
    foliodet = models.BigIntegerField(blank=True)
    movimiento = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    comanda = models.CharField(max_length=8, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    preciosinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tiempo = models.CharField(max_length=20, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    modificador = models.BooleanField(blank=True, null=True)
    mitad = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    idestacion = models.CharField(max_length=40, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    horaproduccion = models.DateTimeField(blank=True, null=True)
    idproductocompuesto = models.CharField(max_length=15, blank=True, null=True)
    productocompuestoprincipal = models.BooleanField(blank=True, null=True)
    preciocatalogo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    marcar = models.BooleanField(blank=True, null=True)
    idmeseroproducto = models.CharField(max_length=4, blank=True, null=True)
    prioridadproduccion = models.CharField(max_length=1, blank=True, null=True)
    estatuspatin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idcortesia = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=16, blank=True, null=True)
    estadomonitor = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    llavemovto = models.CharField(max_length=100, blank=True, null=True)
    horameserofinalizado = models.DateTimeField(blank=True, null=True)
    meserofinalizado = models.CharField(max_length=4, blank=True, null=True)
    sistema_envio = models.IntegerField()
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)
    promovolumen = models.BooleanField()
    iddispositivo = models.IntegerField()
    productsyncidsr = models.IntegerField()
    subtotalsrx = models.DecimalField(max_digits=7, decimal_places=5)
    totalsrx = models.DecimalField(max_digits=7, decimal_places=5)
    idmovtobillar = models.BigIntegerField()
    idlistaprecio = models.IntegerField(blank=True, null=True)

    # Duda
    tipocambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuestoimporte3 = models.DecimalField(max_digits=19, decimal_places=4)
    estrateca_discountcode = models.CharField(db_column='estrateca_DiscountCode', max_length=50)  # Field name made lowercase.
    estrateca_discountid = models.CharField(db_column='estrateca_DiscountID', max_length=50)  # Field name made lowercase.
    estrateca_discountamount = models.DecimalField(db_column='estrateca_DiscountAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    saledetailid = models.CharField(max_length=250, blank=True, null=True)
    preciosinimpuestos_ec = models.BinaryField(blank=True, null=True)
    precio_ec = models.BinaryField(blank=True, null=True)
    escargoarea = models.BooleanField()
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cheqdet'
        verbose_name = 'Detalle del Cheque'
        verbose_name_plural = 'Detalles del Cheque'

class Cheqdetf(models.Model):
    foliodet = models.BigIntegerField(blank=True, null=True)
    movimiento = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    comanda = models.CharField(max_length=8, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    preciosinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tiempo = models.CharField(max_length=20, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    modificador = models.BooleanField(blank=True, null=True)
    mitad = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    idestacion = models.CharField(max_length=40, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    horaproduccion = models.DateTimeField(blank=True, null=True)
    idproductocompuesto = models.CharField(max_length=15, blank=True, null=True)
    productocompuestoprincipal = models.BooleanField(blank=True, null=True)
    preciocatalogo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    marcar = models.BooleanField(blank=True, null=True)
    idmeseroproducto = models.CharField(max_length=4, blank=True, null=True)
    prioridadproduccion = models.CharField(max_length=1, blank=True, null=True)
    estatuspatin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idcortesia = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=16, blank=True, null=True)
    llavemovto = models.CharField(max_length=100, blank=True, null=True)
    idmovtobillar = models.BigIntegerField()
    estrateca_discountcode = models.CharField(db_column='estrateca_DiscountCode', max_length=50)  # Field name made lowercase.
    estrateca_discountid = models.CharField(db_column='estrateca_DiscountID', max_length=50)  # Field name made lowercase.
    estrateca_discountamount = models.DecimalField(db_column='estrateca_DiscountAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preciosinimpuestos_ec = models.BinaryField(blank=True, null=True)
    precio_ec = models.BinaryField(blank=True, null=True)
    escargoarea = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cheqdetf'


class Cheqdetfeliminados(models.Model):
    foliodet = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheqdetfeliminados'


class Cheqerp(models.Model):
    folio = models.BigIntegerField(primary_key=True)  # The composite primary key (folio, WorkspaceId) found, that is not supported. The first column is selected.
    enviado = models.BooleanField()
    cancelado = models.BooleanField()
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36)  # Field name made lowercase.
    transaction_id = models.CharField(max_length=250, blank=True, null=True)
    transaction_id_cancelled = models.CharField(max_length=250, blank=True, null=True)
    tipo_servicio = models.IntegerField(blank=True, null=True)
    propina = models.BooleanField(blank=True, null=True)
    detalles = models.CharField(max_length=3500, blank=True, null=True)
    fechaenvio = models.DateTimeField(blank=True, null=True)
    estacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheqerp'
        unique_together = (('folio', 'workspaceid'),)


class Cheqpedidos(models.Model):
    foliocheque = models.BigIntegerField(blank=True, null=True)
    idpedido = models.BigIntegerField(blank=True, null=True)
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheqpedidos'


class Cheques(models.Model):
    folio = models.BigAutoField(primary_key=True)
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    numcheque = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    salidarepartidor = models.DateTimeField(blank=True, null=True)
    arriborepartidor = models.DateTimeField(blank=True, null=True)
    cierre = models.DateTimeField(blank=True, null=True)
    mesa = models.CharField(max_length=100, blank=True, null=True)
    nopersonas = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    idmesero = models.CharField(max_length=4, blank=True, null=True)
    pagado = models.BooleanField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    impreso = models.BooleanField(blank=True, null=True)
    # Duda
    impresiones = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    cambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    #Duda
    reabiertas = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    razoncancelado = models.CharField(max_length=255, blank=True, null=True)
    orden = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    facturado = models.BooleanField(blank=True, null=True)
    idcliente = models.CharField(max_length=15, blank=True, null=True)
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    tipodeservicio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idturno = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    estacion = models.CharField(max_length=40, blank=True, null=True)
    cambiorepartidor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    fechacancelado = models.DateTimeField(blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=30, blank=True, null=True)
    folionotadeconsumo = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    notadeconsumo = models.BooleanField(blank=True, null=True)
    #Duda
    propinapagada = models.BooleanField(blank=True, null=True)
    propinafoliomovtocaja = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)

    puntosmonederogenerados = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propinaincluida = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjetadescuento = models.CharField(max_length=30, blank=True, null=True)
    porcentajefac = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    usuariopago = models.CharField(max_length=15, blank=True, null=True)
    #Duda
    propinamanual = models.BooleanField(blank=True, null=True)

    observaciones = models.CharField(max_length=250, blank=True, null=True)
    idclientedomicilio = models.CharField(max_length=15, blank=True, null=True)
    iddireccion = models.CharField(max_length=15, blank=True, null=True)
    idclientefacturacion = models.CharField(max_length=15, blank=True, null=True)
    telefonousadodomicilio = models.CharField(max_length=50, blank=True, null=True)
    totalarticulos = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    subtotalsinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    totalconpropina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    totalimpuesto1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    # Duda
    totalconcargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconpropinacargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentoimporte = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    efectivo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    otros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    #Duda
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propinatarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    campoadicional1 = models.CharField(max_length=250, blank=True, null=True)
    idreservacion = models.CharField(max_length=25, blank=True, null=True)
    idcomisionista = models.CharField(max_length=15, blank=True, null=True)
    importecomision = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    comisionpagada = models.BooleanField(blank=True, null=True)
    fechapagocomision = models.DateTimeField(blank=True, null=True)
    foliopagocomision = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    tipoventarapida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    callcenter = models.BooleanField(blank=True, null=True)
    idordencompra = models.BigIntegerField(blank=True, null=True)

    totalsindescuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalotros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentoalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentobebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentootros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    #Duda
    totalcortesias = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiaalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiabebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiaotros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentoycortesia = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalalimentossindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbebidassindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalotrossindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentocriterio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    descuentomonedero = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idmenucomedor = models.CharField(max_length=15, blank=True, null=True)
    subtotalcondescuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    comisionpax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    procesadointerfaz = models.BooleanField(blank=True, null=True)
    domicilioprogramado = models.BooleanField(blank=True, null=True)
    fechadomicilioprogramado = models.DateTimeField(blank=True, null=True)
    enviado = models.BooleanField(blank=True, null=True)
    ncf = models.CharField(max_length=19, blank=True, null=True)
    numerocuenta = models.CharField(max_length=100, blank=True, null=True)
    codigo_unico_af = models.CharField(max_length=30, blank=True, null=True)
    estatushub = models.IntegerField(blank=True, null=True)
    idfoliohub = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    enviadorw = models.BooleanField(db_column='EnviadoRW', blank=True, null=True)  # Field name made lowercase.
    usuarioapertura = models.CharField(max_length=15)
    titulartarjetamonedero = models.CharField(max_length=100, blank=True, null=True)
    saldoanteriormonedero = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    autorizacionfolio = models.CharField(max_length=50, blank=True, null=True)
    fechalimiteemision = models.DateTimeField(blank=True, null=True)
    totalimpuestod1 = models.DecimalField(max_digits=19, decimal_places=4)
    totalimpuestod2 = models.DecimalField(max_digits=19, decimal_places=4)
    totalimpuestod3 = models.DecimalField(max_digits=19, decimal_places=4)
    idmotivocancela = models.CharField(max_length=200, blank=True, null=True)
    sistema_envio = models.IntegerField()
    idformadepagodescuento = models.CharField(db_column='idformadepagoDescuento', max_length=5)  # Field name made lowercase.
    titulartarjetamonederodescuento = models.CharField(max_length=100)
    foliotempcheques = models.BigIntegerField(blank=True, null=True)
    c_iddispositivo = models.IntegerField()
    salerestaurantid = models.TextField()
    timemarktoconfirmed = models.DateTimeField(blank=True, null=True)
    timemarktodelivery = models.DateTimeField(blank=True, null=True)
    timemarktodeliveryarrive = models.DateTimeField(blank=True, null=True)
    esalestatus = models.IntegerField()
    statussr = models.IntegerField(db_column='statusSR')  # Field name made lowercase.
    paymentreference = models.CharField(max_length=50)
    deliverycharge = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)
    comandaimpresa = models.BooleanField(blank=True, null=True)
    foodorder = models.IntegerField()
    cashpaymentwith = models.DecimalField(max_digits=19, decimal_places=4)
    paymentmethod_id = models.IntegerField()
    surveycode = models.CharField(max_length=18)
    intentoenvioaf = models.IntegerField(db_column='intentoEnvioAF')  # Field name made lowercase.
    tkc_token = models.CharField(db_column='TKC_Token', max_length=50)  # Field name made lowercase.
    tkc_transaction = models.CharField(db_column='TKC_Transaction', max_length=100)  # Field name made lowercase.
    tkc_authorization = models.CharField(db_column='TKC_Authorization', max_length=100)  # Field name made lowercase.
    tkc_cupon = models.CharField(db_column='TKC_Cupon', max_length=100)  # Field name made lowercase.
    tkc_expirationdate = models.CharField(db_column='TKC_ExpirationDate', max_length=100)  # Field name made lowercase.
    tkc_recompensa = models.DecimalField(db_column='TKC_Recompensa', max_digits=19, decimal_places=4)  # Field name made lowercase.
    campoadicional2 = models.CharField(max_length=250)
    campoadicional3 = models.CharField(max_length=250)
    estrateca_cardnumber = models.CharField(db_column='estrateca_CardNumber', max_length=100)  # Field name made lowercase.
    estrateca_vouchertext = models.TextField(db_column='estrateca_VoucherText')  # Field name made lowercase.
    campoadicional4 = models.CharField(max_length=250)
    campoadicional5 = models.CharField(max_length=250)
    sacoa_cardnumber = models.CharField(db_column='sacoa_CardNumber', max_length=100)  # Field name made lowercase.
    sacoa_credits = models.DecimalField(max_digits=19, decimal_places=4)
    estrateca_typedisccount = models.CharField(db_column='estrateca_TypeDisccount', max_length=50)  # Field name made lowercase.
    estrateca_discountcode = models.CharField(db_column='estrateca_DiscountCode', max_length=50)  # Field name made lowercase.
    estrateca_discountid = models.CharField(db_column='estrateca_DiscountID', max_length=50)  # Field name made lowercase.
    estrateca_discountamount = models.DecimalField(db_column='estrateca_DiscountAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desc_imp_original = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    donativo = models.DecimalField(max_digits=19, decimal_places=4)
    totalcondonativo = models.DecimalField(max_digits=19, decimal_places=4)

    # Duda
    totalconpropinacargodonativo = models.DecimalField(max_digits=19, decimal_places=4)

    orderreference = models.CharField(max_length=500)
    appname = models.CharField(max_length=250)
    paymentproviderid = models.CharField(max_length=50)
    paymentprovider = models.CharField(max_length=250)
    changestatussrx = models.BooleanField(db_column='ChangeStatusSRX', blank=True, null=True)  # Field name made lowercase.
    datedownload = models.DateTimeField(db_column='DateDownload', blank=True, null=True)  # Field name made lowercase.
    comandaimpresacancelada = models.BooleanField(blank=True, null=True)
    empaquetado = models.DateTimeField(blank=True, null=True)
    status_domicilio = models.IntegerField()
    asignacion = models.DateTimeField(blank=True, null=True)
    enviopagado = models.BooleanField()
    diet_restrictions = models.CharField(max_length=250)
    sl_cupon_descuento = models.CharField(max_length=250)
    sl_tipo_cupon = models.CharField(max_length=50)
    sl_importe_descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tuki_cardnumber = models.CharField(db_column='TUKI_CardNumber', max_length=250)  # Field name made lowercase.
    tuki_accumulatedpoints = models.DecimalField(db_column='TUKI_AccumulatedPoints', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tuki_currentpoints = models.DecimalField(db_column='TUKI_CurrentPoints', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sl_num_cupones = models.DecimalField(max_digits=16, decimal_places=6, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sentsync = models.BooleanField(db_column='SentSync')  # Field name made lowercase.
    subtotal_ec = models.BinaryField(blank=True, null=True)
    total_ec = models.BinaryField(blank=True, null=True)
    totalconpropinacargo_ec = models.BinaryField(blank=True, null=True)
    mv_room = models.CharField(max_length=100)
    mv_lastname = models.CharField(max_length=100)
    estado = models.BooleanField(default=False, db_column='estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cheques'
        verbose_name = 'Ver cheque'
        verbose_name_plural = 'Ver cheques'

class Chequesf(models.Model):
    folio = models.BigAutoField(primary_key=True)
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    numcheque = models.BigIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    salidarepartidor = models.DateTimeField(blank=True, null=True)
    arriborepartidor = models.DateTimeField(blank=True, null=True)
    cierre = models.DateTimeField(blank=True, null=True)
    mesa = models.CharField(max_length=100, blank=True, null=True)
    nopersonas = models.IntegerField(blank=True, null=True)
    idmesero = models.CharField(max_length=4, blank=True, null=True)
    pagado = models.BooleanField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    impreso = models.BooleanField(blank=True, null=True)
    impresiones = models.IntegerField(blank=True, null=True)
    cambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    reabiertas = models.IntegerField(blank=True, null=True)
    razoncancelado = models.CharField(max_length=255, blank=True, null=True)
    orden = models.BigIntegerField(blank=True, null=True)
    facturado = models.BooleanField(blank=True, null=True)
    idcliente = models.CharField(max_length=15, blank=True, null=True)
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    claveempresav = models.CharField(max_length=5, blank=True, null=True)
    tipodeservicio = models.IntegerField(blank=True, null=True)
    idturno = models.BigIntegerField(blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    estacion = models.CharField(max_length=40, blank=True, null=True)
    cambiorepartidor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    fechacancelado = models.DateTimeField(blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=30, blank=True, null=True)
    folionotadeconsumo = models.BigIntegerField(blank=True, null=True)
    notadeconsumo = models.BooleanField(blank=True, null=True)
    propinapagada = models.BooleanField(blank=True, null=True)
    propinafoliomovtocaja = models.BigIntegerField(blank=True, null=True)
    puntosmonederogenerados = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propinaincluida = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjetadescuento = models.CharField(max_length=30, blank=True, null=True)
    porcentajefac = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    propinamanual = models.BooleanField(blank=True, null=True)
    usuariopago = models.CharField(max_length=15, blank=True, null=True)
    idclientefacturacion = models.CharField(max_length=15, blank=True, null=True)
    cuentaenuso = models.BooleanField(blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    idclientedomicilio = models.CharField(max_length=15, blank=True, null=True)
    iddireccion = models.CharField(max_length=15, blank=True, null=True)
    telefonousadodomicilio = models.CharField(max_length=50, blank=True, null=True)
    totalarticulos = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    subtotalsinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconpropina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalimpuesto1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconcargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconpropinacargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentoimporte = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    efectivo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    otros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propinatarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    campoadicional1 = models.CharField(max_length=250, blank=True, null=True)
    idreservacion = models.CharField(max_length=25, blank=True, null=True)
    idcomisionista = models.CharField(max_length=15, blank=True, null=True)
    importecomision = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    comisionpagada = models.BooleanField(blank=True, null=True)
    fechapagocomision = models.DateTimeField(blank=True, null=True)
    foliopagocomision = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    tipoventarapida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    callcenter = models.BooleanField(blank=True, null=True)
    idordencompra = models.BigIntegerField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    totalsindescuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalotros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentoalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentobebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentootros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesias = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiaalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiabebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiaotros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentoycortesia = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalalimentossindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbebidassindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalotrossindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentocriterio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    descuentomonedero = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idmenucomedor = models.CharField(max_length=15, blank=True, null=True)
    subtotalcondescuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    comisionpax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    procesadointerfaz = models.BooleanField(blank=True, null=True)
    domicilioprogramado = models.BooleanField(blank=True, null=True)
    fechadomicilioprogramado = models.DateTimeField(blank=True, null=True)
    numerocuenta = models.CharField(max_length=100, blank=True, null=True)
    codigo_unico_af = models.CharField(max_length=30, blank=True, null=True)
    modificado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    enviadorw = models.BooleanField(db_column='EnviadoRW', blank=True, null=True)  # Field name made lowercase.
    usuarioapertura = models.CharField(max_length=15)
    autorizacionfolio = models.CharField(max_length=50, blank=True, null=True)
    fechalimiteemision = models.DateTimeField(blank=True, null=True)
    totalimpuestod1 = models.DecimalField(max_digits=19, decimal_places=4)
    totalimpuestod2 = models.DecimalField(max_digits=19, decimal_places=4)
    totalimpuestod3 = models.DecimalField(max_digits=19, decimal_places=4)
    idmotivocancela = models.CharField(max_length=200, blank=True, null=True)
    titulartarjetamonedero = models.CharField(max_length=100)
    saldoanteriormonedero = models.DecimalField(max_digits=19, decimal_places=4)
    ncf = models.CharField(max_length=19, blank=True, null=True)
    idformadepagodescuento = models.CharField(db_column='idformadepagoDescuento', max_length=5, blank=True, null=True)  # Field name made lowercase.
    titulartarjetamonederodescuento = models.CharField(max_length=100)
    surveycode = models.CharField(max_length=18)
    tkc_authorization = models.CharField(db_column='TKC_Authorization', max_length=100)  # Field name made lowercase.
    tkc_cupon = models.CharField(db_column='TKC_Cupon', max_length=100)  # Field name made lowercase.
    tkc_expirationdate = models.CharField(db_column='TKC_ExpirationDate', max_length=100)  # Field name made lowercase.
    tkc_recompensa = models.DecimalField(db_column='TKC_Recompensa', max_digits=19, decimal_places=4)  # Field name made lowercase.
    campoadicional2 = models.CharField(max_length=250)
    campoadicional3 = models.CharField(max_length=250)
    estrateca_cardnumber = models.CharField(db_column='estrateca_CardNumber', max_length=100)  # Field name made lowercase.
    estrateca_vouchertext = models.TextField(db_column='estrateca_VoucherText')  # Field name made lowercase.
    campoadicional4 = models.CharField(max_length=250)
    campoadicional5 = models.CharField(max_length=250)
    sacoa_cardnumber = models.CharField(db_column='sacoa_CardNumber', max_length=100)  # Field name made lowercase.
    sacoa_credits = models.DecimalField(max_digits=19, decimal_places=4)
    estrateca_typedisccount = models.CharField(db_column='estrateca_TypeDisccount', max_length=50)  # Field name made lowercase.
    estrateca_discountcode = models.CharField(db_column='estrateca_DiscountCode', max_length=50)  # Field name made lowercase.
    estrateca_discountid = models.CharField(db_column='estrateca_DiscountID', max_length=50)  # Field name made lowercase.
    estrateca_discountamount = models.DecimalField(db_column='estrateca_DiscountAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desc_imp_original = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    donativo = models.DecimalField(max_digits=19, decimal_places=4)
    totalcondonativo = models.DecimalField(max_digits=19, decimal_places=4)
    totalconpropinacargodonativo = models.DecimalField(max_digits=19, decimal_places=4)
    orderreference = models.CharField(max_length=500)
    appname = models.CharField(max_length=250)
    paymentproviderid = models.CharField(max_length=50)
    paymentprovider = models.CharField(max_length=250)
    changestatussrx = models.BooleanField(db_column='ChangeStatusSRX', blank=True, null=True)  # Field name made lowercase.
    datedownload = models.DateTimeField(db_column='DateDownload', blank=True, null=True)  # Field name made lowercase.
    empaquetado = models.DateTimeField(blank=True, null=True)
    status_domicilio = models.IntegerField()
    asignacion = models.DateTimeField(blank=True, null=True)
    enviopagado = models.BooleanField()
    sl_cupon_descuento = models.CharField(max_length=250)
    sl_tipo_cupon = models.CharField(max_length=50)
    sl_importe_descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tuki_cardnumber = models.CharField(db_column='TUKI_CardNumber', max_length=250)  # Field name made lowercase.
    tuki_accumulatedpoints = models.DecimalField(db_column='TUKI_AccumulatedPoints', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tuki_currentpoints = models.DecimalField(db_column='TUKI_CurrentPoints', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sl_num_cupones = models.DecimalField(max_digits=16, decimal_places=6, blank=True, null=True)
    subtotal_ec = models.BinaryField(blank=True, null=True)
    total_ec = models.BinaryField(blank=True, null=True)
    totalconpropinacargo_ec = models.BinaryField(blank=True, null=True)
    mv_room = models.CharField(max_length=100)
    mv_lastname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'chequesf'


class Chequespagos(models.Model):
    folio = models.BigIntegerField()
    idformadepago = models.ForeignKey('Formasdepago', models.DO_NOTHING, db_column='idformadepago', blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    referencia = models.TextField(blank=True, null=True)
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)
    sistema_envio = models.IntegerField()
    importe_ec = models.BinaryField(blank=True, null=True)
    propina_ec = models.BinaryField(blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36)  # Field name made lowercase.
    cardbrand = models.CharField(db_column='cardBrand', max_length=120)  # Field name made lowercase.
    importe_cashdro = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chequespagos'


class Chequespagosf(models.Model):
    folio = models.DecimalField(max_digits=9, decimal_places=0)
    idformadepago = models.ForeignKey('Formasdepago', models.DO_NOTHING, db_column='idformadepago', blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    referencia = models.TextField(blank=True, null=True)
    sistema_envio = models.IntegerField()
    importe_ec = models.BinaryField(blank=True, null=True)
    propina_ec = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chequespagosf'


class Clientes(models.Model):
    idcliente = models.CharField(primary_key=True, max_length=15)
    nombre = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=160, blank=True, null=True)
    codigopostal = models.CharField(max_length=15, blank=True, null=True)
    poblacion = models.CharField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=25, blank=True, null=True)
    pais = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    rfc = models.CharField(max_length=15, blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    cumpleaños = models.DateTimeField(blank=True, null=True)
    limitedecredito = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    limitecreditodiario = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notas = models.CharField(max_length=254, blank=True, null=True)
    foliofiscal = models.CharField(max_length=15, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    tipofacturacion = models.IntegerField(blank=True, null=True)
    procesadoweb = models.BooleanField(blank=True, null=True)
    nocobrarimpuestos = models.BooleanField(blank=True, null=True)
    contacto = models.CharField(max_length=250, blank=True, null=True)
    tarjetamonedero = models.CharField(max_length=20, blank=True, null=True)
    telefono1 = models.CharField(max_length=50, blank=True, null=True)
    telefono2 = models.CharField(max_length=50, blank=True, null=True)
    telefono3 = models.CharField(max_length=50, blank=True, null=True)
    telefono4 = models.CharField(max_length=50, blank=True, null=True)
    telefono5 = models.CharField(max_length=50, blank=True, null=True)
    femextipocliente = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    giro = models.CharField(max_length=60, blank=True, null=True)
    tipocredito = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idtipocliente = models.CharField(max_length=5, blank=True, null=True)
    idtipomenu = models.CharField(max_length=5, blank=True, null=True)
    fotografia = models.BinaryField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    retenerimpuesto = models.BooleanField(blank=True, null=True)
    tipocuenta = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipoclientencf = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    dinerid = models.CharField(max_length=50, blank=True, null=True)
    descuentoprimeraventacomedoremp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    idpais_sat = models.CharField(db_column='idpais_SAT', max_length=50)  # Field name made lowercase.
    contemplarpropina = models.BooleanField()
    oblig_tributarias = models.CharField(max_length=240)
    idregimen_sat = models.CharField(db_column='idregimen_SAT', max_length=50)  # Field name made lowercase.
    tratamientopersonal = models.CharField(max_length=30)
    status = models.BooleanField()
    dias_vigencia_credito = models.IntegerField()
    primer_nombre = models.CharField(max_length=50)
    otros_nombres = models.CharField(max_length=120)
    apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'clientes'


class Clientestitularsecundario(models.Model):
    idcliente = models.CharField(max_length=15, blank=True, null=True)
    idsecundario = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientestitularsecundario'


class Codigosdeserviciocfdi(models.Model):
    idcodigo = models.IntegerField(blank=True, null=True)
    codigoservicio = models.CharField(max_length=20, blank=True, null=True)
    folios = models.CharField(max_length=50, blank=True, null=True)
    usuarioregistro = models.CharField(max_length=50, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigosdeserviciocfdi'


class Colonias(models.Model):
    idcolonia = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    idzona = models.ForeignKey('Zonasdomicilio', models.DO_NOTHING, db_column='idzona', blank=True, null=True)
    tipo = models.DecimalField(max_digits=2, decimal_places=0)
    minutosreparto = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colonias'


class Comandas(models.Model):
    idmesero = models.CharField(max_length=4, blank=True, null=True)
    folio = models.CharField(max_length=8, blank=True, null=True)
    usado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comandas'


class Comandosimpresion(models.Model):
    idcomando = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    comando = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comandosimpresion'


class Comentarios(models.Model):
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    id_etiqueta = models.CharField(max_length=50)
    idcomentario = models.CharField(db_column='IdComentario', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comentarios'


class Comisionistas(models.Model):
    idcomisionista = models.CharField(primary_key=True, max_length=15)
    idtipocomisionista = models.ForeignKey('Tipocomisionistas', models.DO_NOTHING, db_column='idtipocomisionista', blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    razonsocial = models.CharField(max_length=120, blank=True, null=True)
    direccion = models.CharField(max_length=120, blank=True, null=True)
    codigopostal = models.CharField(max_length=15, blank=True, null=True)
    registrofiscal = models.CharField(max_length=15, blank=True, null=True)
    contacto = models.CharField(max_length=60, blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    paginaweb = models.CharField(max_length=100, blank=True, null=True)
    poblacion = models.CharField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=25, blank=True, null=True)
    pais = models.CharField(max_length=25, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    tipocomision = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    comisionporcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    comisionimporte = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puesto = models.CharField(max_length=20, blank=True, null=True)
    nacimiento = models.DateTimeField(blank=True, null=True)
    aniversario = models.DateTimeField(blank=True, null=True)
    cuentabancaria = models.CharField(max_length=120, blank=True, null=True)
    pagopax = models.CharField(max_length=8, blank=True, null=True)
    idbanco = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comisionistas'


class Companias(models.Model):
    idcompania = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companias'


class Compras(models.Model):
    idcompra = models.BigAutoField(primary_key=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    folio = models.CharField(max_length=15, blank=True, null=True)
    fechaaplicacion = models.DateTimeField(blank=True, null=True)
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    foliofactura = models.CharField(max_length=15, blank=True, null=True)
    fechafactura = models.DateTimeField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    fechavencimiento = models.DateTimeField(blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    referencia = models.CharField(max_length=50, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fiscal = models.BooleanField(blank=True, null=True)
    reterenta = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    reteiva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    reteica = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    editadosucursal = models.BooleanField(blank=True, null=True)
    idcompracentral = models.BigIntegerField(blank=True, null=True)
    polizagenerada = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'compras'


class Comprasmovtos(models.Model):
    idcompra = models.ForeignKey(Compras, models.DO_NOTHING, db_column='idcompra', blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto1importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    importesinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    importeconimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    idordencompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comprasmovtos'


class Conceptos(models.Model):
    idconcepto = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    autorizacion = models.BooleanField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conceptos'


class ConfigMicrosiga(models.Model):
    habilitar = models.BooleanField(blank=True, null=True)
    habilitar_sincronizacion = models.BooleanField(blank=True, null=True)
    tiempo_sincronizacion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    tabla_clientes = models.CharField(max_length=50, blank=True, null=True)
    tabla_productos = models.CharField(max_length=50, blank=True, null=True)
    tabla_almacenes = models.CharField(max_length=50, blank=True, null=True)
    tabla_movimientos = models.CharField(max_length=50, blank=True, null=True)
    tabla_ctt = models.CharField(max_length=50, blank=True, null=True)
    cliente_facturacion_cierre = models.CharField(max_length=15, blank=True, null=True)
    ctt = models.CharField(max_length=50, blank=True, null=True)
    producto_alimentos = models.CharField(max_length=10, blank=True, null=True)
    producto_bebidas = models.CharField(max_length=10, blank=True, null=True)
    producto_otros = models.CharField(max_length=10, blank=True, null=True)
    producto_credito = models.CharField(max_length=10, blank=True, null=True)
    producto_cortesia = models.CharField(max_length=10, blank=True, null=True)
    producto_propina = models.CharField(max_length=10, blank=True, null=True)
    serie_cxc = models.CharField(max_length=10, blank=True, null=True)
    serie_factura = models.CharField(max_length=10, blank=True, null=True)
    salvarxml = models.BooleanField(blank=True, null=True)
    rutaxml = models.CharField(max_length=50, blank=True, null=True)
    salvarsincr = models.BooleanField(blank=True, null=True)
    rutasincr = models.CharField(max_length=50, blank=True, null=True)
    catalogos_ultima_actualizacion = models.DateTimeField(db_column='catalogos_ultima_Actualizacion', blank=True, null=True)  # Field name made lowercase.
    iniciarconwindows = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_microsiga'


class Configuracion(models.Model):
    reindexado = models.DateTimeField(blank=True, null=True)
    respaldo = models.DateTimeField(blank=True, null=True)
    idencuesta = models.CharField(max_length=3, blank=True, null=True)
    encuestainicio = models.CharField(max_length=11, blank=True, null=True)
    encuestafin = models.CharField(max_length=11, blank=True, null=True)
    ivadesglosado = models.BooleanField(blank=True, null=True)
    impnotadeconsumo = models.BooleanField(blank=True, null=True)
    cancelaciones = models.BooleanField(blank=True, null=True)
    reabrir = models.BooleanField(blank=True, null=True)
    descuentos = models.BooleanField(blank=True, null=True)
    incluirpropina = models.BooleanField(blank=True, null=True)
    reimprimir = models.BooleanField(blank=True, null=True)
    cambiarproductodemesa = models.BooleanField(blank=True, null=True)
    cambiodemesa = models.BooleanField(blank=True, null=True)
    juntarmesas = models.BooleanField(blank=True, null=True)
    seguridadprecioabierto = models.BooleanField(blank=True, null=True)
    cambiarcomandas = models.CharField(max_length=10, blank=True, null=True)
    agruparcomandas = models.BooleanField(blank=True, null=True)
    lineascomedor = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    lineasdomicilio = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    lineasrapido = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    sugerirefectivo = models.BooleanField(blank=True, null=True)
    redondearcheque = models.BooleanField(blank=True, null=True)
    propinaincluida = models.BooleanField(blank=True, null=True)
    porcentajepropina = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    registrocontribuyente = models.CharField(max_length=10, blank=True, null=True)
    monedanacional = models.CharField(max_length=25, blank=True, null=True)
    usarcomandas = models.BooleanField(blank=True, null=True)
    resumirconsumocuenta = models.BooleanField(blank=True, null=True)
    propinabarra = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    propinacocina = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    propinagarrotero = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    propinacapitan = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    propinastaff = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    propinacaja = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    propinaempaque = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    ultimatransferencia = models.DateTimeField(blank=True, null=True)
    imprimirtituloscomedor = models.BooleanField(blank=True, null=True)
    imprimirtitulosdomicilio = models.BooleanField(blank=True, null=True)
    imprimirtitulosrapido = models.BooleanField(blank=True, null=True)
    imprimirtitulosnotadeconsumo = models.BooleanField(blank=True, null=True)
    usarproduccion = models.BooleanField(blank=True, null=True)
    comanderoimprimir = models.BooleanField(blank=True, null=True)
    comanderopagar = models.BooleanField(blank=True, null=True)
    contraseñainventarios = models.CharField(max_length=30, blank=True, null=True)
    timercomandero = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    conceptoentradaprod = models.CharField(max_length=5, blank=True, null=True)
    conceptosalidaprod = models.CharField(max_length=5, blank=True, null=True)
    conceptoentradatransferencia = models.CharField(max_length=5, blank=True, null=True)
    conceptosalidatransferencia = models.CharField(max_length=5, blank=True, null=True)
    conceptodesperdicio = models.CharField(max_length=5, blank=True, null=True)
    conceptoentradafisico = models.CharField(max_length=5, blank=True, null=True)
    conceptosalidafisico = models.CharField(max_length=5, blank=True, null=True)
    avisarvariaciondecostos = models.BooleanField(blank=True, null=True)
    porcentajevariaciondecostos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    versiondb = models.CharField(max_length=10, blank=True, null=True)
    revisiondb = models.CharField(max_length=2, blank=True, null=True)
    copiasfacturas = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cortezinicio = models.CharField(max_length=11, blank=True, null=True)
    cortezfin = models.CharField(max_length=11, blank=True, null=True)
    cortezfindiasiguiente = models.BooleanField(blank=True, null=True)
    ocultartiempos = models.BooleanField(blank=True, null=True)
    ocultarmitades = models.BooleanField(blank=True, null=True)
    ocultarcantidades = models.BooleanField(blank=True, null=True)
    permitirrespaldarturnoabierto = models.BooleanField(blank=True, null=True)
    cambiovales = models.BooleanField(blank=True, null=True)
    conceptofacturacion = models.CharField(max_length=50, blank=True, null=True)
    fondofijocaja = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    comanderopuedevermesas = models.BooleanField(blank=True, null=True)
    ccsobrantesdebe = models.CharField(max_length=5, blank=True, null=True)
    ccsobranteshaber = models.CharField(max_length=5, blank=True, null=True)
    ccfaltantes = models.CharField(max_length=5, blank=True, null=True)
    ccivagastos = models.CharField(max_length=5, blank=True, null=True)
    ccivaventas = models.CharField(max_length=5, blank=True, null=True)
    ccdescontarfaltante = models.CharField(max_length=5, blank=True, null=True)
    ccespecialdescuento = models.CharField(max_length=5, blank=True, null=True)
    ccespecialidcliente = models.CharField(max_length=15, blank=True, null=True)
    ccdescontargastos = models.CharField(max_length=5, blank=True, null=True)
    ccdescontarsobrante = models.CharField(max_length=5, blank=True, null=True)
    ccretiroscaja = models.CharField(max_length=5, blank=True, null=True)
    ccdepositoscaja = models.CharField(max_length=5, blank=True, null=True)
    ccaplicarmovtoscaja = models.CharField(max_length=5, blank=True, null=True)
    ccpolizaventasap = models.CharField(max_length=5, blank=True, null=True)
    ccpolizatipopagosap = models.CharField(max_length=5, blank=True, null=True)
    ccsapacreedoresdebe = models.CharField(max_length=5, blank=True, null=True)
    ccsapacreedoreshaber = models.CharField(max_length=5, blank=True, null=True)
    ccpuntosmonederogenerados = models.CharField(max_length=5, blank=True, null=True)
    ccdescontarpropinasdebe = models.CharField(max_length=5, blank=True, null=True)
    infofinmoneda = models.CharField(max_length=5, blank=True, null=True)
    infofindescripcionpoliza = models.CharField(max_length=75, blank=True, null=True)
    descripcionpolizacompras = models.CharField(max_length=25, blank=True, null=True)
    sapsociedad = models.CharField(max_length=4, blank=True, null=True)
    polizanumdivision = models.CharField(max_length=5, blank=True, null=True)
    simbolomoneda = models.CharField(max_length=4, blank=True, null=True)
    idfpefpagoagrupado = models.CharField(max_length=5, blank=True, null=True)
    idfptcpagoagrupado = models.CharField(max_length=5, blank=True, null=True)
    solicitarcomanda = models.BooleanField(blank=True, null=True)
    descontarcomisionpropinas = models.BooleanField(blank=True, null=True)
    ultimacompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ultimaordencompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ultimomovtoinsumo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ultimotraspaso = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usarpantallapequeñamodificador = models.BooleanField(blank=True, null=True)
    vercambiomonex = models.BooleanField(blank=True, null=True)
    vercambioclavemonex = models.CharField(max_length=5, blank=True, null=True)
    autocapturarformadepago = models.BooleanField(blank=True, null=True)
    autocapturaridformadepago = models.CharField(max_length=5, blank=True, null=True)
    nopermitircerrarturnocuentasabiertas = models.BooleanField(blank=True, null=True)
    ultimofolioalmacen = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ultimomovtopresentacion = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    nombrepropina = models.CharField(max_length=15, blank=True, null=True)
    decimalespdv = models.SmallIntegerField(blank=True, null=True)
    nopermitirarchivopoliza = models.BooleanField(blank=True, null=True)
    nopermitircompraspreciosmayores = models.BooleanField(blank=True, null=True)
    solicitarfacturacion = models.BooleanField(blank=True, null=True)
    meserosclavenumerica = models.BooleanField(blank=True, null=True)
    desglosarpaquetecomanda = models.BooleanField(blank=True, null=True)
    comanderoverventa = models.BooleanField(blank=True, null=True)
    imprimirdecimalespdv = models.BooleanField(blank=True, null=True)
    tipoconceptofacturacion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodeimpresioncompra = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ididiomaticket = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idclientepublico = models.CharField(max_length=15, blank=True, null=True)
    totalizarproductosfactura = models.BooleanField(blank=True, null=True)
    capturaventasteclado = models.BooleanField(blank=True, null=True)
    condtran = models.CharField(max_length=4, blank=True, null=True)
    suc = models.CharField(max_length=4, blank=True, null=True)
    pos = models.CharField(max_length=4, blank=True, null=True)
    oper = models.CharField(max_length=4, blank=True, null=True)
    osec = models.CharField(max_length=4, blank=True, null=True)
    puntos = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    plan = models.CharField(max_length=2, blank=True, null=True)
    ean = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    ref = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    numaut = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    oip = models.CharField(max_length=13, blank=True, null=True)
    port = models.CharField(max_length=15, blank=True, null=True)
    otrans = models.BooleanField(blank=True, null=True)
    olog = models.BooleanField(blank=True, null=True)
    otimeout = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    solicitarnotadeconsumo = models.BooleanField(blank=True, null=True)
    folioindependientenotadeconsumo = models.BooleanField(blank=True, null=True)
    solicitarimportecompra = models.BooleanField(blank=True, null=True)
    mitadesusarpreciomasalto = models.BooleanField(blank=True, null=True)
    urlregistrosweb = models.CharField(max_length=120, blank=True, null=True)
    ftpregistrowebdireccion = models.CharField(max_length=60, blank=True, null=True)
    ftpregistrowebusuario = models.CharField(max_length=40, blank=True, null=True)
    ftpregistrowebcontraseña = models.CharField(max_length=20, blank=True, null=True)
    pagoenlineatarjeta = models.BooleanField(blank=True, null=True)
    posip = models.CharField(max_length=15, blank=True, null=True)
    pospuerto = models.CharField(max_length=6, blank=True, null=True)
    posidsucursal = models.CharField(max_length=30, blank=True, null=True)
    posnumafiliacion = models.CharField(max_length=15, blank=True, null=True)
    posnumpuntodeventa = models.CharField(max_length=15, blank=True, null=True)
    posnumterminalprosa = models.CharField(max_length=15, blank=True, null=True)
    pospostracenumber = models.CharField(max_length=15, blank=True, null=True)
    poscopiasvoucher = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    postimeout = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    archivoexportacionpoliza = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nocancelarfolioscuentas = models.BooleanField(blank=True, null=True)
    noimpprodpreciocero = models.BooleanField(blank=True, null=True)
    nopermitircomentprepescrito = models.BooleanField(blank=True, null=True)
    polizanodesglosarimpuestos = models.BooleanField(blank=True, null=True)
    forzarmotivocancela = models.BooleanField(blank=True, null=True)
    solicitarcomentariopagarservrapido = models.BooleanField(blank=True, null=True)
    usarpantallapequeñamodificador0 = models.BooleanField(blank=True, null=True)
    hotelversionsistema = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    hotelrutadb = models.CharField(max_length=80, blank=True, null=True)
    hotelpassworddb = models.CharField(max_length=30, blank=True, null=True)
    hotelidconcepto = models.CharField(max_length=15, blank=True, null=True)
    generararchivoprodsvendidoscorte = models.BooleanField(blank=True, null=True)
    nodescargarinventario = models.BooleanField(blank=True, null=True)
    conceptoentradatraspasosreporte = models.CharField(max_length=5, blank=True, null=True)
    conceptosalidatraspasoreporte = models.CharField(max_length=5, blank=True, null=True)
    solicitarcantidadproducto = models.BooleanField(blank=True, null=True)
    formatocortedecajaresumido = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    obtenerfechahoraremota = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    estacionfechahora = models.CharField(max_length=40, blank=True, null=True)
    formatofecha = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    productocompuestousarmultiplicador = models.BooleanField(blank=True, null=True)
    tipogenerarpuntosmonedero = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ipmonedero = models.CharField(max_length=40, blank=True, null=True)
    bdmonedero = models.CharField(max_length=40, blank=True, null=True)
    contrasenamonedero = models.CharField(max_length=20, blank=True, null=True)
    usuariomonedero = models.CharField(max_length=20, blank=True, null=True)
    clavemonederocliente = models.CharField(max_length=15, blank=True, null=True)
    seguridaddividircuentas = models.BooleanField(blank=True, null=True)
    sysdatabase = models.CharField(max_length=100, blank=True, null=True)
    tiempovisualizapromo = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    caducidadpuntos = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    ccmonederoacreedor = models.CharField(max_length=5, blank=True, null=True)
    cccertificadoregalo = models.CharField(max_length=5, blank=True, null=True)
    pagarsinimprimir = models.BooleanField(blank=True, null=True)
    passmanttoventas = models.CharField(max_length=150, blank=True, null=True)
    imprimircredito = models.BooleanField(blank=True, null=True)
    tipocomandero = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    agruparalimentoscomedor = models.BooleanField(blank=True, null=True)
    agruparbebidascomedor = models.BooleanField(blank=True, null=True)
    agruparotroscomedor = models.BooleanField(blank=True, null=True)
    agruparalimentosdomicilio = models.BooleanField(blank=True, null=True)
    agruparbebidasdomicilio = models.BooleanField(blank=True, null=True)
    agruparotrosdomicilio = models.BooleanField(blank=True, null=True)
    agruparalimentosrapido = models.BooleanField(blank=True, null=True)
    agruparbebidasrapido = models.BooleanField(blank=True, null=True)
    agruparotrosrapido = models.BooleanField(blank=True, null=True)
    porcentajeaumentarcostotraspasos = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    motordepagotarjeta = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    payworksurl = models.CharField(max_length=50, blank=True, null=True)
    payworksmode = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    payworksclienteid = models.CharField(max_length=30, blank=True, null=True)
    payworksname = models.CharField(max_length=30, blank=True, null=True)
    payworkspassword = models.CharField(max_length=30, blank=True, null=True)
    payworksclienteiddolar = models.CharField(max_length=30, blank=True, null=True)
    payworksnamedolar = models.CharField(max_length=30, blank=True, null=True)
    payworkspassworddolar = models.CharField(max_length=30, blank=True, null=True)
    payworksclienteiddiferido = models.CharField(max_length=30, blank=True, null=True)
    payworksnamediferido = models.CharField(max_length=30, blank=True, null=True)
    payworkspassworddiferido = models.CharField(max_length=30, blank=True, null=True)
    fiscalmodificaventareal = models.BooleanField(blank=True, null=True)
    payworksafiliacion = models.CharField(max_length=50, blank=True, null=True)
    payworksafiliaciondolar = models.CharField(max_length=50, blank=True, null=True)
    payworksafiliaciondiferido = models.CharField(max_length=50, blank=True, null=True)
    tiempologout = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    formulatrackii = models.CharField(max_length=30, blank=True, null=True)
    abrircapturaporclaves = models.BooleanField(blank=True, null=True)
    confirmarfolionotaconsumo = models.BooleanField(blank=True, null=True)
    nocantidaddecimalventa = models.BooleanField(blank=True, null=True)
    nomensajesescritos = models.BooleanField(blank=True, null=True)
    facturaslineasmaximo = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    autorizacioncierrecomandero = models.BooleanField(blank=True, null=True)
    autorizacioncancelaproductorapido = models.BooleanField(blank=True, null=True)
    hotelpropina = models.CharField(max_length=15, blank=True, null=True)
    hotelbasededatos = models.CharField(max_length=40, blank=True, null=True)
    idsucursalmonedero = models.CharField(max_length=15, blank=True, null=True)
    autorizaciondeslizartarjeta = models.BooleanField(blank=True, null=True)
    autorizacioncambiarmesero = models.BooleanField(blank=True, null=True)
    tipopuntoselectronicos = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    autorizacioncargo = models.BooleanField(blank=True, null=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    autorizacionacumularpuntos = models.BooleanField(blank=True, null=True)
    autorizacionpagoconpuntos = models.BooleanField(blank=True, null=True)
    autorizaciongruposcaptura = models.BooleanField(blank=True, null=True)
    autorizacionventacredito = models.BooleanField(blank=True, null=True)
    deshabilitarmesa = models.BooleanField(blank=True, null=True)
    payworksvaruserid = models.CharField(max_length=250, blank=True, null=True)
    payworksvarorderid = models.CharField(max_length=250, blank=True, null=True)
    payworksvaruseriddolar = models.CharField(max_length=250, blank=True, null=True)
    payworksvarorderiddolar = models.CharField(max_length=250, blank=True, null=True)
    payworksvaruseriddiferido = models.CharField(max_length=250, blank=True, null=True)
    payworksvarorderiddiferido = models.CharField(max_length=250, blank=True, null=True)
    permitirfacturardolares = models.BooleanField()
    formasdepago_cierreturno = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'configuracion'


class ConfiguracionKds(models.Model):
    kdscolorfuentenormal = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfondonormal = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfuentefoco = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfondofoco = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfuentealerta = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfondoalerta = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfuenteatrasado = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfondoatrasado = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfuentecan = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdscolorfondocan = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdsnumcuadros = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdstiemporefresco = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    kdstimerenabled = models.BooleanField(blank=True, null=True)
    kdskeyboardenabled = models.BooleanField(blank=True, null=True)
    imprimircomanda = models.BooleanField(blank=True, null=True)
    autocuttercomanda = models.BooleanField(blank=True, null=True)
    impresoracomanda = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuracion_kds'


class ConfiguracionWs(models.Model):
    configuracion_vigencia = models.IntegerField(blank=True, null=True)
    configuracion_actualizacion = models.IntegerField(blank=True, null=True)
    configuracion_icono = models.BooleanField(blank=True, null=True)
    configuracion_codigos = models.IntegerField(blank=True, null=True)
    configuracion_url_personalizada = models.CharField(max_length=100, blank=True, null=True)
    configuracion_cierre_fiscal = models.BooleanField(blank=True, null=True)
    configuracion_cierre_mensual = models.BooleanField(blank=True, null=True)
    ws_usuario = models.CharField(max_length=150, blank=True, null=True)
    ws_password = models.CharField(max_length=150, blank=True, null=True)
    autofactura_enabled = models.BooleanField(blank=True, null=True)
    reportes_enabled = models.BooleanField(blank=True, null=True)
    configuracion_timeout = models.IntegerField(blank=True, null=True)
    configuracion_timeout_reportes = models.IntegerField(blank=True, null=True)
    configuracion_actualizacion_reportes = models.IntegerField(blank=True, null=True)
    autofactura_webservice = models.CharField(max_length=200, blank=True, null=True)
    reportes_webservice = models.CharField(max_length=200, blank=True, null=True)
    archivos_cfdi_enviados = models.BooleanField(db_column='archivos_CFDI_enviados', blank=True, null=True)  # Field name made lowercase.
    activacion_dias = models.CharField(max_length=150, blank=True, null=True)
    activacion_estatus = models.CharField(max_length=150, blank=True, null=True)
    ws_dias_reportes = models.CharField(max_length=150, blank=True, null=True)
    ws_estado_reportes = models.CharField(max_length=150, blank=True, null=True)
    autofactura_fecha = models.CharField(max_length=150, blank=True, null=True)
    reportes_fecha = models.CharField(max_length=150, blank=True, null=True)
    serie_factura = models.CharField(max_length=6, blank=True, null=True)
    ultima_descarga = models.DateTimeField(db_column='Ultima_descarga')  # Field name made lowercase.
    horas_entre_descargas = models.IntegerField(db_column='Horas_entre_descargas')  # Field name made lowercase.
    fecha_instalacion_af = models.DateTimeField(db_column='fecha_instalacion_AF')  # Field name made lowercase.
    manttoventasactivo = models.BooleanField(db_column='ManttoVentasActivo')  # Field name made lowercase.
    fecha_inicio_envio = models.DateTimeField()
    actualizado = models.BooleanField(db_column='Actualizado')  # Field name made lowercase.
    configuracion_cierremensual_dias = models.BooleanField()
    serie_complemento = models.CharField(max_length=6, blank=True, null=True)
    inicio_automatico = models.BooleanField()
    cliente_2doplano = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'configuracion_ws'


class Configuracionarchivoexportacion(models.Model):
    sapsociedad = models.CharField(max_length=4, blank=True, null=True)
    infofinmoneda = models.CharField(max_length=5, blank=True, null=True)
    infofindescripcionpoliza = models.CharField(max_length=75, blank=True, null=True)
    archivoexportacionpoliza = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    descripcionpolizacompras = models.CharField(max_length=25, blank=True, null=True)
    polizanumdivision = models.CharField(max_length=5, blank=True, null=True)
    polizanodesglosarimpuestos = models.BooleanField(blank=True, null=True)
    polizatiposistema = models.CharField(max_length=10, blank=True, null=True)
    polizaconvertirmonedaextranjera = models.BooleanField(blank=True, null=True)
    sapgenerardoscabecerosmonex = models.BooleanField(blank=True, null=True)
    infofintipodepoliza = models.CharField(max_length=2, blank=True, null=True)
    infofinusuario = models.CharField(max_length=2, blank=True, null=True)
    infofinpolizaregimensimp = models.CharField(max_length=1, blank=True, null=True)
    idempresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    posnumafiliacion = models.CharField(max_length=15, blank=True, null=True)
    prefijocompras = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuracionarchivoexportacion'


class Consumodiarioinsumos(models.Model):
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    consumopromdiario = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumodiarioinsumos'


class Cortesiasmonedero(models.Model):
    idcortesia = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    diasvigencia = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cortesiasmonedero'


class Cortesiasmonederodetalle(models.Model):
    idcortesia = models.ForeignKey(Cortesiasmonedero, models.DO_NOTHING, db_column='idcortesia', blank=True, null=True)
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cortesiasmonederodetalle'


class Cortesiasmonederotarjetas(models.Model):
    idcortesia = models.ForeignKey(Cortesiasmonedero, models.DO_NOTHING, db_column='idcortesia', blank=True, null=True)
    numerotarjeta = models.CharField(max_length=16, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechainicio = models.DateTimeField(blank=True, null=True)
    fechafin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cortesiasmonederotarjetas'


class Costos(models.Model):
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idinsumo = models.ForeignKey('Insumos', models.DO_NOTHING, db_column='idinsumo', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'costos'


class Cuentas(models.Model):
    clavemesero = models.CharField(max_length=15, blank=True, null=True)
    clavemesa = models.CharField(max_length=15, blank=True, null=True)
    numeropersonas = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    clavearea = models.CharField(max_length=5, blank=True, null=True)
    imprimir = models.BooleanField(blank=True, null=True)
    estacion = models.CharField(max_length=80, blank=True, null=True)
    prueba = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tiposervicio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    formadepago = models.CharField(max_length=15, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impresorabt = models.BooleanField(db_column='impresoraBT', blank=True, null=True)  # Field name made lowercase.
    idmesa = models.CharField(max_length=50, blank=True, null=True)
    editado = models.BooleanField(blank=True, null=True)
    enviadosr = models.BooleanField(blank=True, null=True)
    foliocuenta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalimpuesto1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentoimporte = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    procesado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    usuariopago = models.CharField(max_length=200, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propinaincluida = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    efectivo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    otros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propinatarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    numerocuenta = models.CharField(max_length=20, blank=True, null=True)
    motivocancelado = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    datosimpresion = models.TextField()
    mesaorigen = models.CharField(max_length=50)
    sistema_envio = models.IntegerField()
    iddispositivo = models.IntegerField()
    estacion_imprimir = models.CharField(max_length=80)
    idturno = models.BigIntegerField()
    pieimpresion = models.TextField(blank=True, null=True)
    tipoventarapido = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    foliokiosco = models.CharField(max_length=36, blank=True, null=True)
    idpropiedad = models.BigIntegerField()
    habitacion = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    salerestaurantid = models.CharField(max_length=250)
    rfc = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    datosimpresionfacturacion = models.TextField()
    subtotal_ec = models.BinaryField(blank=True, null=True)
    total_ec = models.BinaryField(blank=True, null=True)
    urlautofactura = models.CharField(db_column='urlAutofactura', max_length=230)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuentas'


class CuentasProcesar(models.Model):
    idcuenta = models.CharField(max_length=50)
    idcomanda = models.IntegerField()
    productos = models.IntegerField()
    contador = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuentas_procesar'


class Cuentascontables(models.Model):
    idcuentacontable = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    clavecontable = models.CharField(max_length=2, blank=True, null=True)
    clasifpoliza = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    indicadorimpuesto = models.CharField(max_length=2, blank=True, null=True)
    cuenta = models.CharField(max_length=10, blank=True, null=True)
    subcuenta = models.CharField(max_length=10, blank=True, null=True)
    subsubcuenta = models.CharField(max_length=10, blank=True, null=True)
    auxiliar = models.CharField(max_length=10, blank=True, null=True)
    moneda = models.CharField(max_length=3, blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    polizatienenumdivision = models.BooleanField(blank=True, null=True)
    polizatipocentro = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    polizasolicitareferencia = models.BooleanField(blank=True, null=True)
    usarenoperacion = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    usaromnitrans = models.BooleanField(blank=True, null=True)
    nombrectacontpaq = models.CharField(max_length=150)
    costcenter = models.CharField(db_column='CostCenter', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuentascontables'


class Cuentascontablesdetalle(models.Model):
    idcuentacontable = models.CharField(max_length=5)
    descripciondetalle = models.CharField(max_length=50, blank=True, null=True)
    cuenta = models.CharField(max_length=10, blank=True, null=True)
    subcuenta = models.CharField(max_length=10, blank=True, null=True)
    subsubcuenta = models.CharField(max_length=10, blank=True, null=True)
    auxiliar = models.CharField(max_length=10, blank=True, null=True)
    idempresa = models.CharField(max_length=15)
    descargar = models.BooleanField(blank=True, null=True)
    archingalternouni = models.BooleanField(db_column='ArchIngAlternoUni', blank=True, null=True)  # Field name made lowercase.
    companiaua = models.CharField(db_column='companiaUA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    clavecontabilizacion = models.CharField(max_length=10, blank=True, null=True)
    clavecontabilizacionhaber = models.CharField(max_length=10, blank=True, null=True)
    cuentafilialuni = models.CharField(max_length=10, blank=True, null=True)
    clavecontabilizacionfilialuni = models.CharField(db_column='ClaveContabilizacionFilialUni', max_length=10, blank=True, null=True)  # Field name made lowercase.
    clavecontabilizacionua = models.CharField(db_column='ClavecontabilizacionUA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tipodepoliza = models.CharField(max_length=10, blank=True, null=True)
    cuentamayorua = models.CharField(db_column='CuentaMayorUA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    clienteua = models.CharField(db_column='ClienteUA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    acreedorua = models.CharField(db_column='AcreedorUA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    relacion = models.CharField(max_length=10, blank=True, null=True)
    secuencia = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    iva = models.BooleanField(blank=True, null=True)
    comision = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    cuenta1 = models.CharField(max_length=10, blank=True, null=True)
    naturaleza = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    referencia = models.CharField(max_length=8, blank=True, null=True)
    descripcionmovcontable = models.CharField(max_length=40, blank=True, null=True)
    tipodediario = models.CharField(max_length=5, blank=True, null=True)
    ctaarchivoalt = models.CharField(max_length=50, blank=True, null=True)
    asiento = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    referenciaalt = models.CharField(max_length=5, blank=True, null=True)
    compania = models.CharField(max_length=10, blank=True, null=True)
    cuentamayor = models.CharField(max_length=10, blank=True, null=True)
    cliente = models.CharField(max_length=10, blank=True, null=True)
    acreedor = models.CharField(max_length=10, blank=True, null=True)
    tipoimpuesto = models.CharField(max_length=10, blank=True, null=True)
    centrocostos = models.CharField(max_length=10, blank=True, null=True)
    centrobeneficio = models.CharField(max_length=10, blank=True, null=True)
    tipoimpuestoua = models.CharField(max_length=10, blank=True, null=True)
    centrocostosua = models.CharField(max_length=10, blank=True, null=True)
    centrobeneficioua = models.CharField(max_length=10, blank=True, null=True)
    generaingresofilial = models.BooleanField(blank=True, null=True)
    clavecontabilizacionfilial = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentascontablesdetalle'


class Cuentaspagos(models.Model):
    folio = models.BigIntegerField(blank=True, null=True)
    idformadepago = models.CharField(max_length=5, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    referencia = models.TextField(blank=True, null=True)
    foliokiosco = models.CharField(db_column='FolioKiosco', max_length=36, blank=True, null=True)  # Field name made lowercase.
    importe_ec = models.BinaryField(blank=True, null=True)
    propina_ec = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentaspagos'


class Cuentasporcobrar(models.Model):
    foliocxc = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idturno = models.IntegerField(blank=True, null=True)
    idcliente = models.CharField(max_length=15, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    foliocuenta = models.CharField(max_length=25, blank=True, null=True)
    nota = models.CharField(max_length=100, blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    pagada = models.BooleanField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    idsecundario = models.CharField(max_length=15, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fechavigencia = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentasporcobrar'


class Cuentasporcobrarpagos(models.Model):
    foliocxc = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    idformadepago = models.CharField(max_length=5, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    referencia = models.CharField(max_length=80, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentasporcobrarpagos'


class Declaracioncajero(models.Model):
    idturnointerno = models.BigIntegerField()
    idturno = models.BigIntegerField()
    idformadepago = models.CharField(max_length=10)
    importedeclarado = models.DecimalField(max_digits=19, decimal_places=4)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    descripcion = models.CharField(max_length=30)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'declaracioncajero'


class Declaracioncorte(models.Model):
    idturno = models.BigIntegerField()
    sistema_turno = models.IntegerField()
    iddenominacion = models.CharField(max_length=10)
    tipodenominacion = models.IntegerField()
    nombremoneda = models.CharField(max_length=30)
    denominacion = models.DecimalField(max_digits=19, decimal_places=4)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4)
    cantidad = models.IntegerField()
    autorizacion = models.CharField(max_length=10)
    importevoucher = models.DecimalField(max_digits=19, decimal_places=4)
    propinavoucher = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'declaracioncorte'


class Denominaciones(models.Model):
    iddenominacion = models.CharField(primary_key=True, max_length=10)
    tipodenominacion = models.IntegerField()
    nombremoneda = models.CharField(max_length=30, blank=True, null=True)
    denominacion = models.DecimalField(max_digits=19, decimal_places=4)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4)
    idformapagoex = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'denominaciones'


class Deptosventa(models.Model):
    iddeptoventa = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    idcuentacontable = models.ForeignKey(Cuentascontables, models.DO_NOTHING, db_column='idcuentacontable', blank=True, null=True)
    idcuentacontablecostodebe = models.CharField(max_length=5, blank=True, null=True)
    idcuentacontablecostohaber = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deptosventa'


class Deptosventagrupos(models.Model):
    iddeptoventa = models.ForeignKey(Deptosventa, models.DO_NOTHING, db_column='iddeptoventa', blank=True, null=True)
    idgrupo = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deptosventagrupos'


class Deptosventagruposinsumos(models.Model):
    iddeptoventa = models.ForeignKey(Deptosventa, models.DO_NOTHING, db_column='iddeptoventa', blank=True, null=True)
    idgruposi = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deptosventagruposinsumos'


class Desperdicios(models.Model):
    cantidad = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    idproductorelacionado = models.CharField(max_length=15, blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    escancelacion = models.BooleanField(blank=True, null=True)
    esdesperdicio = models.BooleanField(blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'desperdicios'


class Destinatarioantifraude(models.Model):
    destinatario = models.CharField(max_length=60)
    tipocorreo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'destinatarioantifraude'


class Destinatariocorte(models.Model):
    destinatario = models.CharField(max_length=60)
    tipocorreo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'destinatariocorte'


class Destinatarioscorreo(models.Model):
    destinatario = models.CharField(max_length=60, blank=True, null=True)
    tipocorreo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destinatarioscorreo'


class Detallescuentas(models.Model):
    clavemesa = models.CharField(max_length=22, blank=True, null=True)
    clave = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    nombrecorto = models.CharField(max_length=10, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    tiempo = models.CharField(max_length=20, blank=True, null=True)
    modificador = models.BooleanField(blank=True, null=True)
    estacion = models.CharField(max_length=80, blank=True, null=True)
    mitad = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tiposerviciodet = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    enviadosr = models.BooleanField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    movimiento = models.IntegerField(blank=True, null=True)
    separador = models.BooleanField(blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    procesado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    motivocancelado = models.CharField(max_length=100, blank=True, null=True)
    cantidadcancelado = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    usuariocancelar = models.CharField(max_length=15, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    idproductocompuesto = models.CharField(max_length=15, blank=True, null=True)
    productocompuestoprincipal = models.BooleanField(blank=True, null=True)
    nivel = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idcomanda = models.IntegerField(blank=True, null=True)
    comanda = models.CharField(max_length=10)
    sistema_envio = models.IntegerField()
    idmesero = models.CharField(max_length=10)
    id_unico = models.CharField(max_length=50)
    iddispositivo = models.IntegerField()
    foliokiosco = models.CharField(max_length=36, blank=True, null=True)
    promovolumen = models.BooleanField(blank=True, null=True)
    saledetailid = models.CharField(max_length=250)
    precio_ec = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallescuentas'


class Direccionesdomicilio(models.Model):
    iddireccion = models.CharField(max_length=15)
    idcliente = models.CharField(max_length=15, blank=True, null=True)
    idcolonia = models.CharField(max_length=5, blank=True, null=True)
    delegacion = models.CharField(max_length=250, blank=True, null=True)
    calle = models.CharField(max_length=250, blank=True, null=True)
    cruzamiento1 = models.CharField(max_length=250, blank=True, null=True)
    cruzamiento2 = models.CharField(max_length=100, blank=True, null=True)
    numeroexterior = models.CharField(max_length=250, blank=True, null=True)
    numerointerior = models.CharField(max_length=250, blank=True, null=True)
    codigopostal = models.CharField(max_length=15, blank=True, null=True)
    ciudad = models.CharField(max_length=250, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True, null=True)
    referencia = models.CharField(max_length=250, blank=True, null=True)
    dineraddressid = models.CharField(max_length=250, blank=True, null=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=7, decimal_places=6, blank=True, null=True)
    district = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'direccionesdomicilio'


class Elaborados(models.Model):
    idelaborado = models.ForeignKey('Insumos', models.DO_NOTHING, db_column='idelaborado', blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elaborados'


class EmpresaProveedor(models.Model):
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idproveedor = models.CharField(max_length=15, blank=True, null=True)
    descarga = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa_proveedor'


class Empresas(models.Model):
    idempresa = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    razonsocial = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    sucursal = models.CharField(max_length=250, blank=True, null=True)
    rfc = models.CharField(max_length=150, blank=True, null=True)
    curp = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=150, blank=True, null=True)
    giro = models.CharField(max_length=200, blank=True, null=True)
    contacto = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    fechacompra = models.DateTimeField(blank=True, null=True)
    distribuidor = models.CharField(max_length=250, blank=True, null=True)
    numerofactura = models.CharField(max_length=100, blank=True, null=True)
    numerodecontrol = models.CharField(max_length=200, blank=True, null=True)
    contrasenacontrol = models.CharField(max_length=150, blank=True, null=True)
    idhardware = models.CharField(max_length=150, blank=True, null=True)
    licenciaprincipal = models.CharField(max_length=150, blank=True, null=True)
    licenciamonederoelectronico = models.CharField(max_length=150, blank=True, null=True)
    licenciamonitorproduccion = models.CharField(max_length=150, blank=True, null=True)
    licenciasrmovil = models.CharField(max_length=150, blank=True, null=True)
    licenciamanttoventas = models.CharField(max_length=150, blank=True, null=True)
    licenciapagoenlinea = models.CharField(max_length=150, blank=True, null=True)
    licenciahuelladigital = models.CharField(max_length=150, blank=True, null=True)
    licenciabillar = models.CharField(max_length=150, blank=True, null=True)
    franquicia = models.BooleanField(blank=True, null=True)
    web = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=True)
    pais = models.CharField(max_length=150, blank=True, null=True)
    ciudadsucursal = models.CharField(max_length=150, blank=True, null=True)
    estadosucursal = models.CharField(max_length=150, blank=True, null=True)
    passwordempresa = models.CharField(max_length=15, blank=True, null=True)
    escedis = models.BooleanField(blank=True, null=True)
    idproveedor = models.CharField(max_length=15, blank=True, null=True)
    escorporativo = models.BooleanField(blank=True, null=True)
    codigopostal = models.CharField(max_length=100, blank=True, null=True)
    ventapedidocedis = models.BooleanField(blank=True, null=True)
    descuentocedis = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    idtipoempresa = models.ForeignKey('Tipoempresa', models.DO_NOTHING, db_column='idtipoempresa', blank=True, null=True)
    idregionempresa = models.ForeignKey('Regionempresa', models.DO_NOTHING, db_column='idregionempresa', blank=True, null=True)
    idestado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='idestado', blank=True, null=True)
    idpais = models.ForeignKey('Paises', models.DO_NOTHING, db_column='idpais', blank=True, null=True)
    claveunicaempresa = models.CharField(max_length=50, blank=True, null=True)
    regimen = models.CharField(max_length=100, blank=True, null=True)
    idempresahub = models.CharField(max_length=50, blank=True, null=True)
    logohub = models.BinaryField(blank=True, null=True)
    logoempresa = models.TextField()
    logoempresaext = models.CharField(max_length=10)
    prefijoempresa = models.CharField(max_length=3)
    a86ed5f9d02ec5b3 = models.CharField(max_length=250, blank=True, null=True)
    idplaza = models.CharField(max_length=15, blank=True, null=True)
    idcompania = models.CharField(max_length=15, blank=True, null=True)
    idubicacionempresa = models.CharField(max_length=15, blank=True, null=True)
    idzonaempresa = models.CharField(max_length=15, blank=True, null=True)
    asientos = models.IntegerField(blank=True, null=True)
    metroscuadrados = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fechaapertura = models.CharField(max_length=10, blank=True, null=True)
    fechacierre = models.CharField(max_length=10, blank=True, null=True)
    fechamodificado = models.CharField(max_length=10, blank=True, null=True)
    imagen_logo_menu = models.TextField(blank=True, null=True)
    imagen_portada_menu = models.TextField(blank=True, null=True)
    eslogan = models.CharField(max_length=300)
    nombre_menu = models.CharField(max_length=300)
    codigopostalsucursal = models.CharField(max_length=100)
    idregimen_sat = models.CharField(db_column='idregimen_SAT', max_length=50)  # Field name made lowercase.
    uid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas'


class EmpresasCol(models.Model):
    idempresa = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=200)
    razonsocial = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250)
    sucursal = models.CharField(max_length=250)
    rfc = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    giro = models.CharField(max_length=200)
    contacto = models.CharField(max_length=150)
    email = models.CharField(max_length=120)
    web = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudadsucursal = models.CharField(max_length=100)
    estadosucursal = models.CharField(max_length=100)
    codigopostal = models.CharField(max_length=30)
    regimen = models.CharField(max_length=150)
    codigopostalsucursal = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'empresas_col'


class EmpresasRegaliasConfig(models.Model):
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa')
    aplicarregalias = models.BooleanField(blank=True, null=True)
    aplicarcannon = models.BooleanField(blank=True, null=True)
    montocannon = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    aplicarroyalties = models.BooleanField(blank=True, null=True)
    esquema = models.SmallIntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas_regalias_config'


class Empresasvi(models.Model):
    idempresavi = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    idcuentacontable = models.ForeignKey(Cuentascontables, models.DO_NOTHING, db_column='idcuentacontable', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresasvi'


class Empresasvp(models.Model):
    idempresavp = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    rangoinicial = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    rangofinal = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    idcuentacontable = models.ForeignKey(Cuentascontables, models.DO_NOTHING, db_column='idcuentacontable', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresasvp'


class Encuestas(models.Model):
    idencuesta = models.CharField(primary_key=True, max_length=3)
    titulo = models.CharField(max_length=50, blank=True, null=True)
    pregunta1 = models.CharField(max_length=50, blank=True, null=True)
    resp11 = models.CharField(max_length=30, blank=True, null=True)
    resp12 = models.CharField(max_length=30, blank=True, null=True)
    resp13 = models.CharField(max_length=30, blank=True, null=True)
    pregunta2 = models.CharField(max_length=50, blank=True, null=True)
    resp21 = models.CharField(max_length=30, blank=True, null=True)
    resp22 = models.CharField(max_length=30, blank=True, null=True)
    resp23 = models.CharField(max_length=30, blank=True, null=True)
    pregunta3 = models.CharField(max_length=50, blank=True, null=True)
    resp31 = models.CharField(max_length=30, blank=True, null=True)
    resp32 = models.CharField(max_length=30, blank=True, null=True)
    resp33 = models.CharField(max_length=30, blank=True, null=True)
    pregunta4 = models.CharField(max_length=50, blank=True, null=True)
    resp41 = models.CharField(max_length=30, blank=True, null=True)
    resp42 = models.CharField(max_length=30, blank=True, null=True)
    resp43 = models.CharField(max_length=30, blank=True, null=True)
    pregunta5 = models.CharField(max_length=50, blank=True, null=True)
    resp51 = models.CharField(max_length=30, blank=True, null=True)
    resp52 = models.CharField(max_length=30, blank=True, null=True)
    resp53 = models.CharField(max_length=30, blank=True, null=True)
    pregunta6 = models.CharField(max_length=50, blank=True, null=True)
    resp61 = models.CharField(max_length=30, blank=True, null=True)
    resp62 = models.CharField(max_length=30, blank=True, null=True)
    resp63 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encuestas'


class Estaciones(models.Model):
    idestacion = models.CharField(primary_key=True, max_length=40)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    serie = models.CharField(max_length=30, blank=True, null=True)
    ip = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=200, blank=True, null=True)
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    bloqueararearestaurant = models.BooleanField(blank=True, null=True)
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    mostrarcumpleaños = models.BooleanField(blank=True, null=True)
    esconderescritorio = models.BooleanField(blank=True, null=True)
    esconderbarra = models.BooleanField(blank=True, null=True)
    impresoracheques = models.CharField(max_length=50, blank=True, null=True)
    impresoranotas = models.CharField(max_length=50, blank=True, null=True)
    impresorafacturas = models.CharField(max_length=50, blank=True, null=True)
    saltosimpresoracheques = models.IntegerField(blank=True, null=True)
    saltosimpresoranotas = models.IntegerField(blank=True, null=True)
    usacutterimpresoracheques = models.BooleanField(blank=True, null=True)
    usacutterimpresoranotas = models.BooleanField(blank=True, null=True)
    usacajondedinero = models.BooleanField(blank=True, null=True)
    cajonascii = models.CharField(max_length=20, blank=True, null=True)
    cajonpuerto = models.IntegerField(blank=True, null=True)
    cajontipo = models.IntegerField(blank=True, null=True)
    cajontiempo = models.IntegerField(blank=True, null=True)
    cajonimpresora = models.CharField(max_length=50, blank=True, null=True)
    cajontipoconexion = models.IntegerField(blank=True, null=True)
    cajacomandero = models.CharField(max_length=80, blank=True, null=True)
    impventasempezar1 = models.CharField(max_length=3, blank=True, null=True)
    impventasempezar2 = models.CharField(max_length=3, blank=True, null=True)
    impventasempezar3 = models.CharField(max_length=3, blank=True, null=True)
    impventasempezar4 = models.CharField(max_length=3, blank=True, null=True)
    impventasempezar5 = models.CharField(max_length=8, blank=True, null=True)
    impventasfinalizar1 = models.CharField(max_length=3, blank=True, null=True)
    impventasfinalizar2 = models.CharField(max_length=3, blank=True, null=True)
    impventasfinalizar3 = models.CharField(max_length=3, blank=True, null=True)
    impventasfinalizar4 = models.CharField(max_length=3, blank=True, null=True)
    impventasfinalizar5 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar1 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar2 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar3 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar4 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar5 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar1 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar2 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar3 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar4 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar5 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar1 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar2 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar3 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar4 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar5 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar1 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar2 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar3 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar4 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar5 = models.CharField(max_length=3, blank=True, null=True)
    idformatofacturafiscal = models.IntegerField(blank=True, null=True)
    idformatofacturapublico = models.IntegerField(blank=True, null=True)
    estacionpocket = models.BooleanField(blank=True, null=True)
    colorbotones = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    colorpantallas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    colorcuadrosdetexto = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipodeimpresionfactura = models.IntegerField(blank=True, null=True)
    seriefacturacion = models.CharField(max_length=15, blank=True, null=True)
    usarturnoestacion = models.IntegerField(blank=True, null=True)
    buscaractualizaciones = models.BooleanField(blank=True, null=True)
    directorioactualizaciones = models.CharField(max_length=150, blank=True, null=True)
    nombrearchivoexportacion = models.CharField(max_length=80, blank=True, null=True)
    directoriorespaldo = models.CharField(max_length=150, blank=True, null=True)
    directoriopoliza = models.CharField(max_length=150, blank=True, null=True)
    directorioexportacion = models.CharField(max_length=150, blank=True, null=True)
    numeroestacion = models.IntegerField(blank=True, null=True)
    nombrepuntodeventa = models.CharField(max_length=40, blank=True, null=True)
    serieimpresoracuentas = models.CharField(max_length=40, blank=True, null=True)
    posnoterminal = models.CharField(max_length=15, blank=True, null=True)
    rutasonido = models.CharField(max_length=150, blank=True, null=True)
    sonidomonitor = models.BooleanField(blank=True, null=True)
    usarbascula = models.BooleanField(blank=True, null=True)
    basculapuerto = models.IntegerField(blank=True, null=True)
    basculabitsegundo = models.CharField(max_length=10, blank=True, null=True)
    basculabitdatos = models.CharField(max_length=10, blank=True, null=True)
    basculaparidad = models.CharField(max_length=10, blank=True, null=True)
    basculabitdeparada = models.CharField(max_length=10, blank=True, null=True)
    facturaslineasencabezado = models.IntegerField(blank=True, null=True)
    facturaslineaspiedepagina = models.IntegerField(blank=True, null=True)
    facturassumarlineascuerpoapie = models.BooleanField(blank=True, null=True)
    autorizacionacceso = models.IntegerField(blank=True, null=True)
    autorizacioneventos = models.IntegerField(blank=True, null=True)
    autorizacioncomandero = models.IntegerField(blank=True, null=True)
    ejecutararchivocierre = models.BooleanField(blank=True, null=True)
    nombrearchivoejecutarcierre = models.CharField(max_length=150, blank=True, null=True)
    enlacesoftencuestas = models.BooleanField(blank=True, null=True)
    impresorafiscal = models.BooleanField(blank=True, null=True)
    fiscalport = models.IntegerField(blank=True, null=True)
    paridadxsegfiscal = models.IntegerField(blank=True, null=True)
    idcallactivo = models.BooleanField(blank=True, null=True)
    idcallpuerto = models.IntegerField(blank=True, null=True)
    idcallbitsegundo = models.CharField(max_length=10, blank=True, null=True)
    idcallbitdatos = models.CharField(max_length=10, blank=True, null=True)
    idcallparidad = models.CharField(max_length=10, blank=True, null=True)
    idcallbitdeparada = models.CharField(max_length=50, blank=True, null=True)
    paisimpresorafiscal = models.IntegerField(blank=True, null=True)
    visorinstalado = models.BooleanField(blank=True, null=True)
    visorpuerto = models.IntegerField(blank=True, null=True)
    visormensaje = models.BooleanField(blank=True, null=True)
    mensajeespera = models.CharField(max_length=40, blank=True, null=True)
    idcallnorma = models.IntegerField(blank=True, null=True)
    monitorteclaarriba = models.CharField(max_length=5, blank=True, null=True)
    monitorteclafinalizar = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaregresar = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaprimero = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaabajo = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaultimo = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaactualizar = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonanterior = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonsiguiente = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonizquierda = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonderecha = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonactualizar = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonconsultaorden = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmoncerrarconsulta = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonfinorden = models.CharField(max_length=5, blank=True, null=True)
    intervalosonidoexcedidomonitor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    monitorimprimircomanda = models.BooleanField(blank=True, null=True)
    monitorimpresoracomandas = models.CharField(max_length=60, blank=True, null=True)
    monitorimpresoraautocutter = models.BooleanField(blank=True, null=True)
    monitoriniciarmodulo = models.IntegerField(blank=True, null=True)
    monitorordenamientoproductos = models.IntegerField(blank=True, null=True)
    tarjetacredito = models.BooleanField(blank=True, null=True)
    tipodispositivo = models.IntegerField(blank=True, null=True)
    pinpadpuertocom = models.CharField(max_length=10, blank=True, null=True)
    pinpadbitsxsegundo = models.CharField(max_length=10, blank=True, null=True)
    pinpadparidad = models.CharField(max_length=1, blank=True, null=True)
    pinpadbitsdeparada = models.CharField(max_length=3, blank=True, null=True)
    pinpadbitsdedatos = models.CharField(max_length=1, blank=True, null=True)
    tipoimpresoracuentas = models.IntegerField(blank=True, null=True)
    tipoimpresoranotas = models.IntegerField(blank=True, null=True)
    fiscalimpcambio = models.IntegerField(blank=True, null=True)
    fiscalimpcantximporte = models.IntegerField(blank=True, null=True)
    sonidomonitortiempoexcedido = models.BooleanField(blank=True, null=True)
    rutasonidotiempoexcedido = models.CharField(max_length=150, blank=True, null=True)
    tipoimpresioncomandamonitor = models.IntegerField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    usartipoventarapida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    actualizarcatalogos = models.BooleanField(blank=True, null=True)
    enviarcomandosdeimpresion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    comandoantesimprimir1 = models.CharField(max_length=30, blank=True, null=True)
    comandoantesimprimir2 = models.CharField(max_length=30, blank=True, null=True)
    comandoantescopia1 = models.CharField(max_length=30, blank=True, null=True)
    comandoantescopia2 = models.CharField(max_length=30, blank=True, null=True)
    actualizaclientes = models.BooleanField(blank=True, null=True)
    rutatemporal = models.CharField(max_length=255, blank=True, null=True)
    fenombreformatopublico = models.CharField(max_length=50, blank=True, null=True)
    fenombreformatoempresa = models.CharField(max_length=50, blank=True, null=True)
    feimpresoragrafico = models.CharField(max_length=250, blank=True, null=True)
    lectordehuellainstalado = models.IntegerField(blank=True, null=True)
    autorizacioncuentasporcobrar = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    logofiscal = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    densidadlogo = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    idarearestaurantrapido = models.CharField(max_length=5, blank=True, null=True)
    idarearestaurantdomicilio = models.CharField(max_length=5, blank=True, null=True)
    monprodincluirtodas = models.BooleanField(blank=True, null=True)
    impfiscalvalidaitems = models.BooleanField(blank=True, null=True)
    monitorimprimircomandamoduloadmin = models.BooleanField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    serieimpresora = models.CharField(max_length=10, blank=True, null=True)
    fecharev = models.CharField(max_length=10, blank=True, null=True)
    rev = models.CharField(max_length=4, blank=True, null=True)
    accesocentral = models.BooleanField(blank=True, null=True)
    usarturnousuario = models.DecimalField(max_digits=1, decimal_places=0)
    solicitarturnocomandero = models.DecimalField(max_digits=1, decimal_places=0)
    usuariocajacomandero = models.CharField(max_length=15)
    actualizarexistencias = models.BooleanField()
    bloquearteclado = models.BooleanField(blank=True, null=True)
    servidoraplicacionessucursal = models.BooleanField(blank=True, null=True)
    servidoraplicaciones = models.BooleanField(blank=True, null=True)
    actualizarcatalogosmovil = models.BooleanField(blank=True, null=True)
    colorbarratitulo = models.DecimalField(max_digits=10, decimal_places=0)
    ejecarchnvacta = models.IntegerField()
    archejecnvacta = models.CharField(max_length=200)
    paramejecnvacta = models.CharField(max_length=200)
    ejecarchreimpresioncta = models.IntegerField()
    archejecreimpresioncta = models.CharField(max_length=200)
    paramejecreimpresioncta = models.CharField(max_length=200)
    ejecarchcancelcta = models.IntegerField()
    archejeccancelcta = models.CharField(max_length=200)
    paramejeccancelcta = models.CharField(max_length=200)
    ejecarchreabrircta = models.IntegerField()
    archejecreabrircta = models.CharField(max_length=200)
    paramejecreabrircta = models.CharField(max_length=200)
    idformatocomedor = models.CharField(max_length=5)
    idformatodomicilio = models.CharField(max_length=5)
    idformatorapido = models.CharField(max_length=5)
    idformatonotadeconsumo = models.CharField(max_length=5)
    idformatomovil = models.CharField(max_length=5)
    copiasticketcomedor = models.DecimalField(max_digits=2, decimal_places=0)
    copiasticketdomicilio = models.DecimalField(max_digits=2, decimal_places=0)
    copiasticketrapido = models.DecimalField(max_digits=2, decimal_places=0)
    copiasnotadeconsumo = models.DecimalField(max_digits=2, decimal_places=0)
    copiasticketmovil = models.DecimalField(max_digits=2, decimal_places=0)
    autorizacionmonedero = models.IntegerField(blank=True, null=True)
    vigianotificar = models.IntegerField()
    archivoejecutarfincierreturno = models.CharField(max_length=150, blank=True, null=True)
    archivoejecutariniciocierreturno = models.CharField(max_length=150, blank=True, null=True)
    ejecutarfincierreturno = models.BooleanField(blank=True, null=True)
    ejecutariniciocierreturno = models.BooleanField(blank=True, null=True)
    esperarejecutarfincierreturno = models.BooleanField(blank=True, null=True)
    esperarejecutariniciocierreturno = models.BooleanField(blank=True, null=True)
    autorizacionregistroasistencia = models.IntegerField()
    ejecutararchivoiniciocierreturno = models.BooleanField()
    ejecutararchivofincierreturno = models.BooleanField()
    rutaarchivoiniciocierreturno = models.CharField(max_length=150, blank=True, null=True)
    rutaarchivofincierreturno = models.CharField(max_length=150, blank=True, null=True)
    ejecarchpagarcta = models.BooleanField()
    archejecpagarcta = models.CharField(max_length=200)
    paramejecpagarcta = models.CharField(max_length=200)
    formato_cfdi_33_persona = models.CharField(max_length=80)
    formato_cfdi_33_empresa = models.CharField(max_length=80)
    formato_cfdi_33_publico = models.CharField(max_length=80)
    abrecajonparacontar = models.IntegerField()
    scaleinputstring = models.CharField(max_length=3)
    tkc_numcaja = models.IntegerField(db_column='TKC_NumCaja')  # Field name made lowercase.
    seriecomplementopago = models.CharField(max_length=15, blank=True, null=True)
    habilitapinpad = models.BooleanField()
    ip_pinpad = models.CharField(db_column='IP_pinpad', max_length=100)  # Field name made lowercase.
    puerto_pinpad = models.CharField(max_length=100)
    seriefactglobal = models.CharField(db_column='serieFactGlobal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    almacensalida_elabora = models.CharField(max_length=5)
    almacenentrada_elabora = models.CharField(max_length=5)
    ejecarchfactura = models.IntegerField()
    archarchfactura = models.CharField(max_length=150, blank=True, null=True)
    paramarchfactura = models.CharField(max_length=200, blank=True, null=True)
    areatipoventarapida = models.CharField(max_length=5)
    mercadopagoposid = models.CharField(db_column='MercadoPagoPosId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    usemercadopago = models.BooleanField(db_column='UseMercadoPago', blank=True, null=True)  # Field name made lowercase.
    idformatokiosco = models.CharField(max_length=5, blank=True, null=True)
    copiasticketkiosco = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    modo_operacion = models.SmallIntegerField()
    ejecarchcancelarfactura = models.IntegerField()
    archcancelarfactura = models.CharField(max_length=150, blank=True, null=True)
    paramarchcancelarfactura = models.CharField(max_length=200, blank=True, null=True)
    posisopen = models.BooleanField(db_column='PosIsOpen')  # Field name made lowercase.
    poslastonline = models.DateTimeField(db_column='PosLastOnline')  # Field name made lowercase.
    prefijo_bascula = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    monitorcorte_servidor = models.BooleanField()
    monitorcorte_ejecutando = models.BooleanField()
    sistemamaximizado = models.BooleanField()
    gazebo_eg = models.BooleanField()
    bracelet_enum_payment = models.SmallIntegerField()
    idalmacen = models.CharField(max_length=5, blank=True, null=True)
    only_areas_fastfood = models.BooleanField()
    fastfood_type_mode = models.IntegerField()
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estaciones'


class Estacionesalmacen(models.Model):
    idproducto = models.CharField(max_length=15)
    idestacion = models.CharField(max_length=40)
    idalmacen = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'estacionesalmacen'


class Estacionesareas(models.Model):
    idestacion = models.ForeignKey(Estaciones, models.DO_NOTHING, db_column='idestacion', blank=True, null=True)
    idarea = models.ForeignKey(Areas, models.DO_NOTHING, db_column='idarea', blank=True, null=True)
    impresora = models.CharField(max_length=60, blank=True, null=True)
    imprimir = models.BooleanField(blank=True, null=True)
    saltos = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    autocutter = models.BooleanField(blank=True, null=True)
    empezarimp1 = models.CharField(max_length=3, blank=True, null=True)
    empezarimp2 = models.CharField(max_length=3, blank=True, null=True)
    empezarimp3 = models.CharField(max_length=3, blank=True, null=True)
    empezarimp4 = models.CharField(max_length=3, blank=True, null=True)
    empezarimp5 = models.CharField(max_length=3, blank=True, null=True)
    finalizarimp1 = models.CharField(max_length=3, blank=True, null=True)
    finalizarimp2 = models.CharField(max_length=3, blank=True, null=True)
    finalizarimp3 = models.CharField(max_length=3, blank=True, null=True)
    finalizarimp4 = models.CharField(max_length=3, blank=True, null=True)
    finalizarimp5 = models.CharField(max_length=3, blank=True, null=True)
    impresion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    comedor = models.BooleanField(blank=True, null=True)
    domicilio = models.BooleanField(blank=True, null=True)
    rapido = models.BooleanField(blank=True, null=True)
    tipodeimpresioncomanda = models.CharField(max_length=1, blank=True, null=True)
    nombrereportecomanda = models.CharField(max_length=150, blank=True, null=True)
    copias = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estacionesareas'


class Estados(models.Model):
    idestado = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idpais = models.ForeignKey('Paises', models.DO_NOTHING, db_column='idpais', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


class Etiquetaslenguaje(models.Model):
    ididioma = models.ForeignKey('Idiomas', models.DO_NOTHING, db_column='ididioma', blank=True, null=True)
    idetiqueta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    valor = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etiquetaslenguaje'


class Explosioninsumosdetalle(models.Model):
    idexplosion = models.ForeignKey('Explosionproductos', models.DO_NOTHING, db_column='idexplosion')
    idproducto = models.CharField(max_length=15)
    idinsumo = models.CharField(max_length=15)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4)
    costo = models.DecimalField(max_digits=19, decimal_places=4)
    costopromedio = models.DecimalField(max_digits=19, decimal_places=4)
    unidad = models.CharField(max_length=10)
    rendimientoelaborado = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    elaborado = models.BooleanField()
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    idelaborado = models.CharField(max_length=15)
    nivel = models.SmallIntegerField()
    ordengenerada = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'explosioninsumosdetalle'


class Explosionproductos(models.Model):
    folio = models.IntegerField()
    fecha = models.DateTimeField()
    usuario = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=100)
    estatus = models.SmallIntegerField()
    explosionparaordencompra = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'explosionproductos'


class Explosionproductosdetalle(models.Model):
    id = models.ForeignKey(Explosionproductos, models.DO_NOTHING, db_column='id')
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto')
    cantidad = models.DecimalField(max_digits=14, decimal_places=4)
    id_epd = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'explosionproductosdetalle'


class Facturas(models.Model):
    idfactura = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    serie = models.CharField(max_length=15, blank=True, null=True)
    folio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    cancelada = models.BooleanField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    concepto = models.CharField(max_length=180, blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    idturno = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    impresiones = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigocontrolbolivia = models.CharField(max_length=30, blank=True, null=True)
    propinafacturada = models.BooleanField(blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    femexelectronico = models.BooleanField(blank=True, null=True)
    femextipocliente = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    femexxmlvalido = models.TextField(blank=True, null=True)  # This field type is a guess.
    femexcadenaoriginal = models.TextField(blank=True, null=True)  # This field type is a guess.
    femexsello = models.TextField(blank=True, null=True)  # This field type is a guess.
    femexnumcertificado = models.CharField(max_length=50, blank=True, null=True)
    femexanioaprobacion = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    femexnumaprobacion = models.CharField(max_length=30, blank=True, null=True)
    fechacancelacion = models.DateTimeField(blank=True, null=True)
    femexdeclarado = models.BooleanField(blank=True, null=True)
    femexdeclaradocancelado = models.BooleanField(blank=True, null=True)
    femexmodogenerado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    femexrfc = models.CharField(max_length=20, blank=True, null=True)
    femexcbb = models.BinaryField(blank=True, null=True)
    tipoesquema = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    uidtimbre = models.TextField(blank=True, null=True)  # This field type is a guess.
    timbrenocertificadosat = models.TextField(db_column='TimbrenoCertificadoSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timbrefechatimbrado = models.CharField(db_column='TimbreFechaTimbrado', max_length=25, blank=True, null=True)  # Field name made lowercase.
    timbresellocfd = models.TextField(db_column='TimbreselloCFD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timbresellosat = models.TextField(db_column='TimbreselloSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timbrecadenaoriginal = models.TextField(db_column='TimbreCadenaOriginal', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    imagencfdi = models.BinaryField(db_column='ImagenCFDI', blank=True, null=True)  # Field name made lowercase.
    femexretencion1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    femexretencion2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    femexretencion3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ncf = models.CharField(max_length=19, blank=True, null=True)
    regimen = models.CharField(max_length=100, blank=True, null=True)
    formapago = models.CharField(max_length=200, blank=True, null=True)
    numerocuenta = models.CharField(max_length=140, blank=True, null=True)
    expedidoen = models.CharField(max_length=200, blank=True, null=True)
    idunidad = models.CharField(max_length=200, blank=True, null=True)
    pac_reprocesado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    pac_enviado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    folios_central = models.BooleanField(blank=True, null=True)
    pac = models.IntegerField()
    acusecancelacion = models.TextField()  # This field type is a guess.
    rifdetallado = models.BooleanField(db_column='RIFDetallado')  # Field name made lowercase.
    femexenviado = models.BooleanField()
    impuesto1 = models.DecimalField(max_digits=19, decimal_places=4)
    impuesto2 = models.DecimalField(max_digits=19, decimal_places=4)
    impuesto3 = models.DecimalField(max_digits=19, decimal_places=4)
    numautorizacionbolivia = models.CharField(max_length=30)
    descuento = models.DecimalField(max_digits=19, decimal_places=4)
    complementoine = models.BooleanField()
    tipodecambio = models.DecimalField(max_digits=15, decimal_places=4)
    moneda = models.IntegerField()
    esfoliofiscal = models.BooleanField()
    condicionesdepago = models.CharField(max_length=250)
    leyendadesglosefolios = models.CharField(db_column='leyendaDesgloseFolios', max_length=250)  # Field name made lowercase.
    ordenleyendadesglosefolios = models.SmallIntegerField(db_column='ordenLeyendaDesgloseFolios')  # Field name made lowercase.
    versionfacturacion = models.DecimalField(max_digits=16, decimal_places=6)
    cpcliente_sat = models.CharField(db_column='cpcliente_SAT', max_length=15)  # Field name made lowercase.
    idusocfdi_sat = models.CharField(db_column='idusocfdi_SAT', max_length=50)  # Field name made lowercase.
    cfdirelacionado_sat = models.CharField(db_column='cfdirelacionado_SAT', max_length=50)  # Field name made lowercase.
    idprodserv_sat = models.CharField(db_column='idprodserv_SAT', max_length=50)  # Field name made lowercase.
    idunidad_sat = models.CharField(db_column='idunidad_SAT', max_length=50)  # Field name made lowercase.
    idmetodopago_sat = models.CharField(db_column='idmetodopago_SAT', max_length=50)  # Field name made lowercase.
    idpaiscliente_sat = models.CharField(db_column='idpaiscliente_SAT', max_length=50)  # Field name made lowercase.
    nombre_emisor = models.CharField(max_length=254)
    idregimen_sat = models.CharField(db_column='idregimen_SAT', max_length=50)  # Field name made lowercase.
    cpemisor_sat = models.CharField(db_column='cpemisor_SAT', max_length=15)  # Field name made lowercase.
    factura_agrupada = models.BooleanField()
    des_gt_fechavigencia = models.DateTimeField(db_column='Des_GT_fechavigencia')  # Field name made lowercase.
    des_gt_consecutivoinicio = models.DecimalField(db_column='Des_GT_consecutivoinicio', max_digits=10, decimal_places=0)  # Field name made lowercase.
    des_gt_consecutivofin = models.DecimalField(db_column='Des_GT_consecutivofin', max_digits=10, decimal_places=0)  # Field name made lowercase.
    des_gt_fechaaprobacion = models.DateTimeField(db_column='Des_GT_fechaaprobacion')  # Field name made lowercase.
    pendientecancelacion = models.BooleanField()
    fechaenviopendiente = models.DateTimeField(blank=True, null=True)
    usuarioenviopendiente = models.CharField(max_length=15)
    tipocancelacion = models.SmallIntegerField()
    escancelable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'facturas'


class FacturasRep(models.Model):
    idfactura_rep = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=15)
    folio = models.IntegerField()
    fecha = models.DateTimeField()
    cancelada = models.BooleanField()
    versionfacturacion = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4)
    moneda = models.CharField(max_length=5)
    total = models.DecimalField(max_digits=19, decimal_places=4)
    lugarexpedicion = models.CharField(max_length=15)
    rfc_emisor = models.CharField(max_length=20)
    nombre_emisor = models.CharField(max_length=254)
    idregimen_sat = models.CharField(db_column='idregimen_SAT', max_length=50)  # Field name made lowercase.
    rfc_receptor = models.CharField(max_length=20)
    nombre_receptor = models.CharField(max_length=254)
    femexxmlvalido = models.TextField()  # This field type is a guess.
    tipodecambio = models.DecimalField(max_digits=16, decimal_places=6)
    enviado = models.BooleanField()
    fechaenviado = models.DateTimeField()
    intentoenvioaf = models.IntegerField(db_column='intentoEnvioAF')  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    uuidtimbre = models.TextField(db_column='uuidTimbre')  # Field name made lowercase. This field type is a guess.
    usuariocancelo = models.CharField(max_length=15)
    fechacancela = models.DateTimeField(blank=True, null=True)
    acusecancelacion = models.TextField()  # This field type is a guess.
    usuariofactura = models.CharField(max_length=15)
    pendientecancelacion = models.BooleanField()
    fechaenviopendiente = models.DateTimeField(blank=True, null=True)
    usuarioenviopendiente = models.CharField(max_length=15)
    tipocancelacion = models.SmallIntegerField()
    escancelable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'facturas_rep'


class FacturasRepDoctos(models.Model):
    idfact_rep_docto = models.AutoField(primary_key=True)
    idfact_rep_pago = models.ForeignKey('FacturasRepPagos', models.DO_NOTHING, db_column='idfact_rep_pago')
    iddocumento = models.TextField()  # This field type is a guess.
    serie = models.CharField(max_length=15)
    folio = models.IntegerField()
    monedadr = models.CharField(max_length=10)
    tipocambiodr = models.DecimalField(max_digits=16, decimal_places=6)
    metododepagodr = models.CharField(max_length=5)
    numparcialidad = models.SmallIntegerField()
    impsaldoant = models.DecimalField(max_digits=19, decimal_places=4)
    imppagado = models.DecimalField(max_digits=19, decimal_places=4)
    impsaldoinsoluto = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'facturas_rep_doctos'


class FacturasRepPagos(models.Model):
    idfact_rep_pago = models.AutoField(primary_key=True)
    idfactura_rep = models.ForeignKey(FacturasRep, models.DO_NOTHING, db_column='idfactura_rep')
    fechapago = models.DateTimeField()
    formadepagop = models.CharField(max_length=5)
    monedap = models.CharField(max_length=5)
    monto = models.DecimalField(max_digits=19, decimal_places=4)
    numoperacion = models.CharField(max_length=100)
    rfcemisorctaord = models.CharField(max_length=20)
    nombancoordext = models.CharField(max_length=250)
    ctaordenante = models.CharField(max_length=50)
    rfcemisorctaben = models.CharField(max_length=20)
    ctabeneficiario = models.CharField(max_length=50)
    tipocadpago = models.CharField(max_length=10)
    certpago = models.TextField()  # This field type is a guess.
    cadpago = models.TextField()  # This field type is a guess.
    sellopago = models.TextField()  # This field type is a guess.
    tipocambiop = models.DecimalField(max_digits=16, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'facturas_rep_pagos'


class Facturascfdipendientesregistrar(models.Model):
    idfactura = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='idfactura', blank=True, null=True)
    procesado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    fechaprocesado = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturascfdipendientesregistrar'


class Facturascomplementoine(models.Model):
    idfacturascomplementoine = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    version = models.CharField(max_length=10)
    tipoproceso = models.CharField(max_length=10)
    tipocomite = models.CharField(max_length=20)
    idcontabilidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturascomplementoine'


class Facturasentidadesine(models.Model):
    idfacturasentidadesine = models.AutoField(primary_key=True)
    idfacturascomplementoine = models.ForeignKey(Facturascomplementoine, models.DO_NOTHING, db_column='idfacturascomplementoine')
    claveentidad = models.CharField(max_length=3)
    ambito = models.CharField(max_length=10)
    contabilidad = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'facturasentidadesine'


class Facturasmovtos(models.Model):
    idfactura = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    precio = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    retencion1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retencion2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retencion3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    idunidad = models.CharField(max_length=50, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2)
    versionfacturacion = models.DecimalField(max_digits=16, decimal_places=6)
    idprodserv_sat = models.CharField(db_column='idprodserv_SAT', max_length=50)  # Field name made lowercase.
    idunidadmedida_sat = models.CharField(db_column='idunidadmedida_SAT', max_length=50)  # Field name made lowercase.
    descuentoimporte = models.DecimalField(max_digits=20, decimal_places=6)
    subtotal = models.DecimalField(max_digits=20, decimal_places=6)
    importeimpuesto1 = models.DecimalField(max_digits=20, decimal_places=6)
    importeimpuesto2 = models.DecimalField(max_digits=20, decimal_places=6)
    importeimpuesto3 = models.DecimalField(max_digits=20, decimal_places=6)
    importeretencion1 = models.DecimalField(max_digits=20, decimal_places=6)
    importeretencion2 = models.DecimalField(max_digits=20, decimal_places=6)
    importeretencion3 = models.DecimalField(max_digits=20, decimal_places=6)
    total = models.DecimalField(max_digits=20, decimal_places=6)
    excentoimpuestos = models.BooleanField()
    foliodet = models.BigIntegerField()
    movimiento = models.BigIntegerField()
    importe = models.DecimalField(max_digits=20, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'facturasmovtos'


class Folios(models.Model):
    serie = models.CharField(max_length=15, blank=True, null=True)
    ultimofolio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ultimaorden = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    ultimofolionotadeconsumo = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    ultimofolioproduccion = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    autorizacion = models.CharField(max_length=50, blank=True, null=True)
    fechalimite = models.DateTimeField(blank=True, null=True)
    rangoautinicio = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    rangoautfin = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    sincronizar_autofactura = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'folios'


class Foliosalmacen(models.Model):
    folio = models.BigIntegerField(primary_key=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    folioalmacen = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    foliomovto = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    nota = models.CharField(max_length=150, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    editadosucursal = models.BooleanField(blank=True, null=True)
    foliocentral = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foliosalmacen'


class Foliosfacturados(models.Model):
    idfactura = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    folio = models.BigIntegerField(blank=True, null=True)
    porcentajefac = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foliosfacturados'


class Foliosfacturas(models.Model):
    serie = models.CharField(max_length=15, blank=True, null=True)
    ultimofolio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    electronico = models.BooleanField(blank=True, null=True)
    consecutivoinicio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    consecutivofin = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    anioaprobacion = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    numaprobacion = models.CharField(max_length=30, blank=True, null=True)
    estatus = models.BooleanField(blank=True, null=True)
    cbb = models.BinaryField(blank=True, null=True)
    tipoesquema = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    fechaaprobacion = models.CharField(max_length=10, blank=True, null=True)
    ultimofoliocentral = models.CharField(max_length=250, blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    des_gt_folioguatemala = models.BooleanField(db_column='Des_GT_folioguatemala')  # Field name made lowercase.
    des_gt_fechaaprobacion = models.DateTimeField(db_column='Des_GT_fechaaprobacion')  # Field name made lowercase.
    des_gt_fechaingreso = models.DateTimeField(db_column='Des_GT_fechaingreso')  # Field name made lowercase.
    des_gt_fechavigencia = models.DateTimeField(db_column='Des_GT_fechavigencia')  # Field name made lowercase.
    des_gt_avisovencimiento = models.DecimalField(db_column='Des_GT_avisovencimiento', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    complementopago = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'foliosfacturas'


class Formasdepago(models.Model):
    idformadepago = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    solicitareferencia = models.BooleanField(blank=True, null=True)
    prioridadboton = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cuentacontableimporte = models.CharField(max_length=5, blank=True, null=True)
    cuentacontablecomision = models.CharField(max_length=5, blank=True, null=True)
    cuentacontableivacomision = models.CharField(max_length=5, blank=True, null=True)
    comision = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    aceptapropina = models.BooleanField(blank=True, null=True)
    subtipo = models.SmallIntegerField(blank=True, null=True)
    prefijo1 = models.CharField(max_length=3, blank=True, null=True)
    prefijo2 = models.CharField(max_length=3, blank=True, null=True)
    codigodeprefijoconsulta = models.CharField(max_length=10, blank=True, null=True)
    codigodeprefijoacumred = models.CharField(max_length=10, blank=True, null=True)
    generapuntos = models.BooleanField(blank=True, null=True)
    formatoimpresion = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    idfpagofiscal = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pagoenlinea = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipotarjeta = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    nofacturable = models.BooleanField(blank=True, null=True)
    comisionreporte1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    comisionreporte2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipotarjetabancaria = models.SmallIntegerField(db_column='tipoTarjetaBancaria')  # Field name made lowercase.
    idtipodescuento = models.CharField(max_length=5)
    idformapago_sat = models.CharField(db_column='idformapago_SAT', max_length=50)  # Field name made lowercase.
    servicecode = models.ForeignKey('Servicecodes', models.DO_NOTHING, db_column='servicecode', blank=True, null=True)
    leerbrazalete = models.BooleanField()
    cargohabitacion_eg = models.BooleanField()
    visible_kiosco = models.BooleanField()
    autocapturar = models.BooleanField()
    sumatotal = models.BooleanField()
    equivalencia = models.CharField(max_length=30, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formasdepago'


class FormasdepagoAppArea(models.Model):
    fkidformadepago = models.ForeignKey(Formasdepago, models.DO_NOTHING, db_column='FKidformadepago')  # Field name made lowercase.
    fkidarearestaurant = models.ForeignKey(Areasrestaurant, models.DO_NOTHING, db_column='FKidarearestaurant')  # Field name made lowercase.
    fkapp = models.ForeignKey(AppList, models.DO_NOTHING, db_column='FKapp_id', to_field='app_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formasdepago_app_area'


class Formasdepagodetalle(models.Model):
    idformadepago = models.CharField(max_length=5)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    solicitareferencia = models.BooleanField(blank=True, null=True)
    prioridadboton = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cuentacontableimporte = models.CharField(max_length=5, blank=True, null=True)
    cuentacontablecomision = models.CharField(max_length=5, blank=True, null=True)
    cuentacontableivacomision = models.CharField(max_length=5, blank=True, null=True)
    comision = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    aceptapropina = models.BooleanField(blank=True, null=True)
    generapuntos = models.BooleanField(blank=True, null=True)
    nofacturable = models.BooleanField(blank=True, null=True)
    idempresa = models.CharField(max_length=15)
    descargar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formasdepagodetalle'


class Formatofacturas(models.Model):
    idformato = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fila = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    columna = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    campo = models.CharField(max_length=250, blank=True, null=True)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formatofacturas'


class FormatofacturasPadre(models.Model):
    idformato = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    facturassumarlineascuerpoapie = models.BooleanField(blank=True, null=True)
    facturaslineasmaximo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formatofacturas_padre'


class Formatos(models.Model):
    idformato = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    anchopapel = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    saltosinicio = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    saltosfinalizar = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    resumirimpresion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    imprimirpreciocero = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipoformato = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipoimpresora = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipoformatovario = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    imprimirlogo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    archivologo = models.CharField(max_length=50, blank=True, null=True)
    imprimirimagenpie = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    imagenpie = models.TextField(blank=True, null=True)
    archivoimagenpie = models.CharField(max_length=50, blank=True, null=True)
    rutalogo = models.CharField(max_length=500, blank=True, null=True)
    rutapie = models.CharField(max_length=500, blank=True, null=True)
    resumiragruparmodificadores = models.BooleanField()
    ordenalfabetico = models.BooleanField()
    af_imprimirqr = models.BooleanField(db_column='AF_imprimirQR')  # Field name made lowercase.
    col_imprimirqr = models.BooleanField(db_column='COL_imprimirQR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formatos'


class Formatosdetalle(models.Model):
    idformato = models.CharField(max_length=5)
    idcampo = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    orden = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    campo = models.CharField(max_length=400, blank=True, null=True)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    aliascampo = models.CharField(max_length=40, blank=True, null=True)
    nombrecampo = models.CharField(max_length=254, blank=True, null=True)
    etiqueta = models.CharField(max_length=30, blank=True, null=True)
    fila = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    columna = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    caracteres = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    caracteresinicio = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    idcomando = models.CharField(max_length=5, blank=True, null=True)
    moneda = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    noimprimirvacios = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    alineacion = models.CharField(max_length=5, blank=True, null=True)
    limitartamano = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    decimales = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    noimprimirfilavacio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    alinear = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipoalineacion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    rellenar = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    rellenarcantidad = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    rellenarcaracter = models.CharField(max_length=1, blank=True, null=True)
    numerico = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formatosdetalle'


class Formatosvarios(models.Model):
    idformato = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fila = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    columna = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    campo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formatosvarios'


class Gastos(models.Model):
    idgasto = models.DecimalField(primary_key=True, max_digits=7, decimal_places=0)
    fecha = models.DateTimeField(blank=True, null=True)
    idcuentacontable = models.ForeignKey(Cuentascontables, models.DO_NOTHING, db_column='idcuentacontable', blank=True, null=True)
    referencia = models.CharField(max_length=50, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    idcompra = models.ForeignKey(Compras, models.DO_NOTHING, db_column='idcompra', blank=True, null=True)
    idtipogasto = models.ForeignKey('Tipogastos', models.DO_NOTHING, db_column='Idtipogasto', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    idsubtipogastos = models.CharField(max_length=5, blank=True, null=True)
    observaciones = models.CharField(max_length=60, blank=True, null=True)
    tipodemovimiento = models.CharField(max_length=30, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    editadosucursal = models.BooleanField(blank=True, null=True)
    foliofactura = models.CharField(max_length=20, blank=True, null=True)
    idgastocentral = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    idproveedor = models.CharField(max_length=15, blank=True, null=True)
    folio = models.CharField(max_length=15, blank=True, null=True)
    enviadoaf = models.BooleanField(db_column='EnviadoAF')  # Field name made lowercase.
    intentoenvioaf = models.IntegerField(db_column='IntentoEnvioAF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gastos'


class Gastosmovtos(models.Model):
    idgasto = models.ForeignKey(Gastos, models.DO_NOTHING, db_column='idgasto', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gastosmovtos'


class Grupoformasdepago(models.Model):
    idgrupoformadepago = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupoformasdepago'


class Grupoformasdepagodet(models.Model):
    iddetalle = models.DecimalField(max_digits=11, decimal_places=0)
    idgrupoformadepago = models.ForeignKey(Grupoformasdepago, models.DO_NOTHING, db_column='idgrupoformadepago', blank=True, null=True)
    idformadepago = models.ForeignKey(Formasdepago, models.DO_NOTHING, db_column='idformadepago', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupoformasdepagodet'


class Grupos(models.Model):
    idgrupo = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    clasificacion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    prioridad = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    color = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    colorletra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    prioridadimpresion = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cambiacolorcuenta = models.BooleanField(blank=True, null=True)
    colorcuenta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    colorletracuenta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitaautorizacion = models.BooleanField(blank=True, null=True)
    imagenmenuelectronico = models.BinaryField(blank=True, null=True)
    extmenu = models.CharField(max_length=5, blank=True, null=True)
    porcentajepropina = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    imagen_menu = models.TextField(blank=True, null=True)
    id_etiqueta = models.CharField(max_length=50)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    alcohol = models.BooleanField()
    servicecode = models.ForeignKey('Servicecodes', models.DO_NOTHING, db_column='servicecode', blank=True, null=True)
    idbo = models.IntegerField(db_column='IdBO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grupos'


class Gruposdeproductosvisibles(models.Model):
    idestacion = models.CharField(max_length=40, blank=True, null=True)
    idgrupo = models.CharField(max_length=5, blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    visiblesiempre = models.BooleanField(blank=True, null=True)
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    lunesdiafin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    martesdiafin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    miercolesdiafin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    juevesdiafin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    viernesdiafin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    sabadodiafin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    domingodiafin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    aplicalunes = models.BooleanField(blank=True, null=True)
    aplicamartes = models.BooleanField(blank=True, null=True)
    aplicamiercoles = models.BooleanField(blank=True, null=True)
    aplicajueves = models.BooleanField(blank=True, null=True)
    aplicaviernes = models.BooleanField(blank=True, null=True)
    aplicasabado = models.BooleanField(blank=True, null=True)
    aplicadomingo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gruposdeproductosvisibles'


class Gruposi(models.Model):
    idgruposi = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    idgruposiclasificacion = models.ForeignKey('Gruposiclasificacion', models.DO_NOTHING, db_column='idgruposiclasificacion', blank=True, null=True)
    idcuentacontable = models.CharField(max_length=5, blank=True, null=True)
    idtipopedido = models.CharField(max_length=5, blank=True, null=True)
    prioridad = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gruposi'


class Gruposiclasificacion(models.Model):
    idgruposiclasificacion = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    clasificacionventa = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gruposiclasificacion'


class Gruposmodificadores(models.Model):
    idgruposmodificadores = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    id_etiqueta = models.CharField(max_length=50)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idbo = models.IntegerField(db_column='IdBO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gruposmodificadores'


class Gruposmodificadoresproductos(models.Model):
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idgruposmodificadores = models.ForeignKey(Gruposmodificadores, models.DO_NOTHING, db_column='idgruposmodificadores', blank=True, null=True)
    incluidos = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    prioridad = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    forzarcaptura = models.BooleanField(blank=True, null=True)
    maximomodificadores = models.SmallIntegerField(blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    captura_incluido = models.BooleanField()
    id = models.CharField(primary_key=True, max_length=36)
    workspaceid = models.CharField(db_column='WorkspaceId', unique=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gruposmodificadoresproductos'


class Grupossubgrupos(models.Model):
    idgrupo = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='idgrupo', blank=True, null=True)
    idsubgrupo = models.ForeignKey('Subgrupos', models.DO_NOTHING, db_column='idsubgrupo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupossubgrupos'


class Horariosturnos(models.Model):
    idhorarioturno = models.IntegerField(blank=True, null=True)
    descripcionturno = models.CharField(max_length=30, blank=True, null=True)
    horainicial = models.CharField(max_length=11, blank=True, null=True)
    horafinal = models.CharField(max_length=11, blank=True, null=True)
    diasiguiente = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horariosturnos'


class Hotelmovtos(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=15, blank=True, null=True)
    habitacion = models.CharField(max_length=15, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    idmovtosh = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    transaction_id = models.CharField(max_length=250, blank=True, null=True)
    transactionid_cancelled = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotelmovtos'


class Huellaclientes(models.Model):
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    huella = models.TextField(blank=True, null=True)  # This field type is a guess.
    huella2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    pic = models.BinaryField(blank=True, null=True)
    tipolector = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huellaclientes'


class Huellameseros(models.Model):
    idmesero = models.CharField(max_length=4, blank=True, null=True)
    huella = models.TextField(blank=True, null=True)  # This field type is a guess.
    huella2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    pic = models.BinaryField(blank=True, null=True)
    tipolector = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huellameseros'


class Huellausuarios(models.Model):
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuario', blank=True, null=True)
    huella = models.TextField(blank=True, null=True)  # This field type is a guess.
    huella2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    pic = models.BinaryField(blank=True, null=True)
    tipolector = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huellausuarios'


class Idiomas(models.Model):
    ididioma = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    idiomadefault = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idiomas'


class IdiomasEtiquetas(models.Model):
    id = models.AutoField(primary_key=True)
    id_etiqueta = models.CharField(max_length=300)
    id_idioma = models.IntegerField()
    tipo = models.IntegerField()
    traduccion = models.CharField(max_length=1000)
    num_idioma = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'idiomas_etiquetas'


class IdiomasMenu(models.Model):
    id_idioma = models.IntegerField()
    nombre = models.CharField(max_length=300)
    traduccion = models.CharField(max_length=1000)
    prioridad = models.IntegerField()
    principal = models.BooleanField()
    habilitado = models.BooleanField()
    bandera = models.TextField()

    class Meta:
        managed = False
        db_table = 'idiomas_menu'


class Idiomasticket(models.Model):
    ididioma = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idcampo = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idiomasticket'


class Imagenbotones(models.Model):
    idestacion = models.CharField(max_length=40)
    nombreboton = models.CharField(max_length=100, blank=True, null=True)
    imagenboton = models.BinaryField(blank=True, null=True)
    imagenbotondeshabilitado = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenbotones'


class Impfiscalnotacreditolog(models.Model):
    idnota = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idturno = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    estacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impfiscalnotacreditolog'


class Imprimefiscalpendientes(models.Model):
    cheque = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    movimiento = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    estacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imprimefiscalpendientes'


class Impuestos(models.Model):
    idinsumo = models.ForeignKey('Insumos', models.DO_NOTHING, db_column='idinsumo')
    idregion = models.ForeignKey('Regiones', models.DO_NOTHING, db_column='idregion')
    impuesto1 = models.DecimalField(max_digits=7, decimal_places=2)
    impuesto2 = models.DecimalField(max_digits=7, decimal_places=2)
    impuesto3 = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'impuestos'


class Insumos(models.Model):
    idinsumo = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idgruposi = models.CharField(max_length=5, blank=True, null=True)
    unidad = models.CharField(max_length=10, blank=True, null=True)
    elaborado = models.BooleanField(blank=True, null=True)
    rendimientoelaborado = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    minutosalerta = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    minutospreparacion = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insumos'


class Insumoscostoproveedor(models.Model):
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    idpresentacion = models.CharField(max_length=15, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insumoscostoproveedor'


class Insumosdetalle(models.Model):
    idinsumo = models.ForeignKey(Insumos, models.DO_NOTHING, db_column='idinsumo')
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    inventariable = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costopromedio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    costoconimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    merma = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    descargar = models.BooleanField(blank=True, null=True)
    usarbasculainv = models.BooleanField(blank=True, null=True)
    alertaexistencias = models.BooleanField()
    estatus = models.IntegerField(blank=True, null=True)
    costoestandar = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idarea = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insumosdetalle'


class Insumoselaboracion(models.Model):
    movimiento = models.BigAutoField(primary_key=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    minutosalerta = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    minutospreparacion = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    horafinalizacion = models.DateTimeField(blank=True, null=True)
    usuarioautorizo = models.CharField(max_length=15, blank=True, null=True)
    usuariofinalizo = models.CharField(max_length=15, blank=True, null=True)
    aplicado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'insumoselaboracion'


class Insumospresentaciones(models.Model):
    idinsumospresentaciones = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    idgruposi = models.CharField(max_length=5, blank=True, null=True)
    rendimiento = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    unidad = models.CharField(max_length=50, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insumospresentaciones'


class Insumospresentacionesdetalle(models.Model):
    idinsumospresentaciones = models.ForeignKey(Insumospresentaciones, models.DO_NOTHING, db_column='idinsumospresentaciones')
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costopromedio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idproveedor = models.CharField(max_length=15, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    indicadorimpuesto = models.CharField(max_length=2, blank=True, null=True)
    stockminimogeneral = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    stockmaximogeneral = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    estatus = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    descargar = models.BooleanField(blank=True, null=True)
    ubicacion = models.CharField(max_length=150, blank=True, null=True)
    usarbasculainv = models.BooleanField(blank=True, null=True)
    costoestandar = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insumospresentacionesdetalle'


class Inventariopendiente(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    idconcepto = models.CharField(max_length=5, blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    idturno = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventariopendiente'


class Invfisico(models.Model):
    folio = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    fecha = models.DateTimeField(blank=True, null=True)
    idalmacen1 = models.CharField(max_length=5, blank=True, null=True)
    idalmacen2 = models.CharField(max_length=5, blank=True, null=True)
    inventarioteorico1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    inventariofisico1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    diferenciafisico1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    inventarioteorico2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    inventariofisico2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    diferenciafisico2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idinventario = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    editadosucursal = models.BooleanField(blank=True, null=True)
    foliocentral = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invfisico'


class Invfisicomovtos(models.Model):
    folio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    idpresentacion = models.CharField(max_length=15, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    existenciaalmacen1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fisicoalmacen1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    diferenciaalmacen1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    existenciaalmacen2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fisicoalmacen2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    diferenciaalmacen2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invfisicomovtos'


class JuegosPreciosporhora(models.Model):
    idtipomesa = models.CharField(max_length=15, blank=True, null=True)
    horainicio = models.CharField(max_length=5, blank=True, null=True)
    horafin = models.CharField(max_length=5, blank=True, null=True)
    findiasiguiente = models.BooleanField(blank=True, null=True)
    costoinicialbillar = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    costobillar = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'juegos_preciosporhora'


class Lectores(models.Model):
    clave = models.CharField(max_length=20, blank=True, null=True)
    llave = models.CharField(max_length=20, blank=True, null=True)
    seriefabricante = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lectores'


class Listadeprecios(models.Model):
    idlistaprecio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    clavemoneda = models.ForeignKey('Monedas', models.DO_NOTHING, db_column='clavemoneda', blank=True, null=True)
    estatus = models.BooleanField()
    listadefault = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'listadeprecios'


class Listadepreciosdetalle(models.Model):
    idlistaprecio = models.ForeignKey(Listadeprecios, models.DO_NOTHING, db_column='idlistaprecio')
    idlistapreciodetalle = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto')
    precio = models.DecimalField(max_digits=19, decimal_places=4)
    preciosinimpuesto = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'listadepreciosdetalle'


class LogRegistroDispositivos(models.Model):
    id_dispositivo = models.CharField(max_length=100)
    numerocontrol = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    vigencia_old = models.CharField(max_length=500)
    vigencia_new = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'log_registro_dispositivos'


class Logcambioprecios(models.Model):
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    precioanterior = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    precionuevo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    observaciones = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logcambioprecios'


class MapaMesas(models.Model):
    idmapa = models.CharField(max_length=5)
    mapa = models.CharField(max_length=50)
    idarearestaurante = models.CharField(max_length=5)
    mapa_actual = models.SmallIntegerField()
    color_fondo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipo_fondo = models.BooleanField(blank=True, null=True)
    textura_fondo = models.SmallIntegerField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idmapasistema = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mapa_mesas'


class Menu(models.Model):
    idmenu = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Menucomedor(models.Model):
    idmenucomedor = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idtipomenu = models.CharField(max_length=5, blank=True, null=True)
    estatus = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    aplicalunes = models.BooleanField(blank=True, null=True)
    aplicamartes = models.BooleanField(blank=True, null=True)
    aplicamiercoles = models.BooleanField(blank=True, null=True)
    aplicajueves = models.BooleanField(blank=True, null=True)
    aplicaviernes = models.BooleanField(blank=True, null=True)
    aplicasabado = models.BooleanField(blank=True, null=True)
    aplicadomingo = models.BooleanField(blank=True, null=True)
    lunesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    martesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    miercolesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    juevesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    viernesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sabadodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    domingodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menucomedor'


class Menucomedorproductos(models.Model):
    idmenucomedor = models.CharField(max_length=15, blank=True, null=True)
    iddia = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menucomedorproductos'


class Menuproductos(models.Model):
    idmenu = models.CharField(max_length=15, blank=True, null=True)
    idproducto = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menuproductos'


class Mesas(models.Model):
    idmesa = models.CharField(max_length=15)
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    personas = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fumar = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    estatus_ocupacion = models.SmallIntegerField(blank=True, null=True)
    idtipomesa = models.CharField(max_length=15, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idmesasistema = models.BigAutoField(primary_key=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mesas'


class Mesasasignadas(models.Model):
    idmesaasignada = models.AutoField(primary_key=True)
    idmesa = models.CharField(max_length=15, blank=True, null=True)
    folio = models.BigIntegerField(blank=True, null=True)
    activo = models.SmallIntegerField(blank=True, null=True)
    idmesero = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesasasignadas'


class Mesasbillar(models.Model):
    idmesa = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    estatus = models.BooleanField(blank=True, null=True)
    idtipomesa = models.CharField(max_length=15)
    iniciarmesacomedor = models.BooleanField()
    idmesacomedor = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesasbillar'


class Meseros(models.Model):
    idmeserointerno = models.BigAutoField(primary_key=True)
    idmesero = models.CharField(max_length=4)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    contraseña = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    fotografia = models.BinaryField(blank=True, null=True)
    visible = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    tipoacceso = models.BooleanField(blank=True, null=True)
    capturarestringidamesas = models.BooleanField(blank=True, null=True)
    perfil = models.CharField(max_length=15, blank=True, null=True)
    monitormeserocolorfondo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitormeserocolorletra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    accesoindicadormesas = models.BooleanField()
    turnoabierto = models.BooleanField()
    comision = models.DecimalField(max_digits=19, decimal_places=4)
    autorizaproductosmenuqr = models.BooleanField()
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'meseros'


class MicrosigaCentrosCostos(models.Model):
    idestacion = models.CharField(max_length=40, blank=True, null=True)
    clavecentros_costos = models.CharField(max_length=25, blank=True, null=True)
    centro_costos = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microsiga_centros_costos'


class MicrosigaRegistroErrores(models.Model):
    mensaje = models.CharField(max_length=250, blank=True, null=True)
    origen_error = models.CharField(max_length=25, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    clave_registro = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microsiga_registro_errores'


class Modificadores(models.Model):
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idmodificador = models.CharField(max_length=15, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idgruposmodificadores = models.ForeignKey(Gruposmodificadores, models.DO_NOTHING, db_column='idgruposmodificadores', blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modificadores'


class Monedas(models.Model):
    clavemoneda = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=25, blank=True, null=True)
    tipocambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monedas'


class Monedasmesero(models.Model):
    denominacion = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monedasmesero'


class Monederorangos(models.Model):
    ventarangoinicial = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ventarangofinal = models.DecimalField(db_column='Ventarangofinal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monederorangos'


class Monitorelaboradosestaciones(models.Model):
    idestacion = models.CharField(max_length=40, blank=True, null=True)
    idareamonitor = models.CharField(max_length=40, blank=True, null=True)
    coloralerta = models.CharField(max_length=40, blank=True, null=True)
    colorpreparacion = models.CharField(max_length=40, blank=True, null=True)
    teclaarriba = models.CharField(max_length=40, blank=True, null=True)
    teclaabajo = models.CharField(max_length=40, blank=True, null=True)
    teclaizquierda = models.CharField(max_length=40, blank=True, null=True)
    tecladerecha = models.CharField(max_length=40, blank=True, null=True)
    teclafinalizar = models.CharField(max_length=40, blank=True, null=True)
    teclaactualizar = models.CharField(max_length=40, blank=True, null=True)
    teclarepag = models.CharField(max_length=40, blank=True, null=True)
    teclaavpag = models.CharField(max_length=40, blank=True, null=True)
    tipomonitor = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ordenadesc = models.BooleanField()
    puertocomm = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitorelaboradosestaciones'


class Monitoresproduccion(models.Model):
    idmonitor = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    ipaddress = models.CharField(max_length=15, blank=True, null=True)
    port = models.CharField(max_length=4, blank=True, null=True)
    nummonitor = models.CharField(max_length=2, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monitoresproduccion'


class Monitorprodestaciones(models.Model):
    idmonitor = models.CharField(max_length=15, blank=True, null=True)
    idestacion = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitorprodestaciones'


class Motivoscancelacion(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    idmotivocancela = models.CharField(max_length=5, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    genera_desperdicio = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'motivoscancelacion'


class Movsinv(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    foliocheque = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    movto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idcompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    traspaso = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    invfisico = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idconcepto = models.ForeignKey(Conceptos, models.DO_NOTHING, db_column='idconcepto', blank=True, null=True)
    idinsumo = models.ForeignKey(Insumos, models.DO_NOTHING, db_column='idinsumo', blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    idturno = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    presentaciondestino = models.CharField(max_length=15, blank=True, null=True)
    idpedido = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movsinv'


class Movsinvcancelados(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    foliocheque = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    movto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idcompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    traspaso = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    invfisico = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idconcepto = models.CharField(max_length=5, blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    idalmacen = models.CharField(max_length=5, blank=True, null=True)
    idturno = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    presentaciondestino = models.CharField(max_length=15, blank=True, null=True)
    idpedido = models.BigIntegerField(blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movsinvcancelados'


class Movtosalmacen(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    movto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idcompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    traspaso = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    invfisico = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idconcepto = models.ForeignKey(Conceptos, models.DO_NOTHING, db_column='idconcepto', blank=True, null=True)
    idinsumospresentaciones = models.ForeignKey(Insumospresentaciones, models.DO_NOTHING, db_column='idinsumospresentaciones', blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    idpedido = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movtosalmacen'


class Movtosalmacencancelados(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    movto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idcompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    traspaso = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    invfisico = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idconcepto = models.CharField(max_length=5, blank=True, null=True)
    idinsumospresentaciones = models.CharField(max_length=15, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    idalmacen = models.CharField(max_length=5, blank=True, null=True)
    idpedido = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movtosalmacencancelados'


class Movtosbillar(models.Model):
    idmovto = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    idmesa = models.CharField(max_length=5, blank=True, null=True)
    hrainicio = models.DateTimeField(blank=True, null=True)
    hrafinal = models.DateTimeField(blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'movtosbillar'


class MovtosbillarPausas(models.Model):
    idmovto = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    inipausa = models.DateTimeField(blank=True, null=True)
    finpausa = models.DateTimeField(blank=True, null=True)
    motivopausa = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movtosbillar_pausas'


class Movtoscaja(models.Model):
    folio = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    foliomovto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idturno = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    concepto = models.CharField(max_length=60, blank=True, null=True)
    referencia = models.CharField(max_length=60, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    pagodepropina = models.BooleanField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idcashmovementtype = models.ForeignKey(Cashmovementstype, models.DO_NOTHING, db_column='IdCashMovementType', blank=True, null=True)  # Field name made lowercase.
    ismoneysafeguard = models.BooleanField(db_column='IsMoneySafeGuard', blank=True, null=True)  # Field name made lowercase.
    usuarioautoriza = models.CharField(max_length=15)
    pagodecomision = models.BooleanField()
    comisionista = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movtoscaja'


class Movtoscajadetalles(models.Model):
    folio = models.ForeignKey(Movtoscaja, models.DO_NOTHING, db_column='folio', blank=True, null=True)
    idturno = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    foliodet = models.BigIntegerField(blank=True, null=True)
    idformadepago = models.CharField(max_length=5, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movtoscajadetalles'


class Movtospatines(models.Model):
    idmovto = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    folio = models.CharField(max_length=10, blank=True, null=True)
    idpatin = models.CharField(max_length=15, blank=True, null=True)
    idservicio = models.CharField(max_length=15, blank=True, null=True)
    inicio = models.DateTimeField(blank=True, null=True)
    fin = models.DateTimeField(blank=True, null=True)
    estatus = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movtospatines'


class MpCuentadetalle(models.Model):
    id = models.BigAutoField(primary_key=True)
    folio = models.BigIntegerField(blank=True, null=True)
    idpropiedad = models.BigIntegerField(blank=True, null=True)
    pax = models.IntegerField(blank=True, null=True)
    habitacion = models.CharField(max_length=20, blank=True, null=True)
    nombreapellido = models.CharField(max_length=80, blank=True, null=True)
    mesa = models.CharField(max_length=100, blank=True, null=True)
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mp_cuentadetalle'


class MpPropiedades(models.Model):
    idpropiedad = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    predeterminado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mp_propiedades'


class MpTempcuentadetalle(models.Model):
    id = models.BigAutoField(primary_key=True)
    folio = models.BigIntegerField(blank=True, null=True)
    idpropiedad = models.BigIntegerField(blank=True, null=True)
    pax = models.IntegerField(blank=True, null=True)
    habitacion = models.CharField(max_length=20, blank=True, null=True)
    nombreapellido = models.CharField(max_length=80, blank=True, null=True)
    mesa = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mp_tempcuentadetalle'


class Ncomprobantesfiscales(models.Model):
    tiponcf = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fijo = models.CharField(max_length=11, blank=True, null=True)
    secini = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    secfin = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    consecutivo = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    consecutivomin = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    agotado = models.BooleanField(blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncomprobantesfiscales'


class Notificaciones(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    estatus_notificacion = models.BooleanField()
    foliocuenta = models.BigIntegerField()
    idcuenta = models.CharField(max_length=15)
    idmesero = models.CharField(max_length=10)
    mensaje = models.TextField()
    hora = models.DateTimeField()
    tipo_notificacion = models.IntegerField()
    hora_leido = models.DateTimeField()
    sistema_leido = models.IntegerField()
    idarearestaurant = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'notificaciones'


class NotificacionesAntifraudes(models.Model):
    fecha = models.DateTimeField()
    turno = models.BigIntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    idestacion = models.CharField(max_length=40, blank=True, null=True)
    reimpresiones = models.IntegerField(blank=True, null=True)
    reimpresionesmax = models.IntegerField(blank=True, null=True)
    enviarreimpresiones = models.BooleanField(blank=True, null=True)
    cancelacionescuenta = models.IntegerField(blank=True, null=True)
    cancelacionescuentamax = models.IntegerField(blank=True, null=True)
    enviarcancelacionescuenta = models.BooleanField(blank=True, null=True)
    cancelacionesprod = models.IntegerField(blank=True, null=True)
    cancelacionesprodmax = models.IntegerField(blank=True, null=True)
    enviarcancelacionesprod = models.BooleanField(blank=True, null=True)
    reaperturacuenta = models.IntegerField(blank=True, null=True)
    reaperturacuentamax = models.IntegerField(blank=True, null=True)
    enviarreaperturacuenta = models.BooleanField(blank=True, null=True)
    reaperturamismacuenta = models.IntegerField(blank=True, null=True)
    reaperturamismacuentamax = models.IntegerField(blank=True, null=True)
    enviarreaperturamismacuenta = models.BooleanField(blank=True, null=True)
    descuentocuenta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentocuentamax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    enviardescuentocuenta = models.BooleanField(blank=True, null=True)
    descuentoproductos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentoprodmax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    enviardescuentoprod = models.BooleanField(blank=True, null=True)
    enviado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificaciones_antifraudes'


class Notificacionesns(models.Model):
    idnotificacion = models.IntegerField()
    codigo = models.CharField(max_length=30, blank=True, null=True)
    titulo = models.CharField(max_length=250, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    fechainicio = models.DateTimeField(blank=True, null=True)
    fechafin = models.DateTimeField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    fechamodificacion = models.DateTimeField(blank=True, null=True)
    tiempodeespera = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notificacionesns'


class Nsplatformcontrol(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36)  # Field name made lowercase.
    entitytype = models.SmallIntegerField(db_column='EntityType')  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType')  # Field name made lowercase.
    issync = models.BooleanField(db_column='IsSync')  # Field name made lowercase.
    attempts = models.IntegerField(db_column='Attempts')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    syncdate = models.DateTimeField(db_column='SyncDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nsplatformcontrol'


class Nsplatforminventory(models.Model):
    workspaceid = models.CharField(db_column='WorkspaceId', primary_key=True, max_length=36)  # Field name made lowercase.
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    idinsumo = models.ForeignKey(Insumos, models.DO_NOTHING, db_column='idinsumo', blank=True, null=True)
    idpresentacion = models.CharField(max_length=15, blank=True, null=True)
    quantity = models.DecimalField(max_digits=14, decimal_places=6)
    averagecost = models.DecimalField(max_digits=19, decimal_places=4)
    lastdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nsplatforminventory'


class Nsplatformtaxes(models.Model):
    workspaceid = models.CharField(db_column='WorkspaceId', primary_key=True, max_length=36)  # Field name made lowercase.
    acronym = models.CharField(db_column='Acronym', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    islocal = models.BooleanField(db_column='IsLocal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nsplatformtaxes'


class Nsplatformtaxschemas(models.Model):
    workspaceid = models.CharField(db_column='WorkspaceId', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nsplatformtaxschemas'


class Nsplatformtaxschemasdetails(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    taxschemaid = models.ForeignKey(Nsplatformtaxschemas, models.DO_NOTHING, db_column='TaxSchemaId', blank=True, null=True)  # Field name made lowercase.
    taxid = models.ForeignKey(Nsplatformtaxes, models.DO_NOTHING, db_column='TaxId', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.SmallIntegerField(db_column='TaxType')  # Field name made lowercase.
    taxvalue = models.DecimalField(db_column='TaxValue', max_digits=9, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nsplatformtaxschemasdetails'


class Numerostarjetas(models.Model):
    foliocuenta = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    idformadepago = models.CharField(max_length=10, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=50, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioautorizo = models.CharField(max_length=20, blank=True, null=True)
    titulartarjetamonedero = models.CharField(max_length=100, blank=True, null=True)
    saldoanteriormonedero = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)
    sistema = models.SmallIntegerField()
    foliokiosco = models.CharField(max_length=36, blank=True, null=True)
    refidempresa = models.CharField(db_column='refIdEmpresa', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refnombreempresa = models.CharField(db_column='refNombreEmpresa', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'numerostarjetas'


class ObjetosMapa(models.Model):
    idobjetomapa = models.AutoField(primary_key=True)
    idmapa = models.CharField(max_length=5, blank=True, null=True)
    coordenadax = models.IntegerField(blank=True, null=True)
    coordenaday = models.IntegerField(blank=True, null=True)
    ancho = models.IntegerField(blank=True, null=True)
    alto = models.IntegerField(blank=True, null=True)
    tipoobjeto = models.IntegerField(blank=True, null=True)
    color = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    idobjeto = models.CharField(max_length=15, blank=True, null=True)
    rotacion = models.IntegerField(blank=True, null=True)
    textoobjeto = models.CharField(max_length=25, blank=True, null=True)
    color2 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipoaccesorio = models.SmallIntegerField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetos_mapa'


class OmnitransCatMensajes(models.Model):
    codigo = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    mensaje = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'omnitrans_cat_mensajes'


class OmnitransCatMovtos(models.Model):
    idmovtoomni = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=100)
    idcuentacontable = models.CharField(max_length=5, blank=True, null=True)
    tipomovto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'omnitrans_cat_movtos'


class OmnitransConfiguracion(models.Model):
    omni_ipotsuc = models.CharField(max_length=100, blank=True, null=True)
    omni_puerto = models.CharField(max_length=5, blank=True, null=True)
    omni_sucursal = models.CharField(max_length=5, blank=True, null=True)
    omni_pos = models.CharField(max_length=5, blank=True, null=True)
    omni_operador = models.CharField(max_length=5, blank=True, null=True)
    omni_secuencia = models.CharField(max_length=5, blank=True, null=True)
    omni_timeout = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    omni_trans = models.BooleanField(blank=True, null=True)
    omni_log = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'omnitrans_configuracion'


class Ordenescompra(models.Model):
    idordencompra = models.BigAutoField(primary_key=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    folio = models.CharField(max_length=15, blank=True, null=True)
    fechacaptura = models.DateTimeField(blank=True, null=True)
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    fecharecepcion = models.DateTimeField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    aplicada = models.BooleanField(blank=True, null=True)
    foliocompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    entregara = models.CharField(max_length=100, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    statusenviado = models.BooleanField(blank=True, null=True)
    fechahoraenviado = models.DateTimeField(blank=True, null=True)
    usuarioenvio = models.CharField(max_length=15, blank=True, null=True)
    ordensurtido = models.BooleanField(blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    editadosucursal = models.BooleanField(blank=True, null=True)
    idordencompracentral = models.BigIntegerField(blank=True, null=True)
    idexplosion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ordenescompra'


class Ordenescompramov(models.Model):
    idordencompra = models.ForeignKey(Ordenescompra, models.DO_NOTHING, db_column='idordencompra')
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    importesinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto1importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    importeconimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idpedido = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    idempresapedido = models.CharField(max_length=15, blank=True, null=True)
    idexplosion = models.IntegerField()
    idexplosioninsumosdetalle = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ordenescompramov'


class Pacs(models.Model):
    pac = models.IntegerField()
    nombrepac = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pacs'


class Pagosproveedores(models.Model):
    foliocompra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    abono = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    referencia = models.CharField(max_length=40, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    foliogasto = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagosproveedores'


class Paises(models.Model):
    idpais = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paises'


class Paquetes(models.Model):
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    idproductopaquete = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproductopaquete', blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paquetes'


class Parametros(models.Model):
    prioridadimpresiongruposproductos = models.BooleanField(blank=True, null=True)
    precioencomanda = models.BooleanField(blank=True, null=True)
    comandaencomanda = models.BooleanField(blank=True, null=True)
    bloqueartraspasosproductos = models.BooleanField(blank=True, null=True)
    mitclavecompania = models.CharField(max_length=5, blank=True, null=True)
    mitclavesucursal = models.CharField(max_length=8, blank=True, null=True)
    mitpais = models.CharField(max_length=8, blank=True, null=True)
    mitusuario = models.CharField(max_length=10, blank=True, null=True)
    mitclave = models.CharField(max_length=15, blank=True, null=True)
    mitnumeroafiliacion = models.CharField(max_length=10, blank=True, null=True)
    mittipooperacion = models.CharField(max_length=10, blank=True, null=True)
    miturl = models.CharField(max_length=150, blank=True, null=True)
    mitclavecompaniadolar = models.CharField(max_length=5, blank=True, null=True)
    mitclavesucursaldolar = models.CharField(max_length=8, blank=True, null=True)
    mitpaisdolar = models.CharField(max_length=8, blank=True, null=True)
    mitusuariodolar = models.CharField(max_length=10, blank=True, null=True)
    mitclavedolar = models.CharField(max_length=15, blank=True, null=True)
    mitnumeroafiliaciondolar = models.CharField(max_length=10, blank=True, null=True)
    mittipooperaciondolar = models.CharField(max_length=10, blank=True, null=True)
    mitclavecompaniadiferido = models.CharField(max_length=5, blank=True, null=True)
    mitclavesucursaldiferido = models.CharField(max_length=8, blank=True, null=True)
    mitpaisdiferido = models.CharField(max_length=8, blank=True, null=True)
    mitusuariodiferido = models.CharField(max_length=10, blank=True, null=True)
    mitclavediferido = models.CharField(max_length=15, blank=True, null=True)
    mitnumeroafiliaciondiferido = models.CharField(max_length=10, blank=True, null=True)
    mittipooperaciondiferido = models.CharField(max_length=10, blank=True, null=True)
    mitreferencia = models.CharField(max_length=150, blank=True, null=True)
    mitreferenciadolar = models.CharField(max_length=150, blank=True, null=True)
    mitreferenciadiferido = models.CharField(max_length=150, blank=True, null=True)
    inicializarventasalcierre = models.BooleanField(blank=True, null=True)
    monitorcolorfondoantes = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitorcolorletraantes = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitorcolorfondodespues = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitorcolorletradespues = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitortiempoactualizacion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    monitorcolorseparador = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mitnumeroafiliacionamex = models.CharField(max_length=10, blank=True, null=True)
    mitnumeroafiliaciondolaramex = models.CharField(max_length=10, blank=True, null=True)
    mitnumeroafiliaciondiferidoamex = models.CharField(max_length=10, blank=True, null=True)
    nombreidpoblacion = models.CharField(max_length=10, blank=True, null=True)
    nombreimpuesto1 = models.CharField(max_length=10, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nombreimpuesto2 = models.CharField(max_length=10, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nombreimpuesto3 = models.CharField(max_length=50, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    solicitarnotaofactura = models.BooleanField(blank=True, null=True)
    fechainicialfoliocortez = models.DateTimeField(blank=True, null=True)
    folioinicialcortez = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    numautorizacionbolivia = models.CharField(max_length=30, blank=True, null=True)
    llavedosificacionbolivia = models.CharField(max_length=254, blank=True, null=True)
    decimalesinventario = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    messenger = models.CharField(max_length=60, blank=True, null=True)
    correosoporte = models.CharField(max_length=60, blank=True, null=True)
    telefonooficinas = models.CharField(max_length=60, blank=True, null=True)
    correoventas = models.CharField(max_length=60, blank=True, null=True)
    polizatiposistema = models.CharField(max_length=10, blank=True, null=True)
    vecesimprimirformatoconcuenta = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ultimofolioimprimirformatoconcuenta = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    descuentosinivaencorte = models.BooleanField(blank=True, null=True)
    minutosbillar = models.IntegerField(blank=True, null=True)
    costobillar = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costoinicialbillar = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    conceptobillar = models.CharField(max_length=15, blank=True, null=True)
    reabrircancelarcuenta = models.BooleanField(blank=True, null=True)
    valesnogeneranotaconsumo = models.BooleanField(blank=True, null=True)
    facturasumarpropina = models.BooleanField(blank=True, null=True)
    cancelarcuentaalcancelarfactura = models.BooleanField(blank=True, null=True)
    passwordmonedero = models.CharField(max_length=6, blank=True, null=True)
    logtarjetacredito = models.BooleanField(blank=True, null=True)
    imprimircomandadecancelacion = models.BooleanField(blank=True, null=True)
    comandaindividualseparador = models.BooleanField(blank=True, null=True)
    monitornivelprioridad = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    monitorprioridadactual = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    minutossegundotiempomonitor = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    minutostercertiempomonitor = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    usarsecuenciatiemposmonitor = models.BooleanField(blank=True, null=True)
    forzartipodescuento = models.BooleanField(blank=True, null=True)
    conceptoentradarepcostos = models.CharField(max_length=5, blank=True, null=True)
    conceptosalidarepcostos = models.CharField(max_length=5, blank=True, null=True)
    mintoleranciap = models.IntegerField(blank=True, null=True)
    servextrapatin = models.CharField(max_length=15, blank=True, null=True)
    ciudaddefault = models.CharField(max_length=30, blank=True, null=True)
    estadodefault = models.CharField(max_length=30, blank=True, null=True)
    paisdefault = models.CharField(max_length=30, blank=True, null=True)
    passwordsalirsistema = models.BooleanField(blank=True, null=True)
    idccivacompras = models.CharField(max_length=15, blank=True, null=True)
    patinestipofoliobusqueda = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    prefijopolizadecompras = models.CharField(max_length=5, blank=True, null=True)
    comandaporproducto = models.BooleanField(blank=True, null=True)
    mitventadirecta = models.BooleanField(blank=True, null=True)
    clientesdomicilioanchoclave = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    idproductoabonorestcard = models.CharField(max_length=15, blank=True, null=True)
    serviciorapidomesero = models.BooleanField(blank=True, null=True)
    serviciorapidomeseropassword = models.BooleanField(blank=True, null=True)
    formatocomedorcomentario = models.BooleanField(blank=True, null=True)
    formatodomiciliocomentario = models.BooleanField(blank=True, null=True)
    formatorapidocomentario = models.BooleanField(blank=True, null=True)
    costopromedioformula = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    inventarionegativoventa = models.BooleanField(blank=True, null=True)
    servidormail = models.CharField(max_length=120, blank=True, null=True)
    puerto = models.CharField(max_length=20, blank=True, null=True)
    autentificacion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    passwordemail = models.CharField(max_length=250, blank=True, null=True)
    nombredesplegado = models.CharField(max_length=100, blank=True, null=True)
    asunto = models.CharField(max_length=120, blank=True, null=True)
    eliminarprodfiscal = models.BooleanField(blank=True, null=True)
    titulocortez = models.CharField(max_length=30, blank=True, null=True)
    campoadicionalcortez = models.CharField(max_length=200, blank=True, null=True)
    meserospuedereservaciones = models.BooleanField(blank=True, null=True)
    mostrarventafacturadacorte = models.BooleanField(blank=True, null=True)
    pagarcuentaautomatico = models.BooleanField(blank=True, null=True)
    idautoasignarrepartidor = models.CharField(max_length=5, blank=True, null=True)
    mantovtasminimoproductos = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    reservahorasbloquear = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    consultareportes = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    versiondb = models.CharField(max_length=5, blank=True, null=True)
    cambio = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    seriecompra = models.CharField(max_length=5, blank=True, null=True)
    foliocompra = models.CharField(max_length=10, blank=True, null=True)
    serieordencompra = models.CharField(max_length=5, blank=True, null=True)
    folioordencompra = models.CharField(max_length=10, blank=True, null=True)
    seriepedido = models.CharField(max_length=5, blank=True, null=True)
    foliopedido = models.CharField(max_length=10, blank=True, null=True)
    nopregtardescargacatalogos = models.BooleanField(blank=True, null=True)
    diasbuscarupd = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    reservaetiquetatiporeserva = models.CharField(max_length=30, blank=True, null=True)
    reservaetiquetacomisionistas = models.CharField(max_length=30, blank=True, null=True)
    reservacionprioridadcliente = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    reservatipoid = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipocalculocomision = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    femex = models.BooleanField(blank=True, null=True)
    femextipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    femexrutaarchivokey = models.CharField(max_length=250, blank=True, null=True)
    femexrutaarchivocer = models.CharField(max_length=250, blank=True, null=True)
    femexclavekey = models.CharField(max_length=50, blank=True, null=True)
    femexolrutaservicio = models.CharField(max_length=250, blank=True, null=True)
    femexolclaveempresa = models.CharField(max_length=50, blank=True, null=True)
    femexolcontrasenia = models.CharField(max_length=30, blank=True, null=True)
    femexolusuario = models.CharField(max_length=50, blank=True, null=True)
    femexolgenerar = models.BooleanField(blank=True, null=True)
    foliosrestantesavisofe = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    femextipoesquema = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    facturaventaimpuestoagrupada = models.BooleanField(blank=True, null=True)
    cortemovtostarjetas = models.BooleanField(blank=True, null=True)
    ocultarusuarioslogin = models.BooleanField(blank=True, null=True)
    kdscolorfuentenormal = models.IntegerField(blank=True, null=True)
    kdscolorfondonormal = models.IntegerField(blank=True, null=True)
    kdscolorfuentefoco = models.IntegerField(blank=True, null=True)
    kdscolorfondofoco = models.IntegerField(blank=True, null=True)
    kdscolorfuentealerta = models.IntegerField(blank=True, null=True)
    kdscolorfondoalerta = models.IntegerField(blank=True, null=True)
    kdscolorfuenteatrasado = models.IntegerField(blank=True, null=True)
    kdscolorfondoatrasado = models.IntegerField(blank=True, null=True)
    kdscolorfuentecan = models.IntegerField(blank=True, null=True)
    kdscolorfondocan = models.IntegerField(blank=True, null=True)
    kdsnumcuadros = models.IntegerField(blank=True, null=True)
    kdstiemporefresco = models.IntegerField(blank=True, null=True)
    kdstimerenabled = models.BooleanField(blank=True, null=True)
    kdskeyboardenabled = models.BooleanField(blank=True, null=True)
    kdsactivo = models.BooleanField(blank=True, null=True)
    costoautilizar = models.IntegerField(blank=True, null=True)
    ultimoturno = models.BigIntegerField(blank=True, null=True)
    impuestosmonedero = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    maxdiarioacumularpuntos = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    redondeopropinas = models.DecimalField(max_digits=1, decimal_places=0)
    redondeodescuentos = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    monederopaisdefault = models.CharField(max_length=10, blank=True, null=True)
    monederoestadodefault = models.CharField(max_length=10, blank=True, null=True)
    monederociudaddefault = models.CharField(max_length=20, blank=True, null=True)
    asignarpatinesrapido = models.BooleanField(blank=True, null=True)
    comandadirecciondomicilio = models.BooleanField(blank=True, null=True)
    serviciorapidocuentaspendientes = models.BooleanField(blank=True, null=True)
    serviciorapidodrivependiente = models.BooleanField(blank=True, null=True)
    serviciorapidomesa = models.BooleanField(blank=True, null=True)
    tipocalcularpropina = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    acumularproductoscondescuento = models.BooleanField(blank=True, null=True)
    visualizarproductosdirecto = models.BooleanField(blank=True, null=True)
    permitirdomicilioprogramado = models.BooleanField(blank=True, null=True)
    minutosactivarpedido = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ftpenviorespaldo = models.BooleanField(blank=True, null=True)
    ftprespaldo = models.CharField(max_length=254, blank=True, null=True)
    ftprespaldousuario = models.CharField(max_length=50, blank=True, null=True)
    ftprespaldocontraseña = models.CharField(max_length=50, blank=True, null=True)
    ftprespaldopuerto = models.CharField(max_length=10, blank=True, null=True)
    ftprespaldodirectorio = models.CharField(max_length=254, blank=True, null=True)
    comandacomentarioalado = models.BooleanField(blank=True, null=True)
    propinasinventa = models.BooleanField(blank=True, null=True)
    pagomonederocuentaimpresa = models.BooleanField(blank=True, null=True)
    nombreconsumiraqui = models.CharField(max_length=30, blank=True, null=True)
    nombreparallevar = models.CharField(max_length=30, blank=True, null=True)
    nombredrivethru = models.CharField(max_length=30, blank=True, null=True)
    nombredomicilio = models.CharField(max_length=30, blank=True, null=True)
    comedorobligarcliente = models.BooleanField(blank=True, null=True)
    comandacdoencabezado1 = models.CharField(max_length=5, blank=True, null=True)
    comandacdoencabezado2 = models.CharField(max_length=5, blank=True, null=True)
    comandacdoencabezado3 = models.CharField(max_length=5, blank=True, null=True)
    comandacdoencabezado4 = models.CharField(max_length=5, blank=True, null=True)
    comandacdocuerpo = models.CharField(max_length=5, blank=True, null=True)
    idproductocargoadicional = models.CharField(max_length=15, blank=True, null=True)
    tipocapturadirecciones = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    juntarmesasmismomesero = models.BooleanField(blank=True, null=True)
    passwordserviciocfdi = models.TextField(blank=True, null=True)  # This field type is a guess.
    urlservicioutileriascfdi = models.TextField(blank=True, null=True)  # This field type is a guess.
    rutacertificadocfdi = models.TextField(blank=True, null=True)  # This field type is a guess.
    verificarcfdirestantes = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    urlmanifiestocfdi = models.CharField(max_length=250, blank=True, null=True)
    manifiestocfdifirmado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    urlregistronatsoftcfdi = models.CharField(max_length=250, blank=True, null=True)
    urlserviciocfdi = models.TextField(blank=True, null=True)  # This field type is a guess.
    comisionpagada = models.BooleanField(blank=True, null=True)
    mostrarautorizacion = models.BooleanField(blank=True, null=True)
    reimprimircuentascan = models.BooleanField(blank=True, null=True)
    multiidiomahabilitado = models.BooleanField(blank=True, null=True)
    notificarreimpresion = models.BooleanField(blank=True, null=True)
    notificarcancelcuenta = models.BooleanField(blank=True, null=True)
    notificarcancelprod = models.BooleanField(blank=True, null=True)
    notificarreaperturacuenta = models.BooleanField(blank=True, null=True)
    notificarreaperturamismacta = models.BooleanField(blank=True, null=True)
    reimpresionemaximas = models.IntegerField(blank=True, null=True)
    cancelacioncuentamax = models.IntegerField(blank=True, null=True)
    cencelacionprodmax = models.IntegerField(blank=True, null=True)
    reaperturactamax = models.IntegerField(blank=True, null=True)
    reaperturamismactamax = models.IntegerField(blank=True, null=True)
    nombredesplegadoantifraudes = models.CharField(db_column='nombredesplegadoAntiFraudes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    asuntoantifraudes = models.CharField(db_column='asuntoAntiFraudes', max_length=120, blank=True, null=True)  # Field name made lowercase.
    notificardescuentocuenta = models.BooleanField(blank=True, null=True)
    notificardescuentoprod = models.BooleanField(blank=True, null=True)
    descuentomax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentoprodmax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nopermitircierreventascedis = models.BooleanField(blank=True, null=True)
    generarnuevopedidocedis = models.BooleanField(blank=True, null=True)
    conceptodevolucioncedis = models.CharField(max_length=5, blank=True, null=True)
    reservaciones_tiempo_inicial_bloqueo_mesa = models.SmallIntegerField(blank=True, null=True)
    asistencia_para_acceso_comandero = models.BooleanField(blank=True, null=True)
    modousoinv = models.SmallIntegerField(blank=True, null=True)
    enviamovtoscierre = models.BooleanField(blank=True, null=True)
    retenerimpuesto = models.BooleanField(blank=True, null=True)
    retencion1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retencion2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retencion3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ingreso_reservaciones = models.SmallIntegerField(blank=True, null=True)
    conceptoenviocedis = models.CharField(max_length=5, blank=True, null=True)
    nousarpendientes = models.BooleanField(blank=True, null=True)
    generarventacedis = models.BooleanField(blank=True, null=True)
    conceptorecepcioncedis = models.CharField(max_length=5, blank=True, null=True)
    usarprovpredeterminado = models.BooleanField(blank=True, null=True)
    saludo = models.CharField(max_length=60, blank=True, null=True)
    mensaje = models.CharField(max_length=100, blank=True, null=True)
    despedida = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros'


class Parametros2(models.Model):
    enviarordencompra = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cifradossl = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    foliocxc = models.IntegerField(blank=True, null=True)
    foliomovtoscaja = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    descargaactualizacionesinicio = models.BooleanField(blank=True, null=True)
    permitirenviocentralalexportar = models.BooleanField(blank=True, null=True)
    autorizacioncancelarproductos = models.BooleanField(blank=True, null=True)
    autorizacioncancelarcompras = models.BooleanField(blank=True, null=True)
    autorizacioncancelartraspasos = models.BooleanField(blank=True, null=True)
    autorizacioncancelarmovtosalmacen = models.BooleanField(blank=True, null=True)
    autorizacioncambiarfechaalmacen = models.BooleanField(blank=True, null=True)
    nousarcoloniasdomcilio = models.BooleanField(blank=True, null=True)
    reabrircuentapagada = models.BooleanField(blank=True, null=True)
    femexnocer = models.CharField(max_length=50, blank=True, null=True)
    hotelusuariodb = models.CharField(max_length=50, blank=True, null=True)
    cargarproductosfavoritos = models.BooleanField(blank=True, null=True)
    baseordenarproductos = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idunidaddeffault = models.CharField(max_length=50, blank=True, null=True)
    solicitarunidad = models.BooleanField(blank=True, null=True)
    formapagodefault = models.CharField(max_length=50, blank=True, null=True)
    usarformapagodefault = models.BooleanField(blank=True, null=True)
    usuariopac = models.CharField(max_length=200, blank=True, null=True)
    passwordpac = models.CharField(max_length=200, blank=True, null=True)
    permitircambiarcuentafac = models.BooleanField(blank=True, null=True)
    percontacto = models.CharField(max_length=50, blank=True, null=True)
    nombreimplementador = models.CharField(max_length=50, blank=True, null=True)
    correoimplementador = models.CharField(max_length=50, blank=True, null=True)
    telefonoimplementador = models.CharField(max_length=50, blank=True, null=True)
    imprimirformatocompramonex = models.BooleanField(blank=True, null=True)
    idformadepagocompramonex = models.CharField(max_length=15, blank=True, null=True)
    procesadocfdi = models.BooleanField(blank=True, null=True)
    mostrarmonitortimbres = models.BooleanField(blank=True, null=True)
    autorizacionmodoinventario = models.BooleanField(blank=True, null=True)
    cuentahub = models.CharField(max_length=200, blank=True, null=True)
    actualizacionpedidohub = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    confirmarpedido = models.BooleanField(blank=True, null=True)
    basedatoshub = models.CharField(max_length=200, blank=True, null=True)
    facturascentral = models.BooleanField(blank=True, null=True)
    cierrediarioaperturarturno = models.BooleanField(blank=True, null=True)
    tipocuentabierta = models.IntegerField(blank=True, null=True)
    colorletracuentarepartidor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    colorearcuentarepartidor = models.BooleanField(blank=True, null=True)
    colorcuentarepartidor = models.DecimalField(db_column='Colorcuentarepartidor', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tipodeimpresionordenescompra = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodeimpresionpedidos = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodeimpresiontraspasos = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodeimpresionmovtos = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodeimpresioninvfisico = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodeimpresiondesperdicio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodeimpresionexplosion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    monitormeserocolorfondopreparacion = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitormeserocolorletrapreparacion = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitormeserocolorfondoexcedido = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitormeserocolorletraexcedido = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitormeserotiempoactualizacion = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitormeserotiempotolerancia = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    monitormeserotipoordenamiento = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    monitormeseromostrarenpreparacion = models.BooleanField(blank=True, null=True)
    resumirconsumocuentacompuestos = models.BooleanField(blank=True, null=True)
    tipomanejoturno = models.IntegerField()
    usarsalvaguarda = models.BooleanField()
    salvaguardalimite = models.DecimalField(max_digits=19, decimal_places=4)
    salvaguardamontopredet = models.DecimalField(max_digits=19, decimal_places=4)
    salvaguardamomentovalidar = models.DecimalField(max_digits=1, decimal_places=0)
    salvaguardaobligar = models.BooleanField()
    alertaexistenciasgral = models.BooleanField()
    imprimircancelados = models.BooleanField()
    mostrarcorte = models.BooleanField(blank=True, null=True)
    criteriodescargarecetas = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    imprimirordenproduccion = models.BooleanField(blank=True, null=True)
    idprodrmplmtovtas = models.CharField(max_length=15, blank=True, null=True)
    rmpultprodmtovta = models.BooleanField(blank=True, null=True)
    permitirmovtosexistencianegativa = models.BooleanField(blank=True, null=True)
    enviarcorreocorte = models.BooleanField(blank=True, null=True)
    opcionenviocorte = models.SmallIntegerField(blank=True, null=True)
    cifradosslinv = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cifradosslantifraude = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cifradosslcortecorreo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nombredesplegadoinv = models.CharField(db_column='nombredesplegadoInv', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombredesplegadocorte = models.CharField(db_column='nombredesplegadoCorte', max_length=100, blank=True, null=True)  # Field name made lowercase.
    asuntoinv = models.CharField(db_column='asuntoInv', max_length=120, blank=True, null=True)  # Field name made lowercase.
    asuntocorte = models.CharField(db_column='asuntoCorte', max_length=120, blank=True, null=True)  # Field name made lowercase.
    servidormailnv = models.CharField(max_length=120, blank=True, null=True)
    servidormailantifraude = models.CharField(db_column='servidormailAntiFraude', max_length=120, blank=True, null=True)  # Field name made lowercase.
    servidormailcorte = models.CharField(db_column='servidormailCorte', max_length=120, blank=True, null=True)  # Field name made lowercase.
    puertoinv = models.CharField(db_column='puertoInv', max_length=20, blank=True, null=True)  # Field name made lowercase.
    puertoantifraude = models.CharField(db_column='puertoAntiFraude', max_length=20, blank=True, null=True)  # Field name made lowercase.
    puertocorte = models.CharField(db_column='puertoCorte', max_length=20, blank=True, null=True)  # Field name made lowercase.
    autentificacioninv = models.DecimalField(db_column='autentificacionInv', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    autentificacionantifraude = models.DecimalField(db_column='autentificacionAntiFraude', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    autentificacioncorte = models.DecimalField(db_column='autentificacionCorte', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    emailinv = models.CharField(db_column='emailInv', max_length=60, blank=True, null=True)  # Field name made lowercase.
    emailantifraude = models.CharField(db_column='emailAntiFraude', max_length=60, blank=True, null=True)  # Field name made lowercase.
    emailcorte = models.CharField(db_column='emailCorte', max_length=60, blank=True, null=True)  # Field name made lowercase.
    passwordemailinv = models.CharField(db_column='passwordemailInv', max_length=250, blank=True, null=True)  # Field name made lowercase.
    passwordemailantifraude = models.CharField(db_column='passwordemailAntiFraude', max_length=250, blank=True, null=True)  # Field name made lowercase.
    passwordemailcorte = models.CharField(db_column='passwordemailCorte', max_length=250, blank=True, null=True)  # Field name made lowercase.
    habilitacoiner = models.BooleanField(blank=True, null=True)
    idestablecimientocoiner = models.CharField(max_length=10, blank=True, null=True)
    porcentajecoiner = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dominiocoiner = models.CharField(max_length=150, blank=True, null=True)
    llaveencriptacioncoiner = models.CharField(max_length=150, blank=True, null=True)
    minutosactualizacion = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    tipodoctoenviocorte = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    propinasinventa = models.BooleanField(blank=True, null=True)
    contrasenameserodestino = models.BooleanField(blank=True, null=True)
    pac = models.IntegerField()
    urlregistrocfdi = models.CharField(max_length=200)
    cfdiv32migrado = models.BooleanField(blank=True, null=True)
    paconline = models.IntegerField()
    imprimirlogocomedor = models.IntegerField()
    imprimirlogodomicilio = models.IntegerField()
    imprimirlogorapido = models.IntegerField()
    imprimirlogonotadeconsumo = models.IntegerField()
    webapiregistrado = models.IntegerField()
    femexarchivokey = models.TextField()
    femexarchivocer = models.TextField()
    femexarchivokey_pem = models.TextField()
    femexarchivocer_pem = models.TextField()
    archivoscerkeyprocesados = models.IntegerField()
    serviciorapidoimprimirpagar = models.BooleanField()
    calculomontopropina = models.IntegerField(blank=True, null=True)
    porcentajepropinarapido = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    redondeopropinasrapido = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    propinaincluidarapido = models.BooleanField(blank=True, null=True)
    forzarcapturamesa = models.IntegerField(blank=True, null=True)
    ultimospedidos = models.BooleanField()
    codigomoneda = models.CharField(max_length=15)
    mostraracumuladomensualcorte = models.BooleanField()
    propinasmantto = models.BooleanField()
    tipopagodomicilio = models.BooleanField()
    uvtcolombia = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    reterenta = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    reteiva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    reteica = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ccreterenta = models.CharField(max_length=5, blank=True, null=True)
    ccreteiva = models.CharField(max_length=5, blank=True, null=True)
    ccreteica = models.CharField(max_length=5, blank=True, null=True)
    editarpesobascula = models.BooleanField()
    recargastelefonicasmx = models.BooleanField(blank=True, null=True)
    recteleftelcel = models.BooleanField(blank=True, null=True)
    recteleftelcelusuario = models.CharField(max_length=30, blank=True, null=True)
    recteleftelcelpass = models.CharField(max_length=30, blank=True, null=True)
    recteleftelcelurl = models.CharField(max_length=100, blank=True, null=True)
    idproductorectelef = models.CharField(max_length=15, blank=True, null=True)
    recteleftelcelurldeposito = models.CharField(max_length=250, blank=True, null=True)
    cedix_activar = models.BooleanField(blank=True, null=True)
    cedix_url = models.CharField(max_length=250, blank=True, null=True)
    cedix_clienteid = models.CharField(max_length=100, blank=True, null=True)
    cedix_storeid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cedix_posid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cedix_clerkcode = models.CharField(max_length=10, blank=True, null=True)
    cedix_timeout = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cedix_secondcheckingmax = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_carga_carriers = models.DateTimeField(blank=True, null=True)
    autorizaciontae = models.BooleanField(blank=True, null=True)
    urlges = models.CharField(max_length=250, blank=True, null=True)
    versiondb = models.DecimalField(max_digits=15, decimal_places=6)
    rifdetallado = models.BooleanField(db_column='RIFDetallado')  # Field name made lowercase.
    fenombreformatorif = models.CharField(max_length=50)
    propinaesconcepto = models.BooleanField()
    facturarapida = models.BooleanField()
    infomostrardespacho = models.DecimalField(max_digits=1, decimal_places=0)
    impuestoagrupadosustituirdetalle = models.BooleanField()
    impuestoagrupadopiedepagina = models.BooleanField()
    msjvigia = models.TextField()
    estatusvigia = models.CharField(max_length=50)
    infofintipodepoliza = models.CharField(max_length=2, blank=True, null=True)
    infofinusuario = models.CharField(max_length=2, blank=True, null=True)
    infofinpolizaregimensimp = models.CharField(max_length=1, blank=True, null=True)
    cccargoadicional = models.CharField(max_length=5, blank=True, null=True)
    traspasoautomatico = models.BooleanField(blank=True, null=True)
    ocpredeterminadoentregara = models.CharField(max_length=250, blank=True, null=True)
    imprimircantidadmodificador = models.BooleanField(blank=True, null=True)
    colorcuentasmonitor = models.BooleanField(blank=True, null=True)
    colorcuentascomedormonitor = models.IntegerField(blank=True, null=True)
    colorcuentascomedormonitorletras = models.IntegerField(blank=True, null=True)
    colorcuentasdomiciliomonitor = models.IntegerField(blank=True, null=True)
    colorcuentasdomiciliomonitorletras = models.IntegerField(blank=True, null=True)
    colorcuentasrapidomonitor = models.IntegerField(blank=True, null=True)
    colorcuentasrapidomonitorletras = models.IntegerField(blank=True, null=True)
    imprimirnotamonederoelectronico = models.BooleanField(blank=True, null=True)
    conceptootrosacrux = models.IntegerField(blank=True, null=True)
    conceptopropinasacrux = models.IntegerField(blank=True, null=True)
    monedaacrux = models.CharField(max_length=50, blank=True, null=True)
    encuestasipservidor = models.CharField(max_length=20, blank=True, null=True)
    encuestasdriverodbc = models.CharField(max_length=30, blank=True, null=True)
    encuestaspuerto = models.CharField(max_length=10, blank=True, null=True)
    encuestasuid = models.CharField(max_length=10, blank=True, null=True)
    encuestaspassword = models.CharField(max_length=30, blank=True, null=True)
    encuestasdb = models.CharField(max_length=30, blank=True, null=True)
    puntosmonederoporrango = models.BooleanField(blank=True, null=True)
    politicaacumulacionmonedero = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipoacumulacion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    montoacumulacionmultiplo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puntosacumulacionmultiplo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    separadorcodigobarrascomedor = models.CharField(max_length=5, blank=True, null=True)
    usarseparadorencomedor = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    separadorcodigobarrasdomicilio = models.CharField(max_length=5, blank=True, null=True)
    usarseparadorendomicilio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    separadorcodigobarrasrapido = models.CharField(max_length=5, blank=True, null=True)
    usarseparadorenrapido = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    separadorcodigobarrasnotaconsumo = models.CharField(max_length=5, blank=True, null=True)
    usarseparadorennotaconsumo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipocodigocomedor = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipocodigodomicilio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipocodigorapido = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipocodigonotadeconsumo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    anchocomedor = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    altocomedor = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    anchodomicilio = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    altodomicilio = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    anchorapido = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    altorapido = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    anchonotaconsumo = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    altonotaconsumo = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    impcodigobarratktcom = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    impcodigobarratktdom = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    impcodigobarratktrap = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    impcodigobarratktnc = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    bloquearfechaaplicacioncompras = models.BooleanField(blank=True, null=True)
    polizaconvertirmonedaextranjera = models.BooleanField(blank=True, null=True)
    sapgenerardoscabecerosmonex = models.BooleanField(blank=True, null=True)
    descripcion_gravada = models.CharField(max_length=50)
    descripcion_exenta = models.CharField(max_length=50)
    imprimircomanda = models.BooleanField()
    autocuttercomanda = models.BooleanField()
    impresoracomanda = models.CharField(max_length=100)
    agrupacomandas = models.BooleanField()
    resumiragruparmodificadores = models.BooleanField()
    descuentoenfactura = models.BooleanField()
    opcionccpropinausar = models.IntegerField(blank=True, null=True)
    ccpropina = models.CharField(max_length=5, blank=True, null=True)
    imprimirboletaperu = models.BooleanField(blank=True, null=True)
    doctoimprimirperu = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    copiasboletaperu = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    marcarcuentafacturadaperu = models.BooleanField(blank=True, null=True)
    cambio = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    ticketsalfabetico = models.BooleanField(blank=True, null=True)
    tipoieps = models.IntegerField(db_column='tipoIEPS')  # Field name made lowercase.
    modificaent = models.BooleanField()
    continuarcapturaproductocompuesto = models.BooleanField()
    primeraconexionent = models.BooleanField()
    contpaqi_instancia = models.CharField(max_length=100)
    contpaqi_usuariobd = models.CharField(max_length=100)
    contpaqi_passbd = models.TextField()
    contpaqi_empresa = models.CharField(max_length=200)
    contpaqi_usuariodefault = models.BooleanField()
    contpaqi_usuario = models.CharField(max_length=100)
    contpaqi_pass = models.TextField()
    contpaqi_conceptoingresos = models.TextField()
    contpaqi_conceptoegresos = models.TextField()
    cobrotarjetarapido = models.BooleanField(db_column='cobroTarjetaRapido')  # Field name made lowercase.
    abrircuentamapamesas = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'parametros2'


class Parametros3(models.Model):
    contpaqi_tipopolizaing = models.IntegerField()
    contpaqi_tipopolizaeg = models.IntegerField()
    mostrarindicadores = models.BooleanField()
    autogenerarpolizacompra = models.IntegerField()
    descuentosformasdepago = models.BooleanField(db_column='descuentosFormasDePago')  # Field name made lowercase.
    microsipinterfaz = models.BooleanField()
    microsip_sucursal = models.CharField(max_length=250)
    microsip_ftp = models.CharField(max_length=250)
    microsip_directorioftp = models.CharField(max_length=250)
    microsip_puertoftp = models.CharField(max_length=10)
    microsip_usuarioftp = models.CharField(max_length=100)
    microsip_passftp = models.TextField()
    microsip_usuario = models.CharField(max_length=50)
    pagarcuentacapitan = models.BooleanField()
    imprimircuentacapitan = models.BooleanField()
    leyendadesglosefolios = models.CharField(db_column='leyendaDesgloseFolios', max_length=250)  # Field name made lowercase.
    ordenleyendadesglosefolios = models.SmallIntegerField(db_column='ordenLeyendaDesgloseFolios')  # Field name made lowercase.
    rifdesglosaimpuestos = models.BooleanField(db_column='RIFDesglosaImpuestos')  # Field name made lowercase.
    totalescompras = models.BooleanField()
    nuevocliente = models.BooleanField()
    editarcliente = models.BooleanField()
    descuentocompras = models.BooleanField()
    autorizausuariofacturarapido = models.BooleanField()
    explosionproductos = models.BooleanField()
    nuevocierraturno = models.BooleanField()
    desarrolloscozumel = models.BooleanField()
    bloquearpagomonex = models.BooleanField()
    bloquearpagoidmonex = models.CharField(max_length=15)
    bloquearpagocantidad = models.DecimalField(max_digits=16, decimal_places=2)
    maxfailedlogins = models.SmallIntegerField()
    blockuserfailedlogins = models.BooleanField()
    minimuserpasslen = models.SmallIntegerField()
    usrpassnotconschar = models.BooleanField()
    usrpassexpires = models.BooleanField()
    usrpassexpiresdays = models.SmallIntegerField()
    multiidiomas_menu_digital = models.BooleanField()
    multiidiomas_menu_activo = models.BooleanField()
    allowdisctoverdisct = models.BooleanField()
    activeallowdisctoverdisct = models.BooleanField()
    ocultareditarcompras = models.BooleanField()
    ocultareditartraspasos = models.BooleanField()
    ocultareditarmovtosalmacen = models.BooleanField()
    dev_bloquearcaptura = models.BooleanField()
    bloquearcapturacuentacondescuento = models.BooleanField()
    dev_monitor_tabletas = models.BooleanField()
    dev_monitor_tabletas_tiempo = models.IntegerField()
    usar_estacion_tablets = models.BooleanField()
    usar_mesero_tablets = models.BooleanField()
    focusinbarcode = models.BooleanField()
    dev_intelisis = models.BooleanField()
    activarmoificadoresclave = models.BooleanField()
    estacionsrx = models.CharField(max_length=50, blank=True, null=True)
    companyid = models.CharField(max_length=50, blank=True, null=True)
    accountid = models.CharField(max_length=50, blank=True, null=True)
    authorizedapp = models.CharField(max_length=50, blank=True, null=True)
    ventasonline = models.BooleanField(db_column='VentasOnline')  # Field name made lowercase.
    dev_repinventarios = models.BooleanField()
    idformadepagosrx = models.CharField(max_length=50, blank=True, null=True)
    finalizarordenmonitor = models.BooleanField()
    idpagoefectivosrx = models.CharField(max_length=50, blank=True, null=True)
    reportecajasrx = models.BooleanField()
    validatodosalmacenes = models.BooleanField()
    requestinvoicesequence = models.SmallIntegerField(db_column='RequestInvoiceSequence')  # Field name made lowercase.
    forceinvoicerequest = models.BooleanField(db_column='ForceInvoiceRequest')  # Field name made lowercase.
    sonidodescargapedidoapp = models.BooleanField()
    idtipodescuentoapp = models.CharField(max_length=5, blank=True, null=True)
    iniciarsrmwindows = models.BooleanField()
    enlaceotraestacion = models.BooleanField()
    idconcepto_sat = models.CharField(db_column='idconcepto_SAT', max_length=50)  # Field name made lowercase.
    versionfacturacion = models.DecimalField(max_digits=16, decimal_places=6)
    repetir_alerta = models.BooleanField()
    multiidiomas_monitor_prod = models.BooleanField()
    multiidiomas_comandas_prod = models.BooleanField()
    dev_cga = models.BooleanField()
    bloquearcambiomonex = models.BooleanField()
    bloquearcambioidmonex = models.CharField(max_length=15)
    bloquearcambiocantidad = models.DecimalField(max_digits=5, decimal_places=2)
    mostrartotalmonex = models.BooleanField()
    dev_surveycode = models.BooleanField()
    storenumber = models.CharField(max_length=10)
    dev_ieps = models.BooleanField(db_column='dev_IEPS')  # Field name made lowercase.
    desglose_ieps = models.BooleanField(db_column='desglose_IEPS')  # Field name made lowercase.
    dev_vectorplus = models.BooleanField()
    activarvp = models.BooleanField(db_column='activarVP')  # Field name made lowercase.
    ipadresvp = models.CharField(db_column='ipadresVP', max_length=50)  # Field name made lowercase.
    portvp = models.CharField(db_column='portVP', max_length=10)  # Field name made lowercase.
    psl = models.BooleanField()
    dev_dominicana = models.BooleanField()
    activartipocredito = models.BooleanField()
    mostrarcambioadevolver = models.BooleanField()
    solicitadeclaraciondecajero = models.BooleanField()
    dev_guatemala = models.BooleanField(db_column='Dev_Guatemala')  # Field name made lowercase.
    dev_activargt = models.BooleanField(db_column='Dev_ActivarGT')  # Field name made lowercase.
    finalizarmonitor = models.BooleanField()
    imprimirfacturadll = models.BooleanField()
    facturaminiprinter = models.BooleanField()
    dev_gpo_cafrema = models.BooleanField()
    nombrereal_inicio = models.BooleanField()
    inicio_maximizado = models.BooleanField()
    rapido_maximizado = models.BooleanField()
    desglosartiposervicio = models.BooleanField()
    boton_checarasistencia = models.BooleanField()
    des_insa_mesajuegos = models.BooleanField()
    dev_mrtecno = models.BooleanField()
    monitorordenamientomesas = models.BooleanField()
    enviarventascentral = models.BooleanField()
    mostrarmenucent = models.BooleanField()
    fechalimitebolivia = models.DateTimeField(blank=True, null=True)
    servicio_cambiodeusuario = models.BooleanField()
    des_ocultarmitades = models.BooleanField()
    permitirventarapida = models.BooleanField()
    des_modificadoresincluidos = models.BooleanField()
    imp_observaciones_factura = models.BooleanField()
    updateonline = models.BooleanField()
    requestcustomerfastservice = models.BooleanField(db_column='requestCustomerFastService')  # Field name made lowercase.
    validacheques = models.BooleanField()
    accesosrapido = models.BooleanField()
    importeminimomantto = models.BooleanField()
    dev_listadefault = models.BooleanField()
    dev_tokencash = models.BooleanField(db_column='Dev_Tokencash')  # Field name made lowercase.
    tkc_usar = models.BooleanField(db_column='TKC_Usar')  # Field name made lowercase.
    tkc_nocuenta = models.CharField(db_column='TKC_Nocuenta', max_length=100)  # Field name made lowercase.
    tkc_apikey = models.TextField(db_column='TKC_Apikey')  # Field name made lowercase.
    tkc_authorization = models.TextField(db_column='TKC_Authorization')  # Field name made lowercase.
    tkc_fidelizacion = models.BooleanField(db_column='TKC_Fidelizacion')  # Field name made lowercase.
    tkc_tipo = models.IntegerField(db_column='TKC_Tipo')  # Field name made lowercase.
    tkc_porcentaje = models.DecimalField(db_column='TKC_Porcentaje', max_digits=6, decimal_places=2)  # Field name made lowercase.
    tkc_impresion = models.BooleanField(db_column='TKC_Impresion')  # Field name made lowercase.
    tkc_tipoimpresion = models.IntegerField(db_column='TKC_TipoImpresion')  # Field name made lowercase.
    complementopago = models.BooleanField()
    foliogasto = models.CharField(max_length=10, blank=True, null=True)
    seriegasto = models.CharField(max_length=5, blank=True, null=True)
    des_reportemodificadores = models.BooleanField()
    dev_impuestoimporte3 = models.BooleanField()
    impuestoimporte3 = models.DecimalField(max_digits=19, decimal_places=4)
    leyendaimpuestoimporte3 = models.CharField(max_length=100)
    versionmit = models.CharField(db_column='versionMIT', max_length=6)  # Field name made lowercase.
    mit_publickey = models.CharField(db_column='MIT_PublicKey', max_length=200)  # Field name made lowercase.
    dtomodificadores = models.BooleanField()
    numimpresionesrapido = models.BooleanField()
    dev_preciocostarica = models.BooleanField()
    showheartlandpax = models.BooleanField(db_column='showHeartlandPax')  # Field name made lowercase.
    fe_cr_show = models.BooleanField(db_column='FE_CR_show')  # Field name made lowercase.
    fe_cr = models.BooleanField(db_column='FE_CR')  # Field name made lowercase.
    fe_cr_fecha_activa = models.DateTimeField(db_column='FE_CR_fecha_activa', blank=True, null=True)  # Field name made lowercase.
    fe_cr_estacion = models.CharField(db_column='FE_CR_estacion', max_length=40)  # Field name made lowercase.
    logheartlandpax = models.BooleanField(db_column='logHeartlandPax')  # Field name made lowercase.
    cancelaciondetallereporte = models.BooleanField()
    showsmartpayments = models.BooleanField(db_column='showSmartPayments')  # Field name made lowercase.
    efectosfiscalesalpago = models.BooleanField()
    usarminusculasticket = models.BooleanField()
    esp_coment_monprodpro = models.BooleanField()
    showcoloresmonitor = models.BooleanField(db_column='showColoresMonitor')  # Field name made lowercase.
    cambiodemesamapa = models.BooleanField()
    dev_calcpropinacostarica = models.BooleanField()
    fe_cr_intervalo = models.IntegerField(db_column='FE_CR_intervalo')  # Field name made lowercase.
    t_monitor = models.BooleanField()
    validamitad = models.BooleanField()
    fe_cr_timeout = models.IntegerField(db_column='FE_CR_timeout')  # Field name made lowercase.
    formaspagocortez = models.BooleanField()
    totalimpuestosdesglose = models.BooleanField()
    subtotalimpuestosdesglose = models.BooleanField()
    importeexento = models.BooleanField()
    descuentos_p_honduras = models.BooleanField()
    importeexonerado = models.BooleanField()
    imprimirticketcancelacion = models.BooleanField()
    imprimirticketdescuento = models.BooleanField()
    ocultadenc = models.BooleanField()
    bitacoracrapido = models.BooleanField()
    fechaactualdiv = models.BooleanField()
    permventaneg = models.BooleanField()
    desc_importe = models.SmallIntegerField()
    desc_importepant = models.SmallIntegerField()
    forzardescuento = models.BooleanField()
    descuentototalhon = models.BooleanField()
    dev_estrateca = models.BooleanField()
    estrateca_usar = models.BooleanField()
    estrateca_urlapi = models.TextField(db_column='estrateca_UrlApi')  # Field name made lowercase.
    formatocomanda = models.BooleanField()
    dev_sacoa = models.BooleanField()
    show_sacoa = models.BooleanField()
    user_sacoa = models.CharField(max_length=50)
    pass_sacoa = models.CharField(max_length=200)
    idproducto_sacoa = models.CharField(max_length=15)
    urlservice_sacoa = models.CharField(max_length=150)
    estrateca_storeid = models.CharField(db_column='estrateca_storeId', max_length=10)  # Field name made lowercase.
    estrateca_programid = models.CharField(db_column='estrateca_programId', max_length=10)  # Field name made lowercase.
    estrateca_brandid = models.CharField(db_column='estrateca_brandId', max_length=10)  # Field name made lowercase.
    fechau = models.CharField(max_length=200)
    dev_cafremaqr = models.BooleanField()
    cafrema_imprimirqr = models.BooleanField()
    cafrema_url = models.CharField(max_length=200)
    service_palace = models.BooleanField()
    url_palace = models.CharField(max_length=200)
    fact_desgloseitems = models.BooleanField()
    show_mit_version = models.BooleanField(db_column='show_MIT_version')  # Field name made lowercase.
    donativos = models.BooleanField()
    activa_donativos = models.BooleanField()
    showfecol = models.BooleanField(db_column='showFECol')  # Field name made lowercase.
    fe_col = models.BooleanField(db_column='FE_COL')  # Field name made lowercase.
    activ_report_total_desc = models.BooleanField(db_column='activ_report_total_Desc')  # Field name made lowercase.
    dev_paraguay = models.BooleanField()
    activar_facturaporitemparaguay = models.BooleanField(db_column='activar_facturaporitemParaguay')  # Field name made lowercase.
    show_factg = models.BooleanField(db_column='show_FactG')  # Field name made lowercase.
    dev_factg_local = models.BooleanField(db_column='dev_FactG_local')  # Field name made lowercase.
    fechacierrefg = models.DateTimeField(db_column='fechacierreFG', blank=True, null=True)  # Field name made lowercase.
    idcliente_factg = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente_FactG', blank=True, null=True)  # Field name made lowercase.
    multiformaspago_show = models.BooleanField()
    multiformaspago = models.BooleanField()
    idiomasletras = models.BooleanField()
    monitor_elab_show = models.BooleanField()
    timermonitorprep = models.DecimalField(max_digits=3, decimal_places=0)
    cancelaproduccion_show = models.BooleanField()
    generaspvelaborado = models.BooleanField()
    dividecuenta_numeros = models.BooleanField()
    abrecuenta_numeros = models.BooleanField()
    turnoxmesero = models.BooleanField()
    colombia_dian = models.BooleanField()
    user_show_login = models.BooleanField()
    reportedeutilidadesm_show = models.BooleanField()
    mpp_vistaporestacion = models.BooleanField()
    usar_nsindicadores = models.BooleanField(db_column='usar_NSIndicadores')  # Field name made lowercase.
    dev_sincfoliosvtaaf = models.BooleanField(db_column='dev_sincFoliosVtaAF')  # Field name made lowercase.
    respclientediv = models.BooleanField()
    habilitar_nsindicadores = models.BooleanField(db_column='habilitar_NSIndicadores')  # Field name made lowercase.
    enablefirmaentouch = models.BooleanField()
    dev_brazalete = models.BooleanField()
    dev_brazalete_modo = models.SmallIntegerField()
    dev_brazalete_solicitahuesped = models.BooleanField()
    master_account = models.CharField(max_length=150)
    monitor_domi_show = models.BooleanField()
    ocultar_empaquetado = models.BooleanField()
    puertopalace = models.CharField(max_length=15)
    service_priceshoes = models.BooleanField()
    idempresa_gen = models.CharField(max_length=60, blank=True, null=True)
    reporte_fiscal = models.BooleanField()
    emailsrpago = models.CharField(max_length=70)
    srpago = models.BooleanField()
    idformadepagosrpago = models.CharField(max_length=5)
    solicitapassadmincapitanmesero = models.BooleanField(db_column='solicitaPassAdminCapitanMesero', blank=True, null=True)  # Field name made lowercase.
    solicitadenominacionpagarcta = models.BooleanField()
    enc_executed = models.BooleanField()
    iniciarmonitorcortewindows = models.BooleanField()
    administraciononline = models.BooleanField()
    fe_py = models.BooleanField(db_column='FE_PY')  # Field name made lowercase.
    unoe = models.CharField(db_column='unoE', max_length=100)  # Field name made lowercase.
    dose = models.CharField(db_column='dosE', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametros3'


class Patines(models.Model):
    idpatin = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    colorpatin = models.CharField(max_length=30, blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patines'


class Pedidos(models.Model):
    idpedido = models.BigAutoField(primary_key=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    folio = models.CharField(max_length=15, blank=True, null=True)
    fechacaptura = models.DateTimeField(blank=True, null=True)
    fecharecepcion = models.DateTimeField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    foliopedido = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    entregara = models.CharField(max_length=100, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fechahoraautorizado = models.DateTimeField(blank=True, null=True)
    usuarioautorizo = models.CharField(max_length=15, blank=True, null=True)
    fechahoraenviado = models.DateTimeField(blank=True, null=True)
    idproveedor = models.CharField(max_length=15, blank=True, null=True)
    ventagenerada = models.BooleanField(blank=True, null=True)
    idtipopedido = models.CharField(max_length=5, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    editadosucursal = models.BooleanField(blank=True, null=True)
    idpedidocentral = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class Pedidosdetalle(models.Model):
    idpedido = models.ForeignKey(Pedidos, models.DO_NOTHING, db_column='idpedido', blank=True, null=True)
    idinsumo = models.ForeignKey(Insumospresentaciones, models.DO_NOTHING, db_column='idinsumo', blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    idalmacen = models.CharField(max_length=5, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    importesinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto1importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    importeconimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidadsurtida = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cantidadrecibida = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    surtirpendiente = models.BooleanField(blank=True, null=True)
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    fechahoraenviado = models.DateTimeField(blank=True, null=True)
    cantidaddevuelta = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    idalmacendescarga = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidosdetalle'


class Perfilesdescuentos(models.Model):
    idusuariosperfiles = models.CharField(max_length=15, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfilesdescuentos'


class Perfilesformasdepago(models.Model):
    idusuariosperfiles = models.OneToOneField('Usuariosperfiles', models.DO_NOTHING, db_column='idusuariosperfiles', primary_key=True)  # The composite primary key (idusuariosperfiles, idformadepago) found, that is not supported. The first column is selected.
    idformadepago = models.ForeignKey(Formasdepago, models.DO_NOTHING, db_column='idformadepago')

    class Meta:
        managed = False
        db_table = 'perfilesformasdepago'
        unique_together = (('idusuariosperfiles', 'idformadepago'),)


class Plazasempresa(models.Model):
    idplaza = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plazasempresa'


class PosSettings(models.Model):
    idestacion = models.CharField(primary_key=True, max_length=40)
    serie_precuenta_col = models.CharField(db_column='serie_precuenta_COL', max_length=30)  # Field name made lowercase.
    colorletrabotones = models.DecimalField(max_digits=10, decimal_places=0)
    colorletradisabled_botones = models.DecimalField(max_digits=10, decimal_places=0)
    mac_address = models.CharField(max_length=20)
    cashdro_activar = models.BooleanField()
    cashdro_ip = models.CharField(max_length=50, blank=True, null=True)
    cashdro_usar_https = models.BooleanField()
    cashdro_usuario = models.CharField(max_length=50, blank=True, null=True)
    cashdro_pass = models.CharField(max_length=50, blank=True, null=True)
    cashdro_currency = models.CharField(max_length=5)
    sync_activo = models.BooleanField(blank=True, null=True)
    cashdro_transfer_shift = models.BooleanField()
    cashdro_has_coin_cassette = models.BooleanField()
    reducir_fuente_encabezado_captura_productos = models.BooleanField()
    criterio_busqueda_catalogos = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'pos_settings'


class Productos(models.Model):
    idproducto = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idgrupo = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='idgrupo', blank=True, null=True)
    nombrecorto = models.CharField(max_length=20, blank=True, null=True)
    plu = models.CharField(max_length=30, blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True, db_comment='Es un campo que se encontraba ')
    nofacturable = models.BooleanField(blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    usarcomedor = models.BooleanField(blank=True, null=True)
    usardomicilio = models.BooleanField(blank=True, null=True)
    usarrapido = models.BooleanField(blank=True, null=True)
    usarcedis = models.BooleanField(blank=True, null=True)
    idinsumospresentaciones = models.CharField(max_length=15, blank=True, null=True)
    imagenmenuelectronico = models.BinaryField(blank=True, null=True)
    descripcionmenuelectronico = models.CharField(max_length=255, blank=True, null=True)
    usarmenuelectronico = models.BooleanField(blank=True, null=True)
    extmenu = models.CharField(max_length=5, blank=True, null=True)
    imagen_menu = models.TextField(blank=True, null=True)
    descripcion_detalle = models.CharField(max_length=300)
    calorias = models.DecimalField(max_digits=18, decimal_places=0)
    visible_menu = models.BooleanField()
    capturar_pendientes = models.BooleanField()
    id_etiqueta = models.CharField(max_length=50)
    id_etiqueta_descripcion = models.CharField(max_length=50)
    idprodserv_sat = models.CharField(db_column='idprodserv_SAT', max_length=50)  # Field name made lowercase.
    usarvectorplus = models.BooleanField(db_column='usarVectorPlus')  # Field name made lowercase.
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    imagenme_modified = models.BooleanField()
    imagenbackoffice = models.BinaryField(blank=True, null=True)
    monitoreo = models.BooleanField()
    prioridadimpresion = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    idbo = models.IntegerField(db_column='IdBO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'

    def __str__(self):
        return f'{self.idproducto} - {self.descripcion}'


class Productostokencash(models.Model):
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    lunesaplica = models.BooleanField(blank=True, null=True)
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    lunesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    martesaplica = models.BooleanField(blank=True, null=True)
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    martesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    miercolesaplica = models.BooleanField(blank=True, null=True)
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    miercolesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    juevesaplica = models.BooleanField(blank=True, null=True)
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    juevesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    viernesaplica = models.BooleanField(blank=True, null=True)
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    viernesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sabadoaplica = models.BooleanField(blank=True, null=True)
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    sabadodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    domingoaplica = models.BooleanField(blank=True, null=True)
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    domingodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    multiplo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puntosmultiplo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productosTokencash'


class ProductosPuntos(models.Model):
    id = models.BigAutoField(primary_key=True)
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    puntos = models.DecimalField(max_digits=12, decimal_places=0)
    app_id = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField()
    modo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'productos_puntos'


class Productosdelivery(models.Model):
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descripcion = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    idapp = models.IntegerField()
    visiblemenu = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productosdelivery'


class Productosdetalle(models.Model):
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    preciosinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bloqueado = models.BooleanField(blank=True, null=True)
    precioabierto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    canjeablepuntos = models.BooleanField(blank=True, null=True)
    preciopuntos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puntoscanje = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puntosextras = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    preciolunes = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    lunesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    preciomartes = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    martesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    preciomiercoles = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    miercolesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    preciojueves = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    juevesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    precioviernes = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    viernesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    preciosabado = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sabadodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    preciodomingo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    domingodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    aplicalunes = models.BooleanField(blank=True, null=True)
    aplicamartes = models.BooleanField(blank=True, null=True)
    aplicamiercoles = models.BooleanField(blank=True, null=True)
    aplicajueves = models.BooleanField(blank=True, null=True)
    aplicaviernes = models.BooleanField(blank=True, null=True)
    aplicasabado = models.BooleanField(blank=True, null=True)
    aplicadomingo = models.BooleanField(blank=True, null=True)
    excentoimpuestos = models.BooleanField(blank=True, null=True)
    secuenciacompuesto = models.BooleanField(blank=True, null=True)
    finalizarsecuenciacompuesto = models.BooleanField(blank=True, null=True)
    heredarmonitormodificadores = models.BooleanField(blank=True, null=True)
    comisionvendedor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    eliminarfiscal = models.BooleanField(blank=True, null=True)
    enviarproduccionsimodificador = models.BooleanField(blank=True, null=True)
    cargoadicional = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    afectacomensales = models.BooleanField(blank=True, null=True)
    comensalesafectados = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    descargar = models.BooleanField(blank=True, null=True)
    usarmultiplicadorprodcomp = models.BooleanField(blank=True, null=True)
    rentabilidadcedis = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    idarea = models.CharField(max_length=4, blank=True, null=True)
    permitirprodcompenmodif = models.BooleanField(blank=True, null=True)
    politicapuntos = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    favorito = models.BooleanField(blank=True, null=True)
    idunidad = models.ForeignKey('Udsmedida', models.DO_NOTHING, db_column='idunidad', blank=True, null=True)
    ocultarmitades = models.BooleanField()
    dev_impuestoimporte3 = models.BooleanField()
    impuestoimporte3 = models.DecimalField(max_digits=19, decimal_places=4)
    usa_imagen_monitor = models.BooleanField()
    rutaimagen = models.TextField(blank=True, null=True)
    comisionprecio = models.DecimalField(max_digits=19, decimal_places=4)
    usa_bascula = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productosdetalle'
        verbose_name_plural = 'Productos Detalle'
        verbose_name = 'Producto Detalle'

    def __str__(self):
        return f'{self.idproducto} - {self.precio}'


class Productosenproduccion(models.Model):
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idmonitor = models.ForeignKey(Monitoresproduccion, models.DO_NOTHING, db_column='idmonitor', blank=True, null=True)
    folio = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    movimiento = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    tiempo = models.CharField(max_length=20, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    modificador = models.BooleanField(blank=True, null=True)
    estadomonitor = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idproductocompuesto = models.CharField(max_length=15, blank=True, null=True)
    productocompuestoprincipal = models.BooleanField(blank=True, null=True)
    minutospreparacion = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    minutosalerta = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    horaproduccion = models.DateTimeField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    prioridad = models.CharField(max_length=1, blank=True, null=True)
    enviadomonitor = models.BooleanField(blank=True, null=True)
    separador = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productosenproduccion'


class Productosindicadorimpuesto(models.Model):
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    indicadorimpuesto = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productosindicadorimpuesto'


class Productosmonedero(models.Model):
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idarearestaurant = models.ForeignKey(Areasrestaurant, models.DO_NOTHING, db_column='idarearestaurant', blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    lunesaplica = models.BooleanField(blank=True, null=True)
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    lunesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    martesaplica = models.BooleanField(blank=True, null=True)
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    martesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    miercolesaplica = models.BooleanField(blank=True, null=True)
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    miercolesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    juevesaplica = models.BooleanField(blank=True, null=True)
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    juevesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    viernesaplica = models.BooleanField(blank=True, null=True)
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    viernesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sabadoaplica = models.BooleanField(blank=True, null=True)
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    sabadodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    domingoaplica = models.BooleanField(blank=True, null=True)
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    domingodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    multiplo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puntosmultiplo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productosmonedero'


class Productosmonitores(models.Model):
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idmonitor = models.ForeignKey(Monitoresproduccion, models.DO_NOTHING, db_column='idmonitor', blank=True, null=True)
    minutosalerta = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    minutospreparacion = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productosmonitores'


class Promociones(models.Model):
    idpromocion = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipopromocion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    aplicalunes = models.BooleanField(blank=True, null=True)
    lunesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    aplicamartes = models.BooleanField(blank=True, null=True)
    martesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    aplicamiercoles = models.BooleanField(blank=True, null=True)
    miercolesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    aplicajueves = models.BooleanField(blank=True, null=True)
    juevesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    aplicaviernes = models.BooleanField(blank=True, null=True)
    viernesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    aplicasabado = models.BooleanField(blank=True, null=True)
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    aplicadomingo = models.BooleanField(blank=True, null=True)
    domingodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fotografia = models.BinaryField(blank=True, null=True)
    visualizar = models.BooleanField(blank=True, null=True)
    relacionuno = models.DecimalField(db_column='Relacionuno', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    relaciondos = models.DecimalField(db_column='Relaciondos', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    forzarporproducto = models.BooleanField(blank=True, null=True)
    aplicamodificadores = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'promociones'


class Promocionesdescargar(models.Model):
    idpromocion = models.CharField(max_length=5, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    descargar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promocionesdescargar'


class Promocionesmenuelectronico(models.Model):
    idpromocion = models.CharField(max_length=5)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idproducto = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    estatus = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ubicacion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fotografia = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promocionesmenuelectronico'


class Promoproductos(models.Model):
    idpromocion = models.ForeignKey(Promociones, models.DO_NOTHING, db_column='idpromocion', blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    preciopromocion = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promoproductos'


class Proveedores(models.Model):
    idproveedor = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    razonsocial = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    codigopostal = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    rfc = models.CharField(max_length=15, blank=True, null=True)
    credito = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    usarcostosasignados = models.BooleanField(blank=True, null=True)
    usarenpoliza = models.BooleanField(blank=True, null=True)
    idtipoproveedor = models.ForeignKey('Tipoproveedores', models.DO_NOTHING, db_column='idtipoproveedor', blank=True, null=True)
    idcuentacontable = models.CharField(max_length=5, blank=True, null=True)
    nombrebanco = models.CharField(max_length=100, blank=True, null=True)
    nocuenta = models.CharField(max_length=100, blank=True, null=True)
    cuentaclave = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'


class Proveedorespredet(models.Model):
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa')
    idproveedor = models.ForeignKey(Proveedores, models.DO_NOTHING, db_column='idproveedor')

    class Meta:
        managed = False
        db_table = 'proveedorespredet'


class Puntos(models.Model):
    tipodeservicio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    lunesaplica = models.BooleanField(blank=True, null=True)
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    lunesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    martesaplica = models.BooleanField(blank=True, null=True)
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    martesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    miercolesaplica = models.BooleanField(blank=True, null=True)
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    miercolesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    juevesaplica = models.BooleanField(blank=True, null=True)
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    juevesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    viernesaplica = models.BooleanField(blank=True, null=True)
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    viernesdiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sabadoaplica = models.BooleanField(blank=True, null=True)
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    sabadodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    domingoaplica = models.BooleanField(blank=True, null=True)
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    domingodiasalida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puntos'


class Puntosgruposdeproductos(models.Model):
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    idgrupoproducto = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='idgrupoproducto', blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipodeservicio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    multiplo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puntosmultiplo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puntosgruposdeproductos'


class Rangohoras(models.Model):
    idrangohoras = models.CharField(db_column='Idrangohoras', max_length=10, blank=True, null=True)  # Field name made lowercase.
    desc_rangohora = models.CharField(db_column='Desc_rangohora', max_length=50, blank=True, null=True)  # Field name made lowercase.
    horainicio = models.CharField(db_column='Horainicio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    horafin = models.CharField(db_column='Horafin', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rangohoras'


class Recetasalmacenes(models.Model):
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idarearestaurant = models.ForeignKey(Areasrestaurant, models.DO_NOTHING, db_column='idarearestaurant', blank=True, null=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recetasalmacenes'


class Regionempresa(models.Model):
    idregionempresa = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regionempresa'


class Regiones(models.Model):
    idregion = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regiones'


class RegistroDispositivos(models.Model):
    folio = models.AutoField(primary_key=True)
    id_dispositivo = models.CharField(max_length=250)
    numerocontrol = models.CharField(max_length=60)
    contraseniacontrol = models.CharField(max_length=30)
    fecha = models.DateTimeField()
    nombre_dispositivo = models.CharField(max_length=250)
    contraclave = models.CharField(max_length=100, blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True)
    sistema_registro = models.IntegerField()
    vigencia = models.CharField(max_length=500)
    ultima_actualizacion = models.DateTimeField()
    id_caja_mercadopago = models.CharField(max_length=255, blank=True, null=True)
    usar_mercadopago = models.BooleanField()
    aplicacion = models.CharField(max_length=255, blank=True, null=True)
    actualizarcatalogos = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_dispositivos'


class RegistroEnlacesrm(models.Model):
    idestacion = models.CharField(primary_key=True, max_length=50)
    ultimo_acceso = models.DateTimeField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'registro_enlacesrm'


class RegistroLicencias(models.Model):
    idregistros = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    tipomodulo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True, db_comment='1=principal 2=modulo')
    nombre = models.CharField(max_length=200, blank=True, null=True)
    fechacompra = models.DateTimeField(blank=True, null=True)
    numerofactura = models.CharField(max_length=100, blank=True, null=True)
    distribuidor = models.CharField(max_length=250, blank=True, null=True)
    numerocontrol = models.CharField(max_length=200, blank=True, null=True)
    contraseniacontrol = models.CharField(max_length=150, blank=True, null=True)
    tipolicencia = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True, db_comment='1=permanente 2=renta')
    mesanio = models.CharField(max_length=100, blank=True, null=True)
    licencia = models.CharField(max_length=150, blank=True, null=True)
    estaciones = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)
    foliosusadosfe = models.CharField(max_length=150, blank=True, null=True)
    limitefoliosfe = models.CharField(max_length=150, blank=True, null=True)
    foliosrestantescfdi = models.CharField(max_length=150, blank=True, null=True)
    seriesistema = models.TextField()
    fecha_vencimiento = models.CharField(max_length=50)
    tipo = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'registro_licencias'


class Registroasistencias(models.Model):
    idmovto = models.CharField(max_length=15, blank=True, null=True)
    idempleado = models.CharField(max_length=15, blank=True, null=True)
    entrada = models.DateTimeField(blank=True, null=True)
    salida = models.DateTimeField(blank=True, null=True)
    tipo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroasistencias'


class Registrocomedorotm(models.Model):
    id = models.AutoField(primary_key=True)
    idempleado = models.CharField(db_column='Idempleado', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(blank=True, null=True)
    estacion = models.CharField(max_length=50, blank=True, null=True)
    lector = models.CharField(max_length=50, blank=True, null=True)
    entregado = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrocomedorotm'


class Renta(models.Model):
    mesaño = models.CharField(max_length=100, blank=True, null=True)
    licencia = models.CharField(max_length=150, blank=True, null=True)
    modulo = models.CharField(max_length=200, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    estatus = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'renta'


class Reservaciones(models.Model):
    idreservacion = models.CharField(primary_key=True, max_length=25)
    idtiporeservacion = models.ForeignKey('Tiporeservaciones', models.DO_NOTHING, db_column='idtiporeservacion', blank=True, null=True)
    idarearestaurant = models.ForeignKey(Areasrestaurant, models.DO_NOTHING, db_column='idarearestaurant', blank=True, null=True)
    idcomisionista = models.ForeignKey(Comisionistas, models.DO_NOTHING, db_column='idcomisionista', blank=True, null=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    estatus = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    motivocancelacion = models.CharField(max_length=150, blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    fechacancelacion = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    pax = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fechaaltareserva = models.DateTimeField(blank=True, null=True)
    fechareserva = models.DateTimeField(blank=True, null=True)
    mesareservada = models.CharField(max_length=150, blank=True, null=True)
    usuarioreserva = models.CharField(max_length=15, blank=True, null=True)
    folio = models.BigIntegerField(blank=True, null=True)
    fumar = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservaciones'


class Saldosclientes(models.Model):
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    saldo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saldosclientes'


class Servicecodes(models.Model):
    servicecode = models.CharField(primary_key=True, max_length=50)
    descripcion = models.CharField(max_length=200)
    sistema = models.SmallIntegerField()
    tipo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'servicecodes'


class Serviciominutospatin(models.Model):
    idservicio = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idservicio', blank=True, null=True)
    tiempo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serviciominutospatin'


class Serviciosns(models.Model):
    id = models.AutoField(primary_key=True)
    idsistema = models.IntegerField()
    prioridad = models.IntegerField()
    urlservicio = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'serviciosns'


class Sincronizacion(models.Model):
    idsincronizacion = models.AutoField(primary_key=True, db_comment='Clave autoincremental de la ta')
    tabla = models.CharField(max_length=50, blank=True, null=True, db_comment='Nombre de la tabla modificada')
    idtabla = models.CharField(max_length=50, blank=True, null=True, db_comment='id de la tabla modificada')
    valoridtabla = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='Define si la sucursal a sincro')
    fechamovto = models.DateTimeField(blank=True, null=True, db_comment='Fecha en que se hizo el movto ')
    usuariomovto = models.CharField(max_length=20, blank=True, null=True, db_comment='Nombre de usuario que realiza ')
    proceso = models.IntegerField(blank=True, null=True, db_comment='Define el tipo de proceso real')
    fechaactualizacion = models.DateTimeField(blank=True, null=True, db_comment='Fecha en que la sucursal desca')
    usuarioactualizacion = models.CharField(max_length=20, blank=True, null=True, db_comment='Nombre de usuario que descarga')
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idtabla2 = models.CharField(max_length=50, blank=True, null=True)
    valoridtabla2 = models.CharField(max_length=100, blank=True, null=True)
    offline = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sincronizacion'


class SincronizacionBitacora(models.Model):
    idsincronizacion = models.AutoField(primary_key=True, db_comment='Clave autoincremental de la ta')
    tabla = models.CharField(max_length=50, blank=True, null=True, db_comment='Nombre de la tabla modificada')
    idtabla = models.CharField(max_length=50, blank=True, null=True, db_comment='id de la tabla modificada')
    valoridtabla = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='Define si la sucursal a sincro')
    fechamovto = models.DateTimeField(blank=True, null=True, db_comment='Fecha en que se hizo el movto ')
    usuariomovto = models.CharField(max_length=20, blank=True, null=True, db_comment='Nombre de usuario que realiza ')
    proceso = models.IntegerField(blank=True, null=True, db_comment='Define el tipo de proceso real')
    fechaactualizacion = models.DateTimeField(blank=True, null=True, db_comment='Fecha en que la sucursal desca')
    usuarioactualizacion = models.CharField(max_length=20, blank=True, null=True, db_comment='Nombre de usuario que descarga')
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    idtabla2 = models.CharField(max_length=50, blank=True, null=True)
    valoridtabla2 = models.CharField(max_length=100, blank=True, null=True)
    offline = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sincronizacion_bitacora'


class Stockinsumos(models.Model):
    idinsumo = models.ForeignKey(Insumos, models.DO_NOTHING, db_column='idinsumo', blank=True, null=True)
    idinsumospresentaciones = models.ForeignKey(Insumospresentaciones, models.DO_NOTHING, db_column='idinsumospresentaciones', blank=True, null=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    stockminimo = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    stockideal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    stockmaximo = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stockinsumos'


class Subgrupos(models.Model):
    idsubgrupo = models.CharField(primary_key=True, max_length=4)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    imagenmenuelectronico = models.BinaryField(blank=True, null=True)
    id_etiqueta = models.CharField(max_length=50)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    servicecode = models.CharField(max_length=50, blank=True, null=True)
    idbo = models.IntegerField(db_column='IdBO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subgrupos'


class Subgruposproductos(models.Model):
    idsubgrupo = models.ForeignKey(Subgrupos, models.DO_NOTHING, db_column='idsubgrupo', blank=True, null=True)
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subgruposproductos'


class Subtipogastos(models.Model):
    idsubtipogastos = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    idtipogasto = models.ForeignKey('Tipogastos', models.DO_NOTHING, db_column='idtipogasto', blank=True, null=True)
    idtipogastos = models.CharField(max_length=5, blank=True, null=True)
    idproveedor = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subtipogastos'


class Sucursalescallcenter(models.Model):
    idsucursal = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    direccion = models.CharField(max_length=120, blank=True, null=True)
    activa = models.BooleanField(blank=True, null=True)
    lunestrabaja = models.BooleanField(blank=True, null=True)
    martestrabaja = models.BooleanField(blank=True, null=True)
    miercolestrabaja = models.BooleanField(blank=True, null=True)
    juevestrabaja = models.BooleanField(blank=True, null=True)
    viernestrabaja = models.BooleanField(blank=True, null=True)
    sabadotrabaja = models.BooleanField(blank=True, null=True)
    domingotrabaja = models.BooleanField(blank=True, null=True)
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    lunesdiafin = models.IntegerField(blank=True, null=True)
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    martesdiafin = models.IntegerField(blank=True, null=True)
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    miercolesdiafin = models.IntegerField(blank=True, null=True)
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    juevesdiafin = models.IntegerField(blank=True, null=True)
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    viernesdiafin = models.IntegerField(blank=True, null=True)
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    sabadodiafin = models.IntegerField(blank=True, null=True)
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    domingodiafin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursalescallcenter'


class Tablaaux(models.Model):
    tabla = models.CharField(max_length=100, blank=True, null=True)
    valor = models.CharField(max_length=250, blank=True, null=True)
    movimiento = models.CharField(max_length=50, blank=True, null=True)
    aplicacion = models.CharField(max_length=250, blank=True, null=True)
    estacion = models.CharField(max_length=250, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tablaaux'


class Tempbitacoraeasygoband(models.Model):
    idbitacora = models.BigAutoField(primary_key=True)
    folio = models.BigIntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    idformadepago = models.CharField(max_length=5)
    servicecode = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=14, decimal_places=4)
    type = models.CharField(max_length=50)
    accountid = models.CharField(max_length=250)
    transactionid = models.CharField(max_length=250)
    guestid = models.CharField(max_length=250)
    transactionid_cancelled = models.CharField(max_length=250)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4)
    exchange_currency_id = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'tempbitacoraeasygoband'


class Tempbitacoratarjetacredito(models.Model):
    folio = models.BigIntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=100, blank=True, null=True)
    cuenta = models.CharField(max_length=100, blank=True, null=True)
    vencimiento = models.CharField(max_length=30, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    reimpresiones = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    mensajederespuesta = models.CharField(max_length=250, blank=True, null=True)
    procedimiento = models.CharField(max_length=50, blank=True, null=True)
    afiliacion = models.CharField(max_length=200, blank=True, null=True)
    statustransaccion = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idtransaccion = models.CharField(max_length=200, blank=True, null=True)
    numerooperacion = models.CharField(max_length=200, blank=True, null=True)
    informaciontarjeta = models.CharField(max_length=200, blank=True, null=True)
    tipotarjeta = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    arqc = models.CharField(max_length=200, blank=True, null=True)
    apn = models.CharField(max_length=200, blank=True, null=True)
    apnlabel = models.CharField(max_length=200, blank=True, null=True)
    transactiontype = models.CharField(max_length=200)
    applicationcryptogram = models.CharField(max_length=200)
    entrymethod = models.CharField(max_length=200)
    approvalcode = models.CharField(max_length=200)
    paymenttype = models.CharField(max_length=200)
    cardholderverificationmethod = models.SmallIntegerField()
    impresomovilcopia = models.BooleanField()
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    marcatarjeta = models.CharField(max_length=200, blank=True, null=True)
    banco = models.CharField(max_length=200, blank=True, null=True)
    terminal = models.CharField(max_length=200, blank=True, null=True)
    foliokiosko = models.CharField(max_length=100, blank=True, null=True)
    tempnumcheque = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    referenciacomercio = models.CharField(max_length=200, blank=True, null=True)
    nombretitular = models.CharField(max_length=250, blank=True, null=True)
    formatomovil = models.SmallIntegerField(blank=True, null=True)
    impresomovil = models.BooleanField()
    datosimpresion = models.TextField(blank=True, null=True)
    datosimpresioncopia = models.TextField(blank=True, null=True)
    puntosredimidos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puntospesosredimidos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    saldodisponiblepuntos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    saldodisponiblepesos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    saldoanteriorpuntos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    saldoanteriorpesos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempbitacoratarjetacredito'


class Tempbitacoratransacciones(models.Model):
    folio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    autorizacion = models.CharField(max_length=15, blank=True, null=True)
    referencia = models.CharField(max_length=15, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    reimpresiones = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    procedimiento = models.CharField(max_length=15, blank=True, null=True)
    datosenvio = models.CharField(max_length=254, blank=True, null=True)
    datosrespuesta = models.CharField(max_length=254, blank=True, null=True)
    medusafol_prov = models.CharField(max_length=15, blank=True, null=True)
    medusafol_ope = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempbitacoratransacciones'


class Tempcancela(models.Model):
    foliocheque = models.BigIntegerField(blank=True, null=True)
    comanda = models.CharField(max_length=8, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    clave = models.ForeignKey(Productos, models.DO_NOTHING, db_column='clave', blank=True, null=True)
    razon = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idmotivocancela = models.TextField(blank=True, null=True)  # This field type is a guess.
    saledetailid = models.CharField(max_length=250, blank=True, null=True)
    procesadosrx = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tempcancela'


class Tempcheqdet(models.Model):
    foliodet = models.BigIntegerField(blank=True, null=True)
    movimiento = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    comanda = models.CharField(max_length=8, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    preciosinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tiempo = models.CharField(max_length=20, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    modificador = models.BooleanField(blank=True, null=True)
    mitad = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    idestacion = models.CharField(max_length=40, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    horaproduccion = models.DateTimeField(blank=True, null=True)
    idproductocompuesto = models.CharField(max_length=15, blank=True, null=True)
    productocompuestoprincipal = models.BooleanField(blank=True, null=True)
    preciocatalogo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    marcar = models.BooleanField(blank=True, null=True)
    idmeseroproducto = models.CharField(max_length=4, blank=True, null=True)
    prioridadproduccion = models.CharField(max_length=1, blank=True, null=True)
    estatuspatin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idcortesia = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=16, blank=True, null=True)
    estadomonitor = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    llavemovto = models.CharField(max_length=100, blank=True, null=True)
    horameserofinalizado = models.DateTimeField(blank=True, null=True)
    meserofinalizado = models.CharField(max_length=4, blank=True, null=True)
    folioproduccion = models.SmallIntegerField(blank=True, null=True)
    nivel = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sistema_envio = models.IntegerField()
    promovolumen = models.BooleanField()
    iddispositivo = models.IntegerField()
    productsyncidsr = models.IntegerField()
    subtotalsrx = models.DecimalField(max_digits=7, decimal_places=5)
    totalsrx = models.DecimalField(max_digits=7, decimal_places=5)
    idmovtobillar = models.BigIntegerField()
    idlistaprecio = models.IntegerField(blank=True, null=True)
    tipocambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuestoimporte3 = models.DecimalField(max_digits=19, decimal_places=4)
    estrateca_discountcode = models.CharField(db_column='estrateca_DiscountCode', max_length=50)  # Field name made lowercase.
    estrateca_discountid = models.CharField(db_column='estrateca_DiscountID', max_length=50)  # Field name made lowercase.
    estrateca_discountamount = models.DecimalField(db_column='estrateca_DiscountAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    saledetailid = models.CharField(max_length=250, blank=True, null=True)
    procesadosrx = models.BooleanField()
    comanda_impresa = models.BooleanField(blank=True, null=True)
    preciosinimpuestos_ec = models.BinaryField(blank=True, null=True)
    precio_ec = models.BinaryField(blank=True, null=True)
    escargoarea = models.BooleanField()
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempcheqdet'


class Tempcheqdetauthsrx(models.Model):
    foliodet = models.BigIntegerField(blank=True, null=True)
    movimiento = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    saledetailid = models.CharField(max_length=250, blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    modificador = models.BooleanField(blank=True, null=True)
    idproductocompuesto = models.CharField(max_length=15, blank=True, null=True)
    productocompuestoprincipal = models.BooleanField(blank=True, null=True)
    nivel = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    statussr = models.IntegerField(db_column='statusSR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempcheqdetauthsrx'


class Tempcheqpedidos(models.Model):
    foliocheque = models.BigIntegerField(blank=True, null=True)
    idpedido = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempcheqpedidos'


class Tempcheques(models.Model):
    folio = models.BigAutoField(primary_key=True)
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    numcheque = models.BigIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    salidarepartidor = models.DateTimeField(blank=True, null=True)
    arriborepartidor = models.DateTimeField(blank=True, null=True)
    cierre = models.DateTimeField(blank=True, null=True)
    mesa = models.CharField(max_length=100, blank=True, null=True)
    nopersonas = models.IntegerField(blank=True, null=True)
    idmesero = models.CharField(max_length=4, blank=True, null=True)
    pagado = models.BooleanField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    impreso = models.BooleanField(blank=True, null=True)
    impresiones = models.IntegerField(blank=True, null=True)
    cambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    reabiertas = models.IntegerField(blank=True, null=True)
    razoncancelado = models.CharField(max_length=255, blank=True, null=True)
    orden = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    facturado = models.BooleanField(blank=True, null=True)
    idcliente = models.CharField(max_length=15, blank=True, null=True)
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    tipodeservicio = models.IntegerField(blank=True, null=True)
    idturno = models.BigIntegerField(blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    estacion = models.CharField(max_length=40, blank=True, null=True)
    cambiorepartidor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    fechacancelado = models.DateTimeField(blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=30, blank=True, null=True)
    folionotadeconsumo = models.BigIntegerField(blank=True, null=True)
    notadeconsumo = models.BooleanField(blank=True, null=True)
    propinapagada = models.BooleanField(blank=True, null=True)
    propinafoliomovtocaja = models.BigIntegerField(blank=True, null=True)
    puntosmonederogenerados = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propinaincluida = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjetadescuento = models.CharField(max_length=30, blank=True, null=True)
    porcentajefac = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    propinamanual = models.BooleanField(blank=True, null=True)
    usuariopago = models.CharField(max_length=15, blank=True, null=True)
    idclientefacturacion = models.CharField(max_length=15, blank=True, null=True)
    cuentaenuso = models.BooleanField(blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    idclientedomicilio = models.CharField(max_length=15, blank=True, null=True)
    iddireccion = models.CharField(max_length=15, blank=True, null=True)
    telefonousadodomicilio = models.CharField(max_length=50, blank=True, null=True)
    totalarticulos = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    subtotalsinimpuestos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconpropina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalimpuesto1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconcargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconpropinacargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentoimporte = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    efectivo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    otros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propinatarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    campoadicional1 = models.CharField(max_length=250, blank=True, null=True)
    idreservacion = models.CharField(max_length=25, blank=True, null=True)
    idcomisionista = models.CharField(max_length=15, blank=True, null=True)
    importecomision = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    comisionpagada = models.BooleanField(blank=True, null=True)
    fechapagocomision = models.DateTimeField(blank=True, null=True)
    foliopagocomision = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    tipoventarapida = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    callcenter = models.BooleanField(blank=True, null=True)
    idordencompra = models.BigIntegerField(blank=True, null=True)
    totalsindescuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalotros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentoalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentobebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentootros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesias = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiaalimentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiabebidas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalcortesiaotros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldescuentoycortesia = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalalimentossindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbebidassindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalotrossindescuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuentocriterio = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    descuentomonedero = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    idmenucomedor = models.CharField(max_length=15, blank=True, null=True)
    subtotalcondescuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    comisionpax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    procesadointerfaz = models.BooleanField(blank=True, null=True)
    domicilioprogramado = models.BooleanField(blank=True, null=True)
    fechadomicilioprogramado = models.DateTimeField(blank=True, null=True)
    enviado = models.BooleanField(blank=True, null=True)
    ncf = models.CharField(max_length=19, blank=True, null=True)
    numerocuenta = models.CharField(max_length=100, blank=True, null=True)
    codigo_unico_af = models.CharField(max_length=30, blank=True, null=True)
    estatushub = models.IntegerField(blank=True, null=True)
    idfoliohub = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    enviadorw = models.BooleanField(db_column='EnviadoRW', blank=True, null=True)  # Field name made lowercase.
    usuarioapertura = models.CharField(max_length=15)
    titulartarjetamonedero = models.CharField(max_length=100, blank=True, null=True)
    saldoanteriormonedero = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    autorizacionfolio = models.CharField(max_length=50, blank=True, null=True)
    fechalimiteemision = models.DateTimeField(blank=True, null=True)
    totalimpuestod1 = models.DecimalField(max_digits=19, decimal_places=4)
    totalimpuestod2 = models.DecimalField(max_digits=19, decimal_places=4)
    totalimpuestod3 = models.DecimalField(max_digits=19, decimal_places=4)
    idmotivocancela = models.CharField(max_length=200, blank=True, null=True)
    sistema_envio = models.IntegerField()
    idformadepagodescuento = models.CharField(db_column='idformadepagoDescuento', max_length=5)  # Field name made lowercase.
    titulartarjetamonederodescuento = models.CharField(max_length=100)
    c_iddispositivo = models.IntegerField()
    salerestaurantid = models.TextField()
    timemarktoconfirmed = models.DateTimeField(blank=True, null=True)
    timemarktodelivery = models.DateTimeField(blank=True, null=True)
    timemarktodeliveryarrive = models.DateTimeField(blank=True, null=True)
    esalestatus = models.IntegerField()
    statussr = models.IntegerField(db_column='statusSR')  # Field name made lowercase.
    paymentreference = models.CharField(max_length=50)
    deliverycharge = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)
    comandaimpresa = models.BooleanField(blank=True, null=True)
    foodorder = models.IntegerField()
    cashpaymentwith = models.DecimalField(max_digits=19, decimal_places=4)
    paymentmethod_id = models.IntegerField()
    surveycode = models.CharField(max_length=18)
    intentoenvioaf = models.IntegerField(db_column='intentoEnvioAF')  # Field name made lowercase.
    pedidovistosrx = models.BooleanField()
    impresoenbitacorasrm = models.BooleanField()
    cuentapagadaprocesada = models.BooleanField(blank=True, null=True)
    tkc_token = models.CharField(db_column='TKC_Token', max_length=50)  # Field name made lowercase.
    tkc_transaction = models.CharField(db_column='TKC_Transaction', max_length=100)  # Field name made lowercase.
    tkc_authorization = models.CharField(db_column='TKC_Authorization', max_length=100)  # Field name made lowercase.
    tkc_cupon = models.CharField(db_column='TKC_Cupon', max_length=100)  # Field name made lowercase.
    tkc_expirationdate = models.CharField(db_column='TKC_ExpirationDate', max_length=100)  # Field name made lowercase.
    tkc_recompensa = models.DecimalField(db_column='TKC_Recompensa', max_digits=19, decimal_places=4)  # Field name made lowercase.
    campoadicional2 = models.CharField(max_length=250)
    campoadicional3 = models.CharField(max_length=250)
    estrateca_cardnumber = models.CharField(db_column='estrateca_CardNumber', max_length=100)  # Field name made lowercase.
    estrateca_vouchertext = models.TextField(db_column='estrateca_VoucherText')  # Field name made lowercase.
    campoadicional4 = models.CharField(max_length=250)
    campoadicional5 = models.CharField(max_length=250)
    sacoa_cardnumber = models.CharField(db_column='sacoa_CardNumber', max_length=100)  # Field name made lowercase.
    sacoa_credits = models.DecimalField(max_digits=19, decimal_places=4)
    estrateca_typedisccount = models.CharField(db_column='estrateca_TypeDisccount', max_length=50)  # Field name made lowercase.
    estrateca_discountcode = models.CharField(db_column='estrateca_DiscountCode', max_length=50)  # Field name made lowercase.
    estrateca_discountid = models.CharField(db_column='estrateca_DiscountID', max_length=50)  # Field name made lowercase.
    estrateca_discountamount = models.DecimalField(db_column='estrateca_DiscountAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desc_imp_original = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    donativo = models.DecimalField(max_digits=19, decimal_places=4)
    totalcondonativo = models.DecimalField(max_digits=19, decimal_places=4)
    totalconpropinacargodonativo = models.DecimalField(max_digits=19, decimal_places=4)
    orderreference = models.CharField(max_length=500)
    appname = models.CharField(max_length=250)
    paymentproviderid = models.CharField(max_length=50)
    paymentprovider = models.CharField(max_length=250)
    changestatussrx = models.BooleanField(db_column='ChangeStatusSRX', blank=True, null=True)  # Field name made lowercase.
    datedownload = models.DateTimeField(db_column='DateDownload', blank=True, null=True)  # Field name made lowercase.
    comandaimpresacancelada = models.BooleanField(blank=True, null=True)
    empaquetado = models.DateTimeField(blank=True, null=True)
    status_domicilio = models.IntegerField()
    asignacion = models.DateTimeField(blank=True, null=True)
    enviopagado = models.BooleanField()
    diet_restrictions = models.CharField(max_length=250)
    sl_cupon_descuento = models.CharField(max_length=250)
    sl_tipo_cupon = models.CharField(max_length=50)
    sl_importe_descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tuki_cardnumber = models.CharField(db_column='TUKI_CardNumber', max_length=250)  # Field name made lowercase.
    tuki_accumulatedpoints = models.DecimalField(db_column='TUKI_AccumulatedPoints', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tuki_currentpoints = models.DecimalField(db_column='TUKI_CurrentPoints', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sl_num_cupones = models.DecimalField(max_digits=16, decimal_places=6, blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36)  # Field name made lowercase.
    sentsync = models.BooleanField(db_column='SentSync')  # Field name made lowercase.
    procesar_descuento_emenu = models.BooleanField()
    procesar_descuento_sr = models.BooleanField()
    imprimenotabluetooth = models.BooleanField()
    datosimpresionnotaconsumo = models.TextField()
    subtotal_ec = models.BinaryField(blank=True, null=True)
    total_ec = models.BinaryField(blank=True, null=True)
    totalconpropinacargo_ec = models.BinaryField(blank=True, null=True)
    mv_room = models.CharField(max_length=100)
    mv_lastname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tempcheques'


class Tempchequespagos(models.Model):
    folio = models.BigIntegerField(blank=True, null=True)
    idformadepago = models.ForeignKey(Formasdepago, models.DO_NOTHING, db_column='idformadepago', blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tipodecambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    referencia = models.TextField(blank=True, null=True)
    sistema_envio = models.IntegerField()
    importe_ec = models.BinaryField(blank=True, null=True)
    propina_ec = models.BinaryField(blank=True, null=True)
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36)  # Field name made lowercase.
    cardbrand = models.CharField(db_column='cardBrand', max_length=120)  # Field name made lowercase.
    importe_cashdro = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempchequespagos'


class Tempexplosioninsumosdetalle(models.Model):
    idexplosion = models.ForeignKey('Tempexplosionproductos', models.DO_NOTHING, db_column='idexplosion')
    idproducto = models.CharField(max_length=15)
    idinsumo = models.CharField(max_length=15)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4)
    costo = models.DecimalField(max_digits=19, decimal_places=4)
    costopromedio = models.DecimalField(max_digits=19, decimal_places=4)
    unidad = models.CharField(max_length=10)
    rendimientoelaborado = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    elaborado = models.BooleanField()
    impuesto1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    impuesto3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    idelaborado = models.CharField(max_length=15)
    nivel = models.SmallIntegerField()
    ordengenerada = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tempexplosioninsumosdetalle'


class Tempexplosionproductos(models.Model):
    folio = models.IntegerField()
    fecha = models.DateTimeField()
    usuario = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=100)
    estatus = models.SmallIntegerField()
    explosionparaordencompra = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tempexplosionproductos'


class Tempexplosionproductosdetalle(models.Model):
    id = models.ForeignKey(Tempexplosionproductos, models.DO_NOTHING, db_column='id')
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto')
    cantidad = models.DecimalField(max_digits=14, decimal_places=4)
    id_epd = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tempexplosionproductosdetalle'


class Tempfoliosfacturados(models.Model):
    idfactura = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='idfactura', blank=True, null=True)
    folio = models.BigIntegerField(blank=True, null=True)
    porcentajefac = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempfoliosfacturados'


class Tempnotificaciones(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    estatus_notificacion = models.BooleanField()
    foliocuenta = models.BigIntegerField()
    idcuenta = models.CharField(max_length=15)
    idmesero = models.CharField(max_length=10)
    mensaje = models.TextField()
    hora = models.DateTimeField()
    tipo_notificacion = models.IntegerField()
    hora_leido = models.DateTimeField()
    sistema_leido = models.IntegerField()
    idarearestaurant = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'tempnotificaciones'


class Tempnumerostarjetas(models.Model):
    foliocuenta = models.BigIntegerField(blank=True, null=True)
    idformadepago = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=50, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioautorizo = models.CharField(max_length=20, blank=True, null=True)
    titulartarjetamonedero = models.CharField(max_length=100, blank=True, null=True)
    saldoanteriormonedero = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sistema = models.SmallIntegerField()
    foliokiosco = models.CharField(max_length=36, blank=True, null=True)
    refidempresa = models.CharField(db_column='refIdEmpresa', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refnombreempresa = models.CharField(db_column='refNombreEmpresa', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempnumerostarjetas'


class Tipoclientes(models.Model):
    idtipocliente = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    idtipoclientesr = models.AutoField(db_column='idtipoclienteSR', primary_key=True)  # Field name made lowercase.
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoclientes'


class Tipoclientespricelist(models.Model):
    tipoclientespricelist = models.CharField(db_column='tipoclientesPriceList', primary_key=True, max_length=36)  # Field name made lowercase.
    fkidtipocliente = models.ForeignKey(Tipoclientes, models.DO_NOTHING, db_column='FKidtipocliente')  # Field name made lowercase.
    fkpricelist = models.ForeignKey(Pricelists, models.DO_NOTHING, db_column='FKPriceList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoclientesPriceList'


class Tipocomisionistas(models.Model):
    idtipocomisionista = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipocomisionistas'


class Tipodescuento(models.Model):
    idtipodescuento = models.CharField(primary_key=True, max_length=5)
    desc_tipodescuento = models.CharField(max_length=30, blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    visible = models.BooleanField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.
    imp_maximo_descuento = models.DecimalField(max_digits=12, decimal_places=2)
    activar_maximo_descuento = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tipodescuento'


class Tipoempresa(models.Model):
    idtipoempresa = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoempresa'


class Tipoformaspagos(models.Model):
    idtipoformaspago = models.CharField(db_column='Idtipoformaspago', max_length=10, blank=True, null=True)  # Field name made lowercase.
    desc_tipoformaspago = models.CharField(db_column='Desc_tipoformaspago', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoformaspagos'


class Tipogastos(models.Model):
    idtipogasto = models.CharField(db_column='Idtipogasto', primary_key=True, max_length=5)  # Field name made lowercase.
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipogastos'


class Tipomenuclientes(models.Model):
    idtipomenu = models.CharField(max_length=5, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipomenuclientes'


class Tipopedido(models.Model):
    idtipopedido = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipopedido'


class Tipoproveedores(models.Model):
    idtipoproveedor = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoproveedores'


class Tiporeservaciones(models.Model):
    idtiporeservacion = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    solicitacomisionista = models.BooleanField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiporeservaciones'


class Tiposdemesa(models.Model):
    idtipomesa = models.CharField(primary_key=True, max_length=15)
    tipodemesa = models.CharField(max_length=20, blank=True, null=True)
    personas = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    tipo_imagen = models.SmallIntegerField(blank=True, null=True)
    mesa_juegos = models.BooleanField(blank=True, null=True)
    minutosbillar = models.IntegerField(blank=True, null=True)
    costobillar = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    costoinicialbillar = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    conceptobillar = models.CharField(max_length=15, blank=True, null=True)
    minutosiniciobillar = models.IntegerField(blank=True, null=True)
    usarpreciosporhora = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tiposdemesa'


class Tiposdemesadetalles(models.Model):
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    idtipomesa = models.ForeignKey(Tiposdemesa, models.DO_NOTHING, db_column='idtipomesa', blank=True, null=True)
    descargar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiposdemesadetalles'


class Tiposervicio(models.Model):
    idtiposervicio = models.CharField(db_column='Idtiposervicio', max_length=10, blank=True, null=True)  # Field name made lowercase.
    desc_tiposervicio = models.CharField(db_column='Desc_tiposervicio', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiposervicio'


class Traspasosalmacen(models.Model):
    folio = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    fecha = models.DateTimeField(blank=True, null=True)
    almacenorigen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='almacenorigen', blank=True, null=True)
    almacendestino = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='almacendestino', related_name='traspasosalmacen_almacendestino_set', blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    nota = models.CharField(max_length=150, blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    idempresaorigen = models.CharField(max_length=15, blank=True, null=True)
    idempresadestino = models.CharField(max_length=15, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    editadosucursal = models.BooleanField(blank=True, null=True)
    foliocentral = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traspasosalmacen'


class Turnos(models.Model):
    idturnointerno = models.BigAutoField(primary_key=True)
    idturno = models.BigIntegerField(blank=True, null=True)
    fondo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    apertura = models.DateTimeField(blank=True, null=True)
    cierre = models.DateTimeField(blank=True, null=True)
    idestacion = models.ForeignKey(Estaciones, models.DO_NOTHING, db_column='idestacion', blank=True, null=True)
    cajero = models.CharField(max_length=15, blank=True, null=True)
    efectivo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    credito = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    procesadoweb = models.BooleanField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    fechaenviado = models.DateTimeField(blank=True, null=True)
    usuarioenvio = models.CharField(max_length=30, blank=True, null=True)
    offline = models.BooleanField(blank=True, null=True)
    enviadoaf = models.BooleanField()
    corte_enviado = models.BooleanField()
    eliminartemporalesencierre = models.BooleanField()
    idmesero = models.CharField(max_length=4, blank=True, null=True)
    fondodolares = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    procesado = models.BooleanField()
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnos'


class Turnosf(models.Model):
    idturnointerno = models.BigAutoField(primary_key=True)
    idturno = models.BigIntegerField(blank=True, null=True)
    fondo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    apertura = models.DateTimeField(blank=True, null=True)
    cierre = models.DateTimeField(blank=True, null=True)
    idestacion = models.ForeignKey(Estaciones, models.DO_NOTHING, db_column='idestacion', blank=True, null=True)
    cajero = models.CharField(max_length=15, blank=True, null=True)
    efectivo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjeta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    credito = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    procesadoweb = models.BooleanField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    fechaenviado = models.DateTimeField(blank=True, null=True)
    usuarioenvio = models.CharField(max_length=30, blank=True, null=True)
    offline = models.BooleanField(blank=True, null=True)
    fondodolares = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turnosf'


class Ubicacionesempresa(models.Model):
    idubicacionempresa = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacionesempresa'


class Udsmedida(models.Model):
    idunidad = models.CharField(primary_key=True, max_length=50)
    idunidadmedida_sat = models.CharField(db_column='idunidadmedida_SAT', max_length=50)  # Field name made lowercase.
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'udsmedida'


class Udsmedidaequivale(models.Model):
    idunidad = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unidadequivale = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'udsmedidaequivale'


class Usuarios(models.Model):
    usuario = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    contraseña = models.CharField(max_length=150, blank=True, null=True)
    administrador = models.BooleanField(blank=True, null=True)
    perfil = models.CharField(max_length=15, blank=True, null=True)
    barraherramientas = models.IntegerField(blank=True, null=True)
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    accesomodulo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True, db_comment='acceso a modulo -- 1 todos - 2')
    estatuslogin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    status = models.BooleanField()
    passexpired = models.BooleanField()
    passlastchange = models.DateTimeField()
    aplicacomision = models.BooleanField()
    workspaceid = models.CharField(db_column='WorkspaceId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'


class Usuariosdescargar(models.Model):
    usuario = models.CharField(max_length=15, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    descargar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuariosdescargar'


class Usuariosperfiles(models.Model):
    idusuariosperfiles = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    autorizadoseguridad = models.BooleanField(blank=True, null=True)
    puedeeditaralmacen = models.BooleanField(blank=True, null=True)
    productos = models.BooleanField(blank=True, null=True)
    meseros = models.BooleanField(blank=True, null=True)
    clientes = models.BooleanField(blank=True, null=True)
    insumos = models.BooleanField(blank=True, null=True)
    almacenes = models.BooleanField(blank=True, null=True)
    conceptosmovtos = models.BooleanField(blank=True, null=True)
    proveedores = models.BooleanField(blank=True, null=True)
    promocionesdescuentos = models.BooleanField(blank=True, null=True)
    comisionistasreservaciones = models.BooleanField(blank=True, null=True)
    gastos = models.BooleanField(blank=True, null=True)
    cuentasporcobrarconsulta = models.BooleanField(blank=True, null=True)
    cuentasporpagar = models.BooleanField(blank=True, null=True)
    reservaciones = models.BooleanField(blank=True, null=True)
    pagodecomisiones = models.BooleanField(blank=True, null=True)
    cierrediario = models.BooleanField(blank=True, null=True)
    pedidos = models.BooleanField(blank=True, null=True)
    ordenesdecompra = models.BooleanField(blank=True, null=True)
    compras = models.BooleanField(blank=True, null=True)
    movtosalmacen = models.BooleanField(blank=True, null=True)
    traspasos = models.BooleanField(blank=True, null=True)
    inventariofisico = models.BooleanField(blank=True, null=True)
    elaboracion = models.BooleanField(blank=True, null=True)
    desperdicios = models.BooleanField(blank=True, null=True)
    explosioninsumos = models.BooleanField(blank=True, null=True)
    costosinsumosproveedor = models.BooleanField(blank=True, null=True)
    recepciondearchivoproductos = models.BooleanField(blank=True, null=True)
    monitordeventas = models.BooleanField(blank=True, null=True)
    consultarturnos = models.BooleanField(blank=True, null=True)
    consultadeprecios = models.BooleanField(blank=True, null=True)
    consultarturnosabiertos = models.BooleanField(blank=True, null=True)
    consultadecuentas = models.BooleanField(blank=True, null=True)
    consultadefacturas = models.BooleanField(blank=True, null=True)
    consultaderetirosdepositos = models.BooleanField(blank=True, null=True)
    consultasaldotarjetas = models.BooleanField(blank=True, null=True)
    consultabitacorahotel = models.BooleanField(blank=True, null=True)
    reportesadmon = models.BooleanField(blank=True, null=True)
    reportesventas = models.BooleanField(blank=True, null=True)
    reportescaja = models.BooleanField(blank=True, null=True)
    reportescompras = models.BooleanField(blank=True, null=True)
    reportesalmacen = models.BooleanField(blank=True, null=True)
    reportescostos = models.BooleanField(blank=True, null=True)
    reportescuentasporpagar = models.BooleanField(blank=True, null=True)
    manttoexportarimportar = models.BooleanField(blank=True, null=True)
    manttoherramientasadmin = models.BooleanField(blank=True, null=True)
    aperturacierreturno = models.BooleanField(blank=True, null=True)
    pagarpropinas = models.BooleanField(blank=True, null=True)
    retirosdepositos = models.BooleanField(blank=True, null=True)
    cortedecaja = models.BooleanField(blank=True, null=True)
    serviciocomedor = models.BooleanField(blank=True, null=True)
    serviciodomicilio = models.BooleanField(blank=True, null=True)
    serviciorapido = models.BooleanField(blank=True, null=True)
    facturacion = models.BooleanField(blank=True, null=True)
    cuentasporcobrar = models.BooleanField(blank=True, null=True)
    imprimirnotadeconsumonueva = models.BooleanField(blank=True, null=True)
    traspasodesdecentrodeconsumo = models.BooleanField(blank=True, null=True)
    inventariofisicociego = models.BooleanField(blank=True, null=True)
    configuracion = models.BooleanField(blank=True, null=True)
    consultaimpresorafiscal = models.BooleanField(blank=True, null=True)
    consultahabitacion = models.BooleanField(blank=True, null=True)
    cortedecajaz = models.BooleanField(blank=True, null=True)
    repartidores = models.BooleanField(blank=True, null=True)
    reportescontabilidad = models.BooleanField(blank=True, null=True)
    cambiodeusuario = models.BooleanField(blank=True, null=True)
    tipodescuento = models.BooleanField(blank=True, null=True)
    abonarsaldotarjeta = models.BooleanField(blank=True, null=True)
    bdreindexado = models.BooleanField(blank=True, null=True)
    bdrespaldorecuperacion = models.BooleanField(blank=True, null=True)
    bdinicializar = models.BooleanField(blank=True, null=True)
    bdaccesar = models.BooleanField(blank=True, null=True)
    bdarreglar = models.BooleanField(blank=True, null=True)
    patinescontrol = models.BooleanField(blank=True, null=True)
    patinescatalogo = models.BooleanField(blank=True, null=True)
    patinesreporte = models.BooleanField(blank=True, null=True)
    billarcontrol = models.BooleanField(blank=True, null=True)
    billarcatalogo = models.BooleanField(blank=True, null=True)
    billarreporte = models.BooleanField(blank=True, null=True)
    cancelaciones = models.BooleanField(blank=True, null=True)
    reabrir = models.BooleanField(blank=True, null=True)
    descuentos = models.BooleanField(blank=True, null=True)
    incluirpropina = models.BooleanField(blank=True, null=True)
    reimprimir = models.BooleanField(blank=True, null=True)
    cambiarproductodemesa = models.BooleanField(blank=True, null=True)
    cambiodemesa = models.BooleanField(blank=True, null=True)
    juntarmesas = models.BooleanField(blank=True, null=True)
    seguridadprecioabierto = models.BooleanField(blank=True, null=True)
    seguridaddividircuentas = models.BooleanField(blank=True, null=True)
    autorizacioncancelaproductorapido = models.BooleanField(blank=True, null=True)
    autorizacioncierrecomandero = models.BooleanField(blank=True, null=True)
    autorizaciondeslizartarjeta = models.BooleanField(blank=True, null=True)
    autorizacioncambiarmesero = models.BooleanField(blank=True, null=True)
    autorizacioncargo = models.BooleanField(blank=True, null=True)
    autorizarpedidos = models.BooleanField(blank=True, null=True)
    enviarordenesemail = models.BooleanField(blank=True, null=True)
    abrircajon = models.BooleanField(blank=True, null=True)
    nuevo = models.BooleanField(blank=True, null=True)
    editar = models.BooleanField(blank=True, null=True)
    eliminar = models.BooleanField(blank=True, null=True)
    autorizacionacumularpuntos = models.BooleanField(blank=True, null=True)
    autorizacionpagoconpuntos = models.BooleanField(blank=True, null=True)
    autorizaciongruposcaptura = models.BooleanField(blank=True, null=True)
    autorizacionventacredito = models.BooleanField(blank=True, null=True)
    comedorempleados = models.BooleanField(blank=True, null=True)
    vercostocompra = models.BooleanField(blank=True, null=True)
    mapademesas = models.BooleanField(blank=True, null=True)
    bitacorasinc = models.BooleanField(blank=True, null=True)
    licenciasreg = models.BooleanField(blank=True, null=True)
    cortesiamonedero = models.BooleanField(blank=True, null=True)
    reimprimirfoliospagados = models.BooleanField(blank=True, null=True)
    tarjetadecredito = models.BooleanField(blank=True, null=True)
    conexionservidor = models.BooleanField(blank=True, null=True)
    actualizarsistemas = models.BooleanField(blank=True, null=True)
    cedis = models.BooleanField(blank=True, null=True)
    abonomonedero = models.BooleanField(blank=True, null=True)
    inventariopendiente = models.BooleanField(blank=True, null=True)
    empresas = models.BooleanField(blank=True, null=True)
    sucursalescallcenter = models.BooleanField(blank=True, null=True)
    areaventa = models.BooleanField(blank=True, null=True)
    descuentomaximopermitido = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    autorizacioncancelarproductos = models.BooleanField(blank=True, null=True)
    autorizacioncancelarcompras = models.BooleanField(blank=True, null=True)
    autorizacioncancelartraspasos = models.BooleanField(blank=True, null=True)
    autorizacioncancelarmovtosalmacen = models.BooleanField(blank=True, null=True)
    autorizacioncambiarfechaalmacen = models.BooleanField(blank=True, null=True)
    passwordsalirsistema = models.BooleanField(blank=True, null=True)
    reabrircuentapagada = models.BooleanField(blank=True, null=True)
    paises = models.BooleanField(blank=True, null=True)
    estados = models.BooleanField(blank=True, null=True)
    empresascentral = models.BooleanField(blank=True, null=True)
    facturacionmexico = models.BooleanField(blank=True, null=True)
    reporteconsolidado = models.BooleanField(blank=True, null=True)
    sincronizacioncatalogos = models.BooleanField(blank=True, null=True)
    autorizacionmodoinventario = models.BooleanField(blank=True, null=True)
    sincronizacion = models.BooleanField(blank=True, null=True)
    descargacatalogos = models.BooleanField(blank=True, null=True)
    cargacatalogos = models.BooleanField(blank=True, null=True)
    enviarorden = models.BooleanField()
    recetaproductos = models.BooleanField()
    recetainsumoselaborados = models.BooleanField()
    asignarhuelladigital = models.BooleanField()
    consultainsumosalerta = models.BooleanField()
    autorizaciontae = models.BooleanField(blank=True, null=True)
    suspenderproductos = models.BooleanField()
    visualizarcortextodos = models.BooleanField()
    editarfechacompras = models.BooleanField()
    formasdepagoturno = models.BooleanField()
    folioscomandas = models.BooleanField()
    activartipocredito = models.BooleanField()
    autorizacerrarturno = models.BooleanField()
    administrarmonitorcorte = models.BooleanField()
    actualizatipodecambio = models.BooleanField()
    cambiodemesamapa = models.BooleanField()
    autoriza_abono_sacoa = models.BooleanField()
    donativos = models.BooleanField()
    puedecerrarsrm = models.BooleanField()
    autorizaproduccionelabora = models.BooleanField()
    reporte_fiscal = models.BooleanField()
    autorizaproductosmenuqr = models.BooleanField()
    envio_ventas = models.BooleanField(db_column='ENVIO_VENTAS')  # Field name made lowercase.
    perfiles_seguridad = models.BooleanField()
    usuarios = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'usuariosperfiles'


class Usuariosperfilescatalogo(models.Model):
    idusuariosperfiles = models.ForeignKey(Usuariosperfiles, models.DO_NOTHING, db_column='idusuariosperfiles')
    catalogo = models.CharField(max_length=100, blank=True, null=True)
    nuevo = models.BooleanField(blank=True, null=True)
    editar = models.BooleanField(blank=True, null=True)
    eliminar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuariosperfilescatalogo'


class Validahuellamonedero(models.Model):
    idcliente = models.CharField(max_length=15, blank=True, null=True)
    huella = models.TextField(blank=True, null=True)  # This field type is a guess.
    huella2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    pic = models.TextField(blank=True, null=True)  # This field type is a guess.
    tarjetamonedero = models.CharField(max_length=20, blank=True, null=True)
    fechactualizahuella = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'validahuellamonedero'


class WorkspaceApps(models.Model):
    idapp = models.IntegerField(primary_key=True)
    nombreapp = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    applicationid = models.CharField(db_column='ApplicationId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    applicationkey = models.TextField(db_column='ApplicationKey', blank=True, null=True)  # Field name made lowercase.
    hasprices = models.BooleanField(db_column='HasPrices', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workspace_apps'


class WorkspaceAppsPricelists(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idapp = models.IntegerField(db_column='IdApp')  # Field name made lowercase.
    fkpricelist = models.CharField(db_column='FKPriceList', max_length=36)  # Field name made lowercase.
    isuse = models.BooleanField(db_column='IsUse')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workspace_apps_pricelists'


class WorkspacePlatformSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    idapp = models.ForeignKey(WorkspaceApps, models.DO_NOTHING, db_column='idapp')
    platform = models.CharField(max_length=100)
    idarearestaurant = models.ForeignKey(Areasrestaurant, models.DO_NOTHING, db_column='idarearestaurant')
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'workspace_platform_settings'


class WorkspaceSettings(models.Model):
    idapp = models.ForeignKey(WorkspaceApps, models.DO_NOTHING, db_column='idapp')
    idarearestaurant = models.ForeignKey(Areasrestaurant, models.DO_NOTHING, db_column='idarearestaurant')
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'workspace_settings'


class WsCloud(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    wsusuario = models.CharField(db_column='WSUsuario', max_length=50)  # Field name made lowercase.
    wsurl = models.CharField(db_column='WSUrl', max_length=500)  # Field name made lowercase.
    wscontrasena = models.CharField(db_column='WSContrasena', max_length=50)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=10)  # Field name made lowercase.
    recordarusuario = models.BooleanField(db_column='RecordarUsuario')  # Field name made lowercase.
    rwactivo = models.BooleanField(db_column='RWActivo')  # Field name made lowercase.
    rwtimer = models.IntegerField(db_column='RWTimer')  # Field name made lowercase.
    wsidsistema = models.IntegerField(db_column='WSIDSistema', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ws_cloud'


class Xpformasdepago(models.Model):
    idcuenta = models.IntegerField(db_column='IDCuenta', blank=True, null=True)  # Field name made lowercase.
    formadepago = models.CharField(db_column='FormaDePago', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xpFormasDePago'


class Xppasoventacabecero(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idcuenta = models.IntegerField(db_column='IDCuenta')  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=10)  # Field name made lowercase.
    folio = models.IntegerField(db_column='Folio')  # Field name made lowercase.
    fechaticket = models.DateTimeField(db_column='FechaTicket')  # Field name made lowercase.
    fechaproceso = models.DateTimeField(db_column='FechaProceso')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=12, decimal_places=2)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=12, decimal_places=2)  # Field name made lowercase.
    impuestos = models.DecimalField(db_column='Impuestos', max_digits=12, decimal_places=2)  # Field name made lowercase.
    serviciotipo = models.IntegerField(db_column='ServicioTipo')  # Field name made lowercase.
    formadepago = models.CharField(db_column='FormaDePago', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechaprocesod = models.DateTimeField(db_column='FechaProcesoD', blank=True, null=True)  # Field name made lowercase.
    idprocesod = models.IntegerField(db_column='IDProcesoD', blank=True, null=True)  # Field name made lowercase.
    estatuscuenta = models.CharField(db_column='EstatusCuenta', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xpPasoVentaCabecero'


class Xppasoventadetalle(models.Model):
    idcabecero = models.IntegerField(db_column='IDCabecero')  # Field name made lowercase.
    idcuenta = models.IntegerField(db_column='IDCuenta')  # Field name made lowercase.
    idproducto = models.CharField(db_column='IDProducto', max_length=20)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=12, decimal_places=2)  # Field name made lowercase.
    impuesto1 = models.FloatField(db_column='Impuesto1')  # Field name made lowercase.
    impuesto2 = models.FloatField(db_column='Impuesto2')  # Field name made lowercase.
    impuesto3 = models.FloatField(db_column='Impuesto3')  # Field name made lowercase.
    estatusproceso = models.CharField(db_column='EstatusProceso', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xpPasoVentaDetalle'


class XppasoInsumos(models.Model):
    folio = models.CharField(max_length=20, blank=True, null=True)
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=16, decimal_places=6, blank=True, null=True)
    idinsumo = models.CharField(max_length=15, blank=True, null=True)
    cantidad_insumo = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xpPaso_Insumos'

class Zonasdomicilio(models.Model):
    idzona = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    idproducto = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonasdomicilio'

class Zonasdomiciliodescargar(models.Model):
    idempresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    descargar = models.BooleanField()
    idzona = models.ForeignKey(Zonasdomicilio, models.DO_NOTHING, db_column='idzona', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonasdomiciliodescargar'

class Zonasdomiciliosucursales(models.Model):
    idzona = models.ForeignKey(Zonasdomicilio, models.DO_NOTHING, db_column='idzona')
    idsucursal = models.CharField(max_length=5, blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonasdomiciliosucursales'

class Zonasempresa(models.Model):
    idzonaempresa = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonasempresa'

## Proxys para el admin y formulario

class cheques_proxy(Cheques): #los proxys son para usuarios no administradores
    class Meta:
        proxy = True
        verbose_name = 'Cheque Proxy'
        verbose_name_plural = 'Proxy de cheques'

class chequedet_proxy(Cheqdet): #los proxys son para usuarios no administradores
    class Meta:
        proxy = True
        verbose_name = 'Detalles Proxy'
        verbose_name_plural = 'Proxy de Detalles'