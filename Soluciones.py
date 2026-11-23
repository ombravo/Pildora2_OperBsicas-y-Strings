# --- SOLUCIÓN EJERCICIO 1 ---
total_cajas = 145
capacidad_camion = 12
camiones_llenos = total_cajas // capacidad_camion
cajas_sobrantes = total_cajas % capacidad_camion
porcentaje_ultimo = (cajas_sobrantes / capacidad_camion) * 100
combinaciones = 2 ** cajas_sobrantes
print(f"Camiones: {camiones_llenos}, Sobran: {cajas_sobrantes}, Ocupación último: {porcentaje_ultimo:.2f}%, Combinaciones: {combinaciones}")

# --- SOLUCIÓN EJERCICIO 2 ---
edad, ingresos_mensuales, tiene_deudas = 28, 1850, False
print(edad >= 18 and ingresos_mensuales > 1500)
print(not tiene_deudas and edad != 65)


# --- SOLUCIÓN EJERCICIO 3 ---
registro = "   usuario:ana_gomez | puntos:450 | ciudad:Madrid   "
limpio = registro.strip().replace("Madrid", "Barcelona")
datos = limpio.split(" | ")
print(datos)

# --- SOLUCIÓN EJERCICIO 4 ---
codigo_producto = "PROD-9876-ES"
precio, unidades = 49, 3
num_serie = codigo_producto[5:9]
pais = codigo_producto[-2:]
num_serie_inv = num_serie[::-1]
total = precio * unidades
print("Producto " + num_serie + " (" + pais + "): total " + str(total) + " euros")
print(f"Producto {num_serie} ({pais}): total {total} euros (Serie invertida: {num_serie_inv})")

