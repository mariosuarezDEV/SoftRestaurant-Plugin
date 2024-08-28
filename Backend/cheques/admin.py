from django.contrib import admin

# Register your models here.

# Modelos de la app de cheques
from .models import Cheques, Cheqdet

admin.site.register(Cheques)
admin.site.register(Cheqdet)
