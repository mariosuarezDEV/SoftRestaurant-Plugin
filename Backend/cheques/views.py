import datetime

from django.shortcuts import render

from .models import cheque_venta, detalle_cheque

# Create your views here.

def chequesIndexView(request):
    cheques = cheque_venta.objects.all()
    if request.method == 'GET':
        return render(request, "ChequesIndex.html",{
            'cheques': cheques
        }) # Renderiza el template index.html
    else:
        fecha_inicio = request.POST.get('fecha-inicio')
        fecha_fin = request.POST.get('fecha-fin')

        if fecha_inicio == "" or fecha_fin == "": # las fechas no pueden estar vacias
            return render(request, "ChequesIndex.html", {"error": "Debes ingresar ambas fechas", 'cheques': cheques})
        elif fecha_inicio > fecha_fin:
            return render(request, "ChequesIndex.html", {"error": "La forma en la que quieres filtrar los cheques es incorrecta", 'cheques': cheques})
        else:
            cheques = cheque_venta.objects.filter(fecha_movimiento__range=[fecha_inicio, fecha_fin])
            return render(request, "ChequesIndex.html",{
                'cheques': cheques
            })

def chequesDetallesView(request):
    datos = detalle_cheque.objects.all()
    
    if request.method == 'GET':
        return render(request, "ChequesDetalles.html",{
            'cheques_detalles': datos
            }) # Renderiza el template index.html
    else:
        fecha_inicio = request.POST.get('fecha-inicio')
        fecha_fin = request.POST.get('fecha-fin')

        if fecha_inicio == "" or fecha_fin == "": # las fechas no pueden estar vacias
            return render(request, "ChequesDetalles.html", {"error": "Debes ingresar ambas fechas", 'cheques_detalles': datos})
        elif fecha_inicio > fecha_fin:
            return render(request, "ChequesDetalles.html", {"error": "La forma en la que quieres filtrar los cheques es incorrecta", 'cheques_detalles': datos})

