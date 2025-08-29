# (Binario→Decimal) Implementa 'bin_to_dec(s: str) -> int' que recibe una cadena binaria
# (p. ej. '101101') y retorna su valor decimal.

def bin_to_dec(s: str) -> int:
    valorDecimal = 0
    longitudBinario = len(s)
    for numBin in range(longitudBinario): #! Itera por la longitud del binario
        bit = int(s[longitudBinario - 1 - numBin]) #! Parsea el bit a número
        valorDecimal += bit * (2**numBin) #? Suma el valor del bit elevandolo por su posición
    return valorDecimal

def dec_to_bin(s: int) -> str:
    if s == 0: #! Si el número es 0, retorna un mensaje advirtiendo que no debe ser 0
        return ("El decimal no puede ser 0")
    numeroBinario = '' #! Se inicializa la variable que contendrá la transformación del número decimal a binario
    while s > 0: #! Se crea un bucle que se repite hasta que el número decimal sea 0
        residuoDecimal = s % 2 #? Obtiene el restante de dividir el decimal por 2
        numeroBinario = str(residuoDecimal) + numeroBinario #? Se concatena el restante al inicio del string
        s = s // 2 #? Se actualiza el valor del decimal por su divisíon entera por 2
    return numeroBinario #! Retorna el número en binario
