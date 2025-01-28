def texto_a_binario(texto):
    return ' '.join(format(ord(caracter), '08b') for caracter in texto)

# Solicita el texto al usuario
texto = input("Introduce el texto que deseas convertir a binario: ")

# Convierte el texto a binario
binario = texto_a_binario(texto)

print("\nTexto en Binario:")
print(binario)
