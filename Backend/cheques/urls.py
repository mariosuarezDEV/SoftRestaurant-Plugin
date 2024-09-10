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
    path('api/', include(router.urls), name="ChequesAPI"), # Acceso a la API
    path('actualizar_tabla/', views.actualizar_tabla, name="ActualizarTabla"), # Actualizar la tabla de la base de datos
]