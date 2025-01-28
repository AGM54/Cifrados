import random

def generar_llave(longitud):
    llave = ''.join(chr(random.randint(32, 126)) for _ in range(longitud))
    return llave

def texto_a_binario(texto):
    return ''.join(format(ord(caracter), '08b') for caracter in texto)


texto = input("Introduce el texto para generar una llave dinámica: ")

# Genera una llave de la misma longitud que el texto
llave = generar_llave(len(texto))

# Convierte el texto y la llave a binario
texto_binario = texto_a_binario(texto)
llave_binaria = texto_a_binario(llave)

print("\nTexto Original (ASCII):", texto)
print("Texto en Binario:", texto_binario)
print("\nLlave Generada (ASCII):", llave)
print("Llave en Binario:", llave_binaria)
