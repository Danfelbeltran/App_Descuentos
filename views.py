from django.shortcuts import render
from django.http import JsonResponse
from .Mi_descuento import calcular_descuento
 

def calcular_descuento(request):
    if request.method == 'GET':
        return render(request, 'app_descuento/calculadora_descuento.html')
    elif request.method == 'POST':
        valor_producto = float(request.POST.get('valor_producto', 0))
        porcentaje_descuento = float(request.POST.get('porcentaje_descuento', 0))

        resultado = calcular_descuento(valor_producto, porcentaje_descuento)
        if "error" in resultado:
            return JsonResponse({"error": resultado['error']})
        else:
            return JsonResponse({"valor_final": resultado['valor_final'], "ahorro": resultado['ahorro']})
        
from django.shortcuts import render

def homepage(request):
    return render(request, 'app_descuento/homepage.html')

