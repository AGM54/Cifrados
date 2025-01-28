import base64

def binario_a_base64(binario):
    try:
        # Validar que el binario tenga una longitud múltiplo de 8
        if len(binario) % 8 != 0:
            raise ValueError("El texto binario debe tener una longitud múltiplo de 8.")

        bytes_array = []
        for i in range(0, len(binario), 8):
            byte = binario[i:i+8]
            # Verificar que el byte solo contenga ceros y unos
            if not all(bit in "01" for bit in byte):
                raise ValueError(f"El grupo '{byte}' no es un binario válido.")
            # Convertir cada grupo de 8 bits a un entero
            bytes_array.append(int(byte, 2))
        
        # Convertir los enteros a bytes
        bytes_data = bytes(bytes_array)
        
        # Codificar los bytes a Base64
        base64_resultado = base64.b64encode(bytes_data).decode('utf-8')
        return base64_resultado
    except Exception as e:
        return f"Error: {e}"


# Solicitar entrada del usuario
texto_binario = input("Introduce el texto en binario (grupos de 8 bits separados por espacios): ")
# Eliminar espacios entre los bits
binario_sin_espacios = texto_binario.replace(" ", "")

# Llamar a la función de conversión
base64_texto = binario_a_base64(binario_sin_espacios)

# Mostrar el resultado
print("\nTexto en Base64:")
print(base64_texto)



#conversación: https://chatgpt.com/share/67982de0-7740-8009-b080-8cbb67761a56