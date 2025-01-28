def aplicar_xor(binario, clave):
    resultado_xor = []
    longitud_clave = len(clave)

    for i in range(len(binario)):
        bit_binario = int(binario[i]) 
        bit_clave = int(clave[i % longitud_clave]) 
        resultado_xor.append(str(bit_binario ^ bit_clave))  
    
    return ''.join(resultado_xor) 


binario = input("Introduce el binario al que deseas aplicar XOR (sin espacios): ")
clave = input("Introduce la clave binaria (sin espacios): ")


resultado = aplicar_xor(binario, clave)

print("\nResultado del XOR:")
print(resultado)
