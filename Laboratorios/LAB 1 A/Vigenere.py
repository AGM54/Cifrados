ALFABETO = "abcdefghijklmnñopqrstuvwxyz"

def limpiar_texto(texto):
    """Convierte a minúsculas y elimina caracteres que no están en el alfabeto."""
    return "".join([c for c in texto.lower() if c in ALFABETO])

def encriptar_vigenere(texto, clave):
    """
    Encripta el texto usando el cifrado Vigenère.
    """
    texto = limpiar_texto(texto)
    clave = limpiar_texto(clave)
    n = len(ALFABETO)
    resultado = ""
    longitud_clave = len(clave)
    for i, char in enumerate(texto):
        indice_texto = ALFABETO.index(char)
        indice_clave = ALFABETO.index(clave[i % longitud_clave])
        nuevo_indice = (indice_texto + indice_clave) % n
        resultado += ALFABETO[nuevo_indice]
    return resultado

def desencriptar_vigenere(texto, clave):
    """
    Desencripta el texto cifrado con el cifrado Vigenère.
    """
    texto = limpiar_texto(texto)
    clave = limpiar_texto(clave)
    n = len(ALFABETO)
    resultado = ""
    longitud_clave = len(clave)
    for i, char in enumerate(texto):
        indice_texto = ALFABETO.index(char)
        indice_clave = ALFABETO.index(clave[i % longitud_clave])
        indice_original = (indice_texto - indice_clave) % n
        resultado += ALFABETO[indice_original]
    return resultado

if __name__ == "__main__":
    ejemplos = [
        ("Hola Mundo", "clave"),
        ("Seguridad Informática", "secreto"),
        ("Mensaje confidencial", "privado"),
        ("Python es increíble", "codigo"),
        ("Cifrado Vigenere", "criptografia"),
        ("Ataque al anochecer", "oculto"),
        ("Examen final de criptografía", "universidad")
    ]

    print("=== Pruebas del Cifrado Vigenère ===")
    for texto, clave in ejemplos:
        encriptado = encriptar_vigenere(texto, clave)
        desencriptado = desencriptar_vigenere(encriptado, clave)
        print("\n🔹 Ejemplo:")
        print(f"Texto original:   {texto}")
        print(f"Clave:            {clave}")
        print(f"Texto encriptado: {encriptado}")
        print(f"Texto desencriptado: {desencriptado}")
#https://chatgpt.com/share/67a040a0-10c4-8009-8573-712f02f4fdef