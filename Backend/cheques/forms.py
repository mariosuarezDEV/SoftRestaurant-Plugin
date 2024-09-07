from django.forms import ModelForm

from django import forms

# Integracion de modelos de la base de datos
from .models import Cheques

class ChequesForm(ModelForm):
    class Meta:
        model = Cheques
        fields = ['totalarticulos', 'total', 'subtotal', 'totalimpuesto1', 'efectivo', 'tarjeta', 'vales', 'otros', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }