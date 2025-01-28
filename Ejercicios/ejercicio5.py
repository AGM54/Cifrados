import base64

def base64_a_binario(texto_base64):
    # Decodifica el texto Base64 a bytes
    bytes_decodificados = base64.b64decode(texto_base64)
    resultado_binario = []
    for byte in bytes_decodificados:
        binario = bin(byte)[2:]  # Convierte a binario y elimina el prefijo '0b'
        # Asegura que cada byte tenga 8 bits
        binario = binario.zfill(8)
        resultado_binario.append(binario)
    
    return ' '.join(resultado_binario)  # Retorna los bytes separados por espacios

def binario_a_ascii(binario):
    caracteres_ascii = []
    # Divide el binario en grupos de 8 bits basados en los espacios
    bytes_binarios = binario.split(" ")
    for byte in bytes_binarios:
        # Convierte cada grupo de 8 bits en un carácter ASCII
        caracter = chr(int(byte, 2))
        caracteres_ascii.append(caracter)
    return ''.join(caracteres_ascii)  # Une los caracteres en una cadena

# Solicita el texto en Base64 al usuario
texto_base64 = input("Introduce el texto en Base64 que deseas convertir a ASCII: ")

# Convierte el Base64 a binario
binario = base64_a_binario(texto_base64)

# Convierte el binario a texto ASCII
texto_ascii = binario_a_ascii(binario)

# Imprime los resultados
print("\nTexto en Binario:")
print(binario)
print("\nTexto en ASCII:")
print(texto_ascii)






#conversación: https://chatgpt.com/share/67982de0-7740-8009-b080-8cbb67761a56