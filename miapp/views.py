from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def hello(request):
    return HttpResponse("Hello World")


def adios(request):
    return HttpResponse("Adios")

def devuelve_fecha(request):
    fecha_actual = date.today()
    mensaje = f"Hoy es {fecha_actual}"
    return render(request, "base.html", {"mensaje": mensaje})

