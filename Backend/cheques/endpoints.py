from .models import Cheques, Cheqdet, Productos # Modelos cargados en la base de datos

from .serializers import ChequeVentaSerializer, ChequeDetalleSerializer, ProductosSerializer # Estas clases controlan las serializaciones de los modelos

from rest_framework import viewsets # Importar el viewset de la API
from rest_framework import permissions # Importar los permisos de la API

# El view set es el controlador de la API que permite hacer operaciones CRUD

# Viewset para el modelo cheque_venta
class ChequeViewSet(viewsets.ModelViewSet):
    queryset = Cheques.objects.all() # Consultar todos los registros de cheque_venta
    serializer_class = ChequeVentaSerializer # Serializar los registros de cheque_venta
    permission_classes = [permissions.AllowAny] # Permisos para el endpoint
    
# Viewset para el modelo detalle_cheque
class ChequeDetalleViewSet(viewsets.ModelViewSet):
    queryset = Cheqdet.objects.all() # Consultar todos los registros de detalle_cheque
    serializer_class = ChequeDetalleSerializer # Serializar los registros de detalle_cheque
    permission_classes = [permissions.AllowAny] # Permisos para el endpoint

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [permissions.AllowAny]
