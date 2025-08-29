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
print(clasificar_edad(-1))

# (match/case) Crea 'tipo_dia(dia)' que reciba el nombre del día y devuelva 'laboral' o 'fin 
# de semana'.

def tipo_dia(dia: str) -> str:
    match dia:
        case 'Lunes' | 'Martes' | 'Miércoles' | 'Jueves' | 'Viernes':
            return "Laboral"
        case 'Sábado' | 'Domingo':
            return "Fin de semana"
print(tipo_dia("Lunes"))
  
# (for + range) Suma los múltiplos de 3 o 5 menores que N (clásico problema). Implementa 
# versión con for y otra con comprensión de listas. 

# (while + else) Cuenta regresiva desde N hasta 0. Si se usa 'break' para salir, no debe 
# ejecutarse el 'else'; si termina 'naturalmente', sí. 

# (Listas I) Dada 'ventas = [13, 5, 21, 5, 8]': agrega 34 al final, inserta 99 en índice 1, 
# elimina la primera ocurrencia de 5, invierte la lista y ordénala descendente. 

# (Listas II) Implementa 'indice_primera_aparicion(lst, valor)' sin usar 'list.index'. 
# Devuelve -1 si no existe. 

# (zip) Dadas 'alumnos = ["Ana", "Luis", "Marta"]' y 'notas = [5.5, 6.0]': combínalas con 
# 'zip' y calcula el promedio de las notas presentes. 

# (enumerate) Recorre 'tareas = ["cargar datos", "limpiar", "entrenar", "evaluar"]' y 
# muestra '1) cargar datos', etc. usando 'enumerate' empezando en 1. 

# (List comprehension I) Genera los cuadrados de 1..N sólo para pares. 
 
# (List comprehension II) Aplana 'mat = [[1,2,3],[4,5],[6]]' en una sola lista '[1,2,3,4,5,6]'  
