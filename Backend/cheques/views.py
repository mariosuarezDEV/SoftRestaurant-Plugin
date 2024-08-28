import datetime

from django.shortcuts import render, redirect

from .models import Cheques, Cheqdet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required
def chequesIndexView(request):
    cheques = Cheques.objects.all()

    if request.method == 'GET':
        return render(request, "ChequesIndex.html",{
            'cheques': cheques
        }) # Renderiza el template index.html
    else:
        fecha_inicio = request.POST.get('fecha-inicio')
        fecha_fin = request.POST.get('fecha-fin')

        if fecha_fin == "": # Obtener solo los cheques de la fecha de inicio
            # formatear la fecha de inicio
            fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            cheques = Cheques.objects.filter(fecha=fecha_inicio)

            return render(request, "ChequesIndex.html", {
                'cheques': cheques
            })
        elif fecha_inicio == "" or fecha_fin == "": # las fechas no pueden estar vacias
            return render(request, "ChequesIndex.html", {"error": "Debes ingresar ambas fechas", 'cheques': cheques})
        elif fecha_inicio > fecha_fin:
            return render(request, "ChequesIndex.html", {"error": "La forma en la que quieres filtrar los cheques es incorrecta", 'cheques': cheques})
        else:
            cheques = Cheques.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
            return render(request, "ChequesIndex.html",{
                'cheques': cheques
            })

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
    cheque.bloqueado = False
    cheque.save()
    return redirect('ChequesIndex') # Redirige a la vista de cheques

@login_required
def bloquearCheque(request, folio):
    cheque = Cheques.objects.get(folio=folio)
    cheque.bloqueado = True
    cheque.save()
    return redirect('ChequesIndex') # Redirige a la vista de cheques

@login_required
def eliminarCheque(request, folio):
    cheque = Cheques.objects.get(folio=folio)
    cheque.delete()
    # Eliminar los detalles del cheque
    detalles = Cheqdet.objects.filter(folio_det=folio)
    for detalle in detalles:
        detalle.delete()
    return redirect('ChequesIndex') # Redirige a la vista de cheques