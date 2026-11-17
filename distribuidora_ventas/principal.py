from paquete_ventas.operaciones import(
    cargar_ventas, mostrar_ventas, regiones_menos_de_porcentaje,
    regiones_mas_de_cantidad, regiones_por_encima_promedio,
    regiones_mas_compradoras,ordenar_regiones_alfabeticamente,
    hardcodear_datos
)
from paquete_ventas.validaciones import validar_es_entero, convertir_a_entero

def main():
    regiones = ["NOA", "NEA", "Pampeana", "Cuyo", "Patagonia", "GBA"]
    ventas =  []
    datos_cargados = False

    while True:
        print("\n ===================================================")
        print("          SISTEMA DE GESTION DE VENTAS        ")
        print("=====================================================")
        print("1. Cargar Ventas")
        print("2. Mostrar Ventas")
        print("3. Regiones con menos del 5 porciento de ventas")
        print("4. Regiones con menos del 25 porciento de ventas")
        print("5. Regiones con más de 500 ventas")
        print("6. Regiones con más de 3000 ventas")
        print("7. Regiones por encima del promedio")
        print("8. Regiones más compradoras")
        print("9. Hardcodear vector")
        print("10. Ordenar regiones por nombre")
        print("11. Salir")

        opcion_str = input("Seleccione una opcion: ")

        if not validar_es_entero(opcion_str):
            print("Error: Opcion invalida")
            continue

        opcion = convertir_a_entero(opcion_str)

        if opcion == 1:
            ventas = cargar_ventas(regiones)
            datos_cargados = True
        elif opcion == 9:
            regiones, ventas = hardcodear_datos()
            datos_cargados = True
        elif opcion == 10:
            lista_nombres_default = ["NOA", "NEA", "Pampeana", "Cuyo", "Patagonia", "GBA"]
            ordenar_regiones_alfabeticamente(lista_nombres_default)
        elif 2 <= opcion <= 8:
            if not datos_cargados:
                print("\n [ACCESO DENEGADO] Debe cargar las ventas (Opcion 1)")
            else:
                if opcion == 2:
                    mostrar_ventas(regiones,ventas)
                elif opcion == 3:
                    regiones_menos_de_porcentaje(regiones, ventas, 5)
                elif opcion == 4:
                    regiones_menos_de_porcentaje(regiones,ventas, 25)
                elif opcion == 5:
                    regiones_mas_de_cantidad(regiones,ventas,500)
                elif opcion == 6:
                    regiones_mas_de_cantidad(regiones,ventas,3000)
                elif opcion == 7:
                    regiones_por_encima_promedio(regiones,ventas)
                elif opcion == 8:
                    regiones_mas_compradoras(regiones,ventas)
        elif opcion == 11:
            print("Saliendo del sistema")
            break
        else:
            print("Error: Opcion fuerda de rango")
