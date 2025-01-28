import random

def generar_llave(longitud):
    return ''.join(chr(random.randint(32, 126)) for _ in range(longitud))

def texto_a_binario(texto):
    return ''.join(format(ord(caracter), '08b') for caracter in texto)

def cifrar_texto(texto, llave):
    texto_cifrado = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(texto, llave))
    return texto_cifrado


tamano_llave = 8
texto = input("Introduce el texto para cifrar: ")
llave = generar_llave(tamano_llave)
llave_repetida = (llave * (len(texto) // len(llave) + 1))[:len(texto)]


texto_cifrado = cifrar_texto(texto, llave_repetida)

# Convierte texto y llave a binario
texto_binario = texto_a_binario(texto)
llave_binaria = texto_a_binario(llave_repetida)
texto_cifrado_binario = texto_a_binario(texto_cifrado)


print("\nTexto Original (ASCII):", texto)
print("Texto en Binario:", texto_binario)
print("\nLlave Generada (ASCII):", llave)
print("Llave en Binario:", llave_binaria)
print("\nTexto Cifrado (ASCII):", texto_cifrado)
print("Texto Cifrado en Binario:", texto_cifrado_binario)



#Conversación: https://chatgpt.com/share/67982de0-7740-8009-b080-8cbb67761a56