# (Binario→Decimal) Implementa 'bin_to_dec(s: str) -> int' que recibe una cadena binaria
# (p. ej. '101101') y retorna su valor decimal.
def bin_to_dec(s: str) -> int:
    valorDecimal = 0
    longitudBinario = len(s)
    for numBin in range(longitudBinario): #! Itera por la longitud del binario
        bit = int(s[longitudBinario - 1 - numBin]) #! Parsea el bit a número
        valorDecimal += bit * (2**numBin) #? Suma el valor del bit elevandolo por su posición
    return valorDecimal
#print(bin_to_dec('100001'))

# (Decimal→Binario) Implementa una solución que devuelve la representación binaria de 
# un número decimal entero cualquiera. Prueba con 0, 1, 2, 7, 8, 255. 
def dec_to_bin(s: int) -> str:
    if s == 0: #! Si el número es 0, retorna un mensaje advirtiendo que no debe ser 0
        return ("El decimal no puede ser 0")
    numeroBinario = '' #! Se inicializa la variable que contendrá la transformación del número decimal a binario
    while s > 0: #! Se crea un bucle que se repite hasta que el número decimal sea 0
        residuoDecimal = s % 2 #? Obtiene el restante de dividir el decimal por 2
        numeroBinario = str(residuoDecimal) + numeroBinario #? Se concatena el restante al inicio del string
        s = s // 2 #? Se actualiza el valor del decimal por su divisíon entera por 2
    return numeroBinario #! Retorna el número en binario
#print(dec_to_bin(254))

# (Floats y precisión) Demuestra con un script que '0.1 + 0.2 != 0.3'. Luego verifica 
# correctamente con 'math.isclose'. Explica en comentarios por qué ocurre. 
#import math
a = 0.1
b = 0.2
c = 0.3
suma = a + b
# print(suma == c)
# print(math.isclose(suma, c))

# (Strings I) Dado 'texto = "  ¡Hola,  mundo          !  "' elimina espacios duplicados, quita 
# signos de puntuación, y genera un 'slug' en minúsculas separado con '-'.
texto = "  ¡Hola,  mundo          !  "
texto = texto.replace(" ","").replace("!","").replace("¡","") #? Elimina espacios y signos de puntuación
texto = texto.lower() #? Lo pasa a minúsculas
slug = texto.replace(",","-") #? Reemplaza las comas por guiones
#print(slug)

# (Strings II) Cuenta vocales en 'áéíóúÁÉÍÓÚaeiou' dentro de un texto Unicode. Devuelve 
# una dupla de frecuencias. 
texto_unicode = "Esto es una simulación de un texto con acentos"
vocales = "áéíóúÁÉÍÓÚaeiou"
contadorVocales = 0 #? Contador de vocales
for letra in texto_unicode: #? Itera por cada letra del texto ingresado
    if letra in vocales: #? Verifica si esa letra es una vocal
            contadorVocales += 1 #? Si es volcal, la suma al contador
#print(contadorVocales)
