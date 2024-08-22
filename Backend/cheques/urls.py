from django.urls import path, include

from . import views
urlpatterns = [
    path("", views.chequesIndexView, name='ChequesIndex'), # Agregar la url de la app cheques
    path("detalles/", views.chequesDetallesView, name='ChequesDetalles') # Agregar la url de la app cheques
]