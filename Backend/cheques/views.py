import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.formats import date_format

from .models import Cheques, Cheqdet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .Funciones.Optimizaciones import optimizaciones

from django.db import connection

clean_orm = optimizaciones()

# Create your views here.

@login_required
def chequesIndexView(request):
    if request.method == 'GET':
        try:
            cheques = clean_orm.get_cheques_loading()
            request.session.pop('fecha_inicio_dia', None)  # Eliminar la session de la fecha
            #print(request.session.get('fecha_inicio_dia'))
            return render(request, "ChequesIndex.html", {
                'cheques': cheques
            })  # Renderiza el template index.html
        except Exception as e:
            if  '42S22' in str(e):
                return  redirect('ActualizarBD') # Redirigir a la vista de actualizar la base de datos
            else:
                return render(request, "ChequesIndex.html", {"error": f'Error: {e} - No se pueden mostrar los cheques'})
    else:
        # Se realizo una petición POST

        # Buscar por fechas
        # Primero se puede buscar por fecha 'desde'
        fecha_incio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        # Validar que fecha inicio si tiene un dato y fecha fin no
        if fecha_incio and not fecha_fin:
            try:
                fecha_incio = datetime.datetime.strptime(fecha_incio, '%Y-%m-%d')
                cheques = clean_orm.get_cheques_detalles_fecha_inicio(fecha_incio)
                # Guardar le fecha en una session
                request.session['fecha_inicio_dia'] = fecha_incio.strftime('%Y-%m-%d')
                #print(request.session.get('fecha_inicio_dia'))
                return render(request, "ChequesIndex.html", {
                    'cheques': cheques,
                    'correcto': f'Devolviendo datos de la fecha: {fecha_incio}'
                })  # Renderiza el template index.html
            except Exception as e:
                return render(request, "ChequesIndex.html", {"error": f'Error: {e} - No se pueden mostrar los cheques con la fecha solicitada'})
        # Validar que la fecha fin sea mayor a la fecha inicio
        elif fecha_fin < fecha_incio:
            return render(request, "ChequesIndex.html", {"error": 'La solicitud de fecha es incorrecta'})
        elif fecha_incio and fecha_fin:
            try:
                fecha_incio = datetime.datetime.strptime(fecha_incio, '%Y-%m-%d')
                fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
                cheques = clean_orm.get_cheques_fechas(fecha_incio, fecha_fin)

                return render(request, "ChequesIndex.html", {
                    'cheques': cheques,
                    'correcto': f'Devolviendo datos de la fecha: {fecha_incio} al {fecha_fin}'
                })  # Renderiza el template index.html
            except Exception as e:
                return render(request, "ChequesIndex.html", {"error": f'Error: {e} - No se pueden mostrar los cheques con la fecha solicitada'})
        else:
            return render(request, "ChequesIndex.html", {"error": 'No se ha ingresado una fecha para buscar'})
@login_required
def chequesDetallesView(request):
    datos = Cheqdet.objects.all()
    return render(request, "ChequesDetalles.html", {
        'cheques_detalles': datos
    })  # Renderiza el template index.html

def loginView(request):
    if request.method == 'GET':
        return render(request, "Login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Saber si el usuario tiene una suscripcion activa o no
            # Si el usuario esta en el grupo "sin_pagar" entonces redirigir a la vista de pago requerido
            if user.groups.filter(name='sin_pagar').exists():
                return redirect('PagoRequeridoView')
            else:
                return redirect('ChequesIndex')
        else:
            return render(request, "Login.html", {"error": "Usuario o contraseña incorrectos"})

@login_required
def logoutView(request):
    logout(request)
    return redirect('LoginView')

@login_required
def pagoRequeridoView(request):
    return render(request, "PagoRequerido.html")

@login_required
def desbloquearCheque(request, folio):
    cheque = Cheques.objects.get(folio=folio)
    cheque.estado = False
    cheque.save()
    return redirect('ChequesIndex') # Redirige a la vista de cheques

@login_required
def bloquearCheque(request, folio):
    cheque = Cheques.objects.get(folio=folio)
    cheque.estado = True
    cheque.save()
    return redirect('ChequesIndex') # Redirige a la vista de cheques

@login_required
def eliminarCheque(request, folio):
    cheque = Cheques.objects.get(folio=folio)
    cheque.delete()
    # Eliminar los detalles del cheque
    detalles = Cheqdet.objects.filter(id=folio)
    for detalle in detalles:
        detalle.delete()
    # Redirigir a la vista de cheques con un mensaje de confirmación
    fecha_inicio = request.session.get('fecha_inicio_dia')
    fecha_incio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
    return render(request, "ChequesIndex.html", {"correcto": "Cheque eliminado correctamente", "cheques": clean_orm.get_cheques_detalles_fecha_inicio(fecha_incio)})

@login_required
def actualizar_tabla(request):
    # Actualizar el diseño de las tablas de la base de datos
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE cheqdet ADD id BIGINT IDENTITY(1,1);")
        cursor.execute("ALTER TABLE cheqdet ADD CONSTRAINT PK_cheqdet_id PRIMARY KEY (id);")
        cursor.execute("ALTER TABLE cheques ADD estado BIT DEFAULT 0;")
        cursor.execute("UPDATE cheques SET estado = 0;")

    return HttpResponse("Tablas actualizadas correctamente, puedes regresar al incio") # Redirigir a la vista de cheques con un mensaje de confirmación