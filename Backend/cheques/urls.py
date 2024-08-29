from tkinter.font import names

from django.urls import path, include

from rest_framework import routers # Utilizado para crear las rutas de la API

from .endpoints import ChequeDetalleViewSet, ChequeViewSet, ProductosViewSet # Vistas para el frontend (estas vistas son el sistema)

from . import views # Importar las vistas de la app cheques (sistema)

router = routers.DefaultRouter() # Crear un router para la API

router.register("cheque", ChequeViewSet) # Registrar el modelo cheque_venta en el router
router.register("chequedet", ChequeDetalleViewSet) # Registrar el modelo detalle_cheque en el router
router.register("productos", ProductosViewSet) # Registrar el modelo productos

urlpatterns = [
    path("", views.chequesIndexView, name='ChequesIndex'), # Agregar la url de la app cheques
    path("login/", views.loginView, name="LoginView"), # Vista para iniciar sesion
    path("cheques/login/", views.logoutView, name="LogoutView"), # Vista para iniciar sesion
    path("suscripcion/", views.pagoRequeridoView, name="PagoRequeridoView"), # Vista para recordarle al cliente que su suscripcion esta vencida
    path("detalles/", views.chequesDetallesView, name='ChequesDetalles'), # Vista para ver los detalles de un cheque
    path("desbloquear/<int:folio>/", views.desbloquearCheque, name='DesbloquearCheque'), # Desbloquear un cheque
    path("bloquear/<int:folio>/", views.bloquearCheque, name='BloquearCheque'), # Bloquear un cheque
    path("eliminar/<int:folio>/", views.eliminarCheque, name='EliminarCheque'), # Eliminar un cheque
    path("peticiones/", views.accion_formulario, name='Accion_Cheques'), # Eliminar varios cheques
    path("eliminar_grupo/", views.eliminar_varios_cheques, name='EliminarGrupoCheques'), # Eliminar varios cheques
    path("sustituir_primera_lista/", views.sustituir_produto_uno_efectivo, name='SustituirPrimeraLista'), # Sustituir la primera lista de productos
    path("configurar/", views.actualizar_tabla, name='ActualizarBD'), # Configuración del diseño de la base de datos
    path('api/', include(router.urls), name="ChequesAPI"), # Acceso a la API
]