ALFABETO = "abcdefghijklmnñopqrstuvwxyz"

def limpiar_texto(texto):
    return "".join([c for c in texto.lower() if c in ALFABETO])

def encriptar_cesar(texto, desplazamiento):
    texto = limpiar_texto(texto)
    n = len(ALFABETO)
    resultado = ""
    for char in texto:
        indice = ALFABETO.index(char)
        nuevo_indice = (indice + desplazamiento) % n
        resultado += ALFABETO[nuevo_indice]
    return resultado

def desencriptar_cesar(texto, desplazamiento):
    texto = limpiar_texto(texto)
    n = len(ALFABETO)
    resultado = ""
    for char in texto:
        indice = ALFABETO.index(char)
        nuevo_indice = (indice - desplazamiento) % n
        resultado += ALFABETO[nuevo_indice]
    return resultado


if __name__ == "__main__":
    ejemplos = [
        ("Hola Mundo", 3),
        ("Cifrado César", 5),
        ("Seguridad informática", 7),
        ("Python es genial", 4),
        ("Mensaje secreto", 8),
        ("Atacar al amanecer", 2),
        ("Clave de acceso", 6)
    ]

    print("=== Pruebas del Cifrado César ===")
    for texto, desplazamiento in ejemplos:
        encriptado = encriptar_cesar(texto, desplazamiento)
        desencriptado = desencriptar_cesar(encriptado, desplazamiento)
        print("\n🔹 Ejemplo:")
        print(f"Texto original:   {texto}")
        print(f"Desplazamiento:   {desplazamiento}")
        print(f"Texto encriptado: {encriptado}")
        print(f"Texto desencriptado: {desencriptado}")



#https://chatgpt.com/share/67a040a0-10c4-8009-8573-712f02f4fdef