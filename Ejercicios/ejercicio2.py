
import base64

def base64_a_binario(texto_base64):
    # Decodifica el texto Base64 a bytes
    bytes_decodificados = base64.b64decode(texto_base64)
    # Convierte cada byte a binario de 8 bits
    resultado_binario = [format(byte, '08b') for byte in bytes_decodificados]
    return ' '.join(resultado_binario)

# Entrada del usuario
texto_base64 = input("Introduce el texto en Base64 que deseas convertir a binario: ")
binario = base64_a_binario(texto_base64)

print("\nTexto en Binario:")
print(binario)









#conversación: https://chatgpt.com/c/67982bca-d0b0-8009-85c9-682c76e7e2a1
