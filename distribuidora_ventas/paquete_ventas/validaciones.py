def mi_sum(vector):
    total = 0
    for x in vector:
        total += x
    return total

def mi_max(vector):
    if not vector:
        return None
    max_val = vector[0]
    for x in vector:
        if x > max_val:
            max_val = x
    return max_val

def mi_min(vector):
    if not vector:
        return None
    min_val = vector[0]
    for x in vector:
        if x < min_val:
            min_val = x
    return min_val

def validar_es_entero(cadena):
    digitos_validos ="0123456789"
    if len(cadena) == 0:
        return False
    for i in range(len(cadena)):
        caracter = cadena[i]
        encontrado = False

        for j in range(len(digitos_validos)):
            if caracter == digitos_validos[j]:
                encontrado = True
                break
        if not encontrado:
            return False
    return True

def convertir_a_entero(cadena):
    digitos_validos ="0123456789"
    valor = 0
    for i in range(len(cadena)):
        caracter = cadena[i]
        digito = 0

        for j in range(len(digitos_validos)):
            if caracter == digitos_validos[j]:
                digito = j
                break
        valor = valor * 10 + digito
    return valor

def validar_entero_positivo(mensaje):
    while True:
        cadena = input(mensaje)
        if validar_es_entero(cadena):
            valor = convertir_a_entero(cadena)
            if valor > 0:
                return valor
            else:
                print("Error: El numero debe ser mayor a cero.")
        else:
            print("Error: Dato invalido (\"abc\" o similar detectado).")

def a_minuscula(caracter):
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minisculas = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(mayusculas)):
        if caracter == mayusculas[i]:
            return minisculas[i]
    return caracter

def comparar_cadenas(cad1, cad2):
    i = 0
    l1 = len(cad1)
    l2 = len(cad2)

    while i < l1 and i < l2:
        c1 = a_minuscula(cad1[i])
        c2 = a_minuscula(cad2[i])

        if c1 < c2:
            return -1
        elif c1 > c2:
            return 1
        i += 1
    if l1 < l2:
        return -1
    elif l1 > l2:
        return 1
    return 0