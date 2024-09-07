from django.forms import ModelForm

from django import forms

# Integracion de modelos de la base de datos
from .models import Cheques, Cheqdet

class ChequesForm(ModelForm):
    class Meta:
        model = Cheques
        fields = ['totalarticulos', 'total', 'subtotal', 'totalimpuesto1', 'efectivo', 'tarjeta', 'vales', 'otros', 'fecha', 'cierre']

class ChequesdetForm(ModelForm):
    class Meta:
        model = Cheqdet
        fields = ['foliodet', 'movimiento', 'cantidad', 'idproducto', 'precio', 'impuesto1', 'preciosinimpuestos']