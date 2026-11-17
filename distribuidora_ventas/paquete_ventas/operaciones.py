from .validaciones import validar_entero_positivo, comparar_cadenas, mi_max, mi_sum
def cargar_ventas(regiones):
    ventas = []
    print("\n--- CARGA DE VENTAS POR REGIÓN ---")
    for region in regiones:
        mensaje = f"Ingrese la cantidad de ventas para la región {region}: "
        cantidad = validar_entero_positivo(mensaje)
        ventas.append(cantidad)
    print("¡Ventas cargadas exitosamente!")
    return ventas

def mostrar_ventas(regiones, ventas):
    print("\n--- LISTADO DE VENTAS POR REGIÓN ---")
    total_ventas = mi_sum(ventas)
    for i in range(len(regiones)):
        porcentaje = (ventas[i] / total_ventas) * 100 if total_ventas > 0 else 0
        print(f"[{i+1}] Región: {regiones[i]} | Ventas: {ventas[i]} | Porcentaje: {porcentaje:.2f}%")
    print(f"\nCantidad total de productos vendidos: {total_ventas}")

def regiones_menos_de_porcentaje(regiones, ventas, porcentaje_limite):
    total_ventas = mi_sum(ventas)
    encontrados = False
    acumulado_ventas = 0
    
    print(f"\n--- REGIONES CON MENOS DEL {porcentaje_limite}% DE VENTAS ---")
    for i in range(len(regiones)):
        porcentaje = (ventas[i] / total_ventas) * 100 if total_ventas > 0 else 0
        if porcentaje < porcentaje_limite:
            print(f"Región: {regiones[i]} | Ventas: {ventas[i]} | Porcentaje: {porcentaje:.2f}%")
            acumulado_ventas += ventas[i]
            encontrados = True
            
    if not encontrados:
        print(f"Error: No hay ninguna región con menos del {porcentaje_limite}% de ventas.")
    else:
        porcentaje_acumulado = (acumulado_ventas / total_ventas) * 100 if total_ventas > 0 else 0
        print(f"\nPorcentaje de ventas acumuladas de los resultados: {porcentaje_acumulado:.2f}%")

def regiones_mas_de_cantidad(regiones, ventas, cantidad_limite):
    encontrados = False
    suma_resultados = 0
    cantidad_regiones = 0
    
    print(f"\n--- REGIONES CON MÁS DE {cantidad_limite} VENTAS ---")
    for i in range(len(regiones)):
        if ventas[i] > cantidad_limite:
            print(f"Región: {regiones[i]} | Ventas: {ventas[i]}")
            suma_resultados += ventas[i]
            cantidad_regiones += 1
            encontrados = True
            
    if not encontrados:
        print(f"Error: No hay ninguna región con más de {cantidad_limite} ventas.")
    else:
        promedio = suma_resultados / cantidad_regiones if cantidad_regiones > 0 else 0
        print(f"\n1. Suma de ventas de los resultados: {suma_resultados}")
        print(f"2. Cantidad de regiones encontradas: {cantidad_regiones}")
        print(f"3. Promedio de ventas de los resultados: {promedio:.2f}")

def regiones_por_encima_promedio(regiones, ventas):
    total_ventas = mi_sum(ventas)
    cantidad_regiones = len(ventas)
    promedio_general = total_ventas / cantidad_regiones if cantidad_regiones > 0 else 0
    
    encontrados = False
    acumulado_resultados = 0
    
    print(f"\n--- REGIONES POR ENCIMA DEL PROMEDIO GENERAL ({promedio_general:.2f}) ---")
    for i in range(len(ventas)):
        if ventas[i] > promedio_general:
            porcentaje = (ventas[i] / total_ventas) * 100 if total_ventas > 0 else 0
            print(f"Región: {regiones[i]} | Ventas: {ventas[i]} | Porcentaje: {porcentaje:.2f}%")
            acumulado_resultados += ventas[i]
            encontrados = True
            
    if not encontrados:
        print("Error: No hay regiones por encima del promedio general.")
    else:
        porcentaje_acumulado = (acumulado_resultados / total_ventas) * 100 if total_ventas > 0 else 0
        print(f"\n1. Promedio general de todas las ventas: {promedio_general:.2f}")
        print(f"2. Porcentaje acumulado de las ventas de los resultados: {porcentaje_acumulado:.2f}%")

def regiones_mas_compradoras(regiones, ventas):
    max_ventas = mi_max(ventas)
    total_ventas = mi_sum(ventas)
    
    print(f"\n--- REGIÓN/ES MÁS COMPRADORA/S ---")
    for i in range(len(ventas)):
        if ventas[i] == max_ventas:
            porcentaje = (ventas[i] / total_ventas) * 100 if total_ventas > 0 else 0
            print(f"Región: {regiones[i]} | Cantidad de ventas: {ventas[i]} | Porcentaje: {porcentaje:.2f}%")

def hardcodear_datos():
    nuevas_regiones = ["PBA", "CABA", "La Pampa", "Tucumán", "Mendoza", "Chubut", "Corrientes", "Neuquén", "La Rioja", "Jujuy"]
    nuevas_ventas = [1800, 555, 2333, 1850, 3999, 777, 1410, 7180, 2500, 60]
    print("\n¡Datos hardcodeados cargados con éxito! (10 regiones y sus respectivas ventas).")
    return nuevas_regiones, nuevas_ventas

def ordenar_regiones_alfabeticamente(lista_nombres):
    nombres = []
    for i in range(len(lista_nombres)):
        nombres.append(lista_nombres[i])
        
    n = len(nombres)
    
    for i in range(n - 1):
         for j in range(n - 1 - i):
            if comparar_cadenas(nombres[j], nombres[j + 1]) > 0:
                aux = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux
                
    print("\n--- REGIONES ORDENADAS ALFABÉTICAMENTE (A-Z) ---")
    for nombre in nombres:
        print(f"- {nombre}")