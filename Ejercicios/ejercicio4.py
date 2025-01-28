def binario_a_texto(binario):
    # Dividir la cadena binaria en grupos de 8 bits
    caracteres = [binario[i:i+8] for i in range(0, len(binario), 8)]
    # Convertir cada grupo de 8 bits a un carácter ASCII
    texto = ''.join(chr(int(byte, 2)) for byte in caracteres)
    return texto

texto_binario = input("Introduce el texto en binario (grupos de 8 bits separados por espacios): ")
binario_sin_espacios = texto_binario.replace(" ", "")

# Convierte el binario a texto
texto_ascii = binario_a_texto(binario_sin_espacios)

print("\nTexto en ASCII:")
print(texto_ascii)
