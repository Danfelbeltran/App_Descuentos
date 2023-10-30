def calcular_descuento(valor_producto, porcentaje_descuento):
    try:
        valor_producto = float(valor_producto)
        porcentaje_descuento = float(porcentaje_descuento)
        if valor_producto >= 0 and porcentaje_descuento >= 0:
            descuento = (valor_producto * porcentaje_descuento) / 100
            valor_final = valor_producto - descuento
            ahorro = descuento
            return {
                "valor_final": round(valor_final, 2),
                "ahorro": round(ahorro, 2)
            }
        else:
            return {"error": "Los valores deben ser no negativos."}
    except ValueError:
        return {"error": "Ingresa valores válidos."}

# Ejemplo de uso
valor_producto = input("Ingrese el valor del producto: ")
porcentaje_descuento = input("Ingrese el porcentaje de descuento: % ")

resultado = calcular_descuento(valor_producto, porcentaje_descuento)
if "error" in resultado:
    print(f"Error: {resultado['error']}")
else:
    print(f"Paga solo: {resultado['valor_final']}")
    print(f"Dinero Ahorrado: {resultado['ahorro']}")
