import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.formats import date_format

from .models import Cheques, Cheqdet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .Funciones.Optimizaciones import optimizaciones

from django.db import connection

from django.core.paginator import Paginator

clean_orm = optimizaciones()

# Create your views here.

@login_required
def chequesIndexView(request):
    if request.method == 'GET':
        try:
            cheques = clean_orm.get_cheques_loading()
            request.session.pop('fecha_inicio', None)  # Eliminar la session de la fecha
            request.session.pop('fecha_fin', None)  # Eliminar la session de la fecha
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
                request.session['fecha_inicio'] = fecha_incio.strftime('%Y-%m-%d')

                # Configurar la paginación
                paginator = Paginator(cheques, 20)  # Mostrar 20 resultados por página
                page_number = request.GET.get('page')  # Obtener el número de la página actual de la URL
                page_obj = paginator.get_page(page_number)  # Obtener los resultados para la página actual

                return render(request, "ChequesIndex.html", {
                    'cheques': page_obj,
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
                request.session['fecha_inicio'] = fecha_incio.strftime('%Y-%m-%d')
                fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
                request.session['fecha_fin'] = fecha_fin.strftime('%Y-%m-%d')
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
    # Obtener todos los datos
    datos = Cheqdet.objects.all()

    # Configurar la paginación
    paginator = Paginator(datos, 20)  # Mostrar 20 resultados por página
    page_number = request.GET.get('page')  # Obtener el número de la página actual de la URL
    page_obj = paginator.get_page(page_number)  # Obtener los resultados para la página actual

    return render(request, "ChequesDetalles.html", {
        'page_obj': page_obj
    })

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
    try:
        cheque = Cheques.objects.get(folio=folio)
        cheque.delete()

        # Eliminar los detalles del cheque
        Cheqdet.objects.filter(foliodet=folio).delete()

        # Redirigir a la vista de cheques con un mensaje de confirmación
        fecha_inicio_str = request.session.get('fecha_inicio')
        fecha_fin_str = request.session.get('fecha_fin')

        # Asegúrate de que las fechas estén disponibles y conviértelas a objetos datetime
        if fecha_inicio_str and not fecha_fin_str:
            fecha_inicio = timezone.datetime.fromisoformat(fecha_inicio_str)
            cheques = clean_orm.get_cheques_detalles_fecha_inicio(fecha_inicio)
            return render(request, "ChequesIndex.html",
                          {"correcto": "Cheque eliminado correctamente", "cheques": cheques})

        elif fecha_inicio_str and fecha_fin_str:
            fecha_inicio = timezone.datetime.fromisoformat(fecha_inicio_str)
            fecha_fin = timezone.datetime.fromisoformat(fecha_fin_str)
            cheques = clean_orm.get_cheques_fechas(fecha_inicio, fecha_fin)
            return render(request, "ChequesIndex.html",
                          {"correcto": "Cheque eliminado correctamente", "cheques": cheques})
        else:
            fecha_inicio = None
            fecha_fin = None

    except Cheques.DoesNotExist:
        return render(request, "ChequesIndex.html", {"error": "Cheque no encontrado"})
    except Exception as e:
        return render(request, "ChequesIndex.html", {"error": str(e)})

@login_required
def actualizar_tabla(request):
    # Actualizar el diseño de las tablas de la base de datos
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE cheqdet ADD id BIGINT IDENTITY(1,1);")
        cursor.execute("ALTER TABLE cheqdet ADD CONSTRAINT PK_cheqdet_id PRIMARY KEY (id);")
        cursor.execute("ALTER TABLE cheques ADD estado BIT DEFAULT 0;")
        cursor.execute("UPDATE cheques SET estado = 0;")

    return HttpResponse("Tablas actualizadas correctamente, puedes regresar al incio") # Redirigir a la vista de cheques con un mensaje de confirmación