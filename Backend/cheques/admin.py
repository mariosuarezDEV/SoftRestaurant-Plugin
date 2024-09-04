from django.contrib import admin
from django.db import models

# Register your models here.

# Modelos de la app de cheques
from .models import Cheques, Cheqdet, Productos, Productosdetalle

class TotalImpuesto1Filter(admin.SimpleListFilter):
    title = 'Impuesto'
    parameter_name = 'totalimpuesto1'

    def lookups(self, request, model_admin):
        return (
            ('0', 'Tasa 0'),
            ('not_0', 'Tasa 16 efectivo'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(totalimpuesto1=0)
        elif self.value() == 'not_0':
            return queryset.exclude(totalimpuesto1=0).filter(efectivo__gt=0, tarjeta=0)
        return queryset

@admin.register(Cheques)
class ChequesAdmin(admin.ModelAdmin):
    list_filter = (TotalImpuesto1Filter, "fecha", )
    date_hierarchy = "fecha"
    search_fields = ("totalimpuesto1", "numcheque")
    list_display=("numcheque", "totalimpuesto1", "total", "efectivo", "tarjeta", "folio")

admin.site.register(Cheqdet)
admin.site.register(Productos)
admin.site.register(Productosdetalle)