from django.urls import path, include

from rest_framework import routers # Utilizado para crear las rutas de la API

from .endpoints import ChequeDetalleViewSet, ChequeViewSet # Vistas para el frontend (estas vistas son el sistema)

from . import views # Importar las vistas de la app cheques (sistema)

router = routers.DefaultRouter() # Crear un router para la API

router.register("cheque", ChequeViewSet) # Registrar el modelo cheque_venta en el router
router.register("chequedet", ChequeDetalleViewSet) # Registrar el modelo detalle_cheque en el router

urlpatterns = [
    path("", views.chequesIndexView, name='ChequesIndex'), # Agregar la url de la app cheques
    path("detalles/", views.chequesDetallesView, name='ChequesDetalles'), # Agregar la url de la app cheques
    path('api/', include(router.urls)), # Agregar las urls del router
]