from django.urls import path, include

from rest_framework import routers # Utilizado para crear las rutas de la API

from .views import ChequeViewSet, ChequeDetalleViewSet # Vistas para el frontend (estas vistas son el sistema)

roter = routers.DefaultRouter() # Crear un router para la API

from . import views
urlpatterns = [
    path("", views.chequesIndexView, name='ChequesIndex'), # Agregar la url de la app cheques
    path("detalles/", views.chequesDetallesView, name='ChequesDetalles') # Agregar la url de la app cheques
]