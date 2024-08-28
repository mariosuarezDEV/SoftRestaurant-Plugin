from rest_framework import serializers # Importar el serializador de la API

from .models import Cheques, Cheqdet # Importar los modelos de la app cheques

# Serializador para el modelo cheque_venta
class ChequeVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheques # Modelo a serializar
        fields = '__all__' # Campos a serial

# Serializador para el modelo detalle_cheque
class ChequeDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheqdet # Modelo a serializar
        fields = '__all__' # Campos a serial
        
