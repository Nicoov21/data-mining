# (Binario→Decimal) Implementa 'bin_to_dec(s: str) -> int' que recibe una cadena binaria
# (p. ej. '101101') y retorna su valor decimal.

def bin_to_dec(s: str) -> int:
    valorDecimal = 0
    longitudBinario = len(s)
    for numBin in range(longitudBinario): #! Itera por la longitud del binario
        bit = int(s[longitudBinario - 1 - numBin]) #! Parsea el bit a número
        valorDecimal += bit * (2**numBin) #? Suma el valor del bit elevandolo por su posición
    return valorDecimal

print(bin_to_dec('100'))
