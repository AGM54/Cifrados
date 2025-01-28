import random

def generar_llave_dinamica(longitud):
    return ''.join(chr(random.randint(32, 126)) for _ in range(longitud))

def cifrar_texto_ascii(texto, llave):
    texto_cifrado = []
    
    for i in range(len(texto)):
        char_cifrado = chr(ord(texto[i]) ^ ord(llave[i]))
        texto_cifrado.append(char_cifrado)
    
    return ''.join(texto_cifrado)

def descifrar_texto_ascii(texto_cifrado, llave):
    return cifrar_texto_ascii(texto_cifrado, llave) 


texto_original = input("Introduce el texto a cifrar: ")
llave_dinamica = generar_llave_dinamica(len(texto_original))
texto_cifrado = cifrar_texto_ascii(texto_original, llave_dinamica)
texto_descifrado = descifrar_texto_ascii(texto_cifrado, llave_dinamica)


print("\nTexto Original (ASCII):", texto_original)
print("Llave Dinámica Generada (ASCII):", llave_dinamica)
print("Texto Cifrado (ASCII):", texto_cifrado)
print("Texto Descifrado (ASCII):", texto_descifrado)
