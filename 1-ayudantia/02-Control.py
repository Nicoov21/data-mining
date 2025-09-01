# (Condicionales) Escribe 'clasificar_edad(edad)' que retorne 'niñez', 'adolescencia', 
# 'adultez' o 'senior' según rangos. Maneja bordes (0, 12, 13, 17, 18, 64, 65…). 
def clasificar_edad(edad: int) -> str:
    if edad < 0 or edad > 110:
        return "Edad ingresada no válida"
    if 0 <= edad <= 12:
        return "Niñez"
    if 13 <= edad <= 17:
        return "Adolescencia"
    if 18 <= edad <= 60:
        return "Adultez"
    else:
        return "Senior"
#print(clasificar_edad(-1))

# (match/case) Crea 'tipo_dia(dia)' que reciba el nombre del día y devuelva 'laboral' o 'fin 
# de semana'.
def tipo_dia(dia: str):
    match dia: 
        case 'Lunes' | 'Martes' | 'Miércoles' | 'Jueves' | 'Viernes': #! Si es día de semana
            return "Laboral" #? Retorna Laboral
        case 'Sábado' | 'Domingo': 
            return "Fin de semana"
#print(tipo_dia("Lunes"))
  
# (for + range) Suma los múltiplos de 3 o 5 menores que N (clásico problema). Implementa 
# versión con for y otra con comprensión de listas. 
def suma_multiplos(num:int)->int:
    suma = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma
#print(suma_multiplos(10))

# (while + else) Cuenta regresiva desde N hasta 0. Si se usa 'break' para salir, no debe 
# ejecutarse el 'else'; si termina 'naturalmente', sí. 
def cuenta_regresiva(num:int):
    while num >= 0:
        print(num)
        if num == 5:
            print(f"Interrumpido en {num}")
            break
        num -= 1
    else:
        print("La cuenta regresiva ha finalizado naturalmente")
#cuenta_regresiva(7)
#cuenta_regresiva(4)


# (Listas I) Dada 'ventas = [13, 5, 21, 5, 8]': agrega 34 al final, inserta 99 en índice 1, 
# elimina la primera ocurrencia de 5, invierte la lista y ordénala descendente. 
ventas = [13, 5, 21, 5, 8]
ventas.append(34)
ventas[1] = 99
ventas.remove(5)
ventas.reverse()
ventas.sort(reverse=True)
#print(ventas)

# (Listas II) Implementa 'indice_primera_aparicion(lst, valor)' sin usar 'list.index'. 
# Devuelve -1 si no existe. 
def indice_primera_aparicion(lst, valor) -> int:
    return -1

# (zip) Dadas 'alumnos = ["Ana", "Luis", "Marta"]' y 'notas = [5.5, 6.0]': combínalas con 
# 'zip' y calcula el promedio de las notas presentes. 
alumnos = ["Ana", "Luis", "Marta"]
notas = [5.5, 6.0]
promedio = (sum(notas)/len(notas))
# for alumno, nota in zip(alumnos,notas):
#     print(f"El alumno {alumno} tiene una nota de {nota}")
#print(f"El promedio de las notas es {promedio}")

# (enumerate) Recorre 'tareas = ["cargar datos", "limpiar", "entrenar", "evaluar"]' y 
# muestra '1) cargar datos', etc. usando 'enumerate' empezando en 1. 
tareas = ["cargar datos", "limpiar", "entrenar", "evaluar"]

# for indice, tarea in enumerate(tareas):
#     print(f"{indice +1}) {tarea}")

# (List comprehension I) Genera los cuadrados de 1..N sólo para pares.
n = 10 
cuadradosPares = [i**2 for i in range(1,n+1) if i % 2 == 0]
#print(cuadradosPares)
 
# (List comprehension II) Aplana 'mat = [[1,2,3],[4,5],[6]]' en una sola lista '[1,2,3,4,5,6]'  
mat = [[1,2,3],[4,5],[6]]
matAplanada = [elemento for fila in mat for elemento in fila]
#print(matAplanada)