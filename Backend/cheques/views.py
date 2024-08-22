from django.shortcuts import render

# Create your views here.

def chequesIndexView(request):
    return render(request, "ChequesIndex.html") # Renderiza el template index.html

def chequesDetallesView(request):
    return render(request, "ChequesDetalles.html") # Renderiza el template index.html