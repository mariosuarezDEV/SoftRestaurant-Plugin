from django.contrib import admin

# Register your models here.

# Modelos de la app de cheques
from .models import Cheques, Cheqdet, Productos, Productosdetalle

@admin.register(Cheques)
class ChequesAdmin(admin.ModelAdmin):
    list_filter = ("totalimpuesto1",)
    search_fields = ("totalimpuesto1", "numcheque",)
    # Los filtros solo que sea la siguiente regla: totalimpuesto1 == 0 | totalimpuesto1 =! 0 && metodo de pago = efectivo


admin.site.register(Cheques)
admin.site.register(Cheqdet)
admin.site.register(Productos)
admin.site.register(Productosdetalle)