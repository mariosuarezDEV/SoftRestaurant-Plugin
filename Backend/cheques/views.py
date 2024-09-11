import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.formats import date_format

from .models import Cheques, Cheqdet, Productos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import connection

@login_required
def actualizar_tabla(request):
    # Actualizar el diseño de las tablas de la base de datos
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE cheqdet ADD id BIGINT IDENTITY(1,1);")
        cursor.execute("ALTER TABLE cheqdet ADD CONSTRAINT PK_cheqdet_id PRIMARY KEY (id);")
        cursor.execute("ALTER TABLE Productosdetalle ADD id BIGINT IDENTITY(1,1);")
        cursor.execute("ALTER TABLE Productosdetalle ADD CONSTRAINT PK_Productosdetalle_id PRIMARY KEY (id);")
        cursor.execute("ALTER TABLE cheques ADD estado BIT DEFAULT 0;")
        cursor.execute("UPDATE cheques SET estado = 0;")

    return HttpResponse("Tablas actualizadas correctamente, puedes regresar al incio")

