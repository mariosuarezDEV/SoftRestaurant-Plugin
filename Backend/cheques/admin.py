from django.contrib import admin

# Register your models here.

# Modelos de la app de cheques
from .models import cheque_venta, detalle_cheque, estados_cheque

admin.site.register(cheque_venta)
admin.site.register(detalle_cheque)
admin.site.register(estados_cheque)
