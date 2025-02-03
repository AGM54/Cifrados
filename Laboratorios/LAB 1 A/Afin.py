import math

ALFABETO = "abcdefghijklmnñopqrstuvwxyz"

def limpiar_texto(texto):
    """Convierte a minúsculas y elimina caracteres que no están en el alfabeto."""
    return "".join([c for c in texto.lower() if c in ALFABETO])

def es_coprimo(a, m):
    """Verifica si 'a' es coprimo con 'm'."""
    return math.gcd(a, m) == 1

def inverso_modular(a, m):
    """
    Calcula el inverso modular de 'a' módulo 'm'.
    
    Retorna el entero x tal que (a * x) % m == 1.
    """
    if not es_coprimo(a, m):
        raise ValueError(f"No existe inverso modular para a = {a} modulo m = {m}")
    
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No existe inverso modular para a = {} modulo m = {}".format(a, m))

def encriptar_afin(texto, a, b):
    """
    Encripta el texto usando el cifrado afín.
    """
    if not es_coprimo(a, len(ALFABETO)):
        raise ValueError(f"El valor de 'a' ({a}) no es coprimo con {len(ALFABETO)}, elige otro.")
    
    texto = limpiar_texto(texto)
    n = len(ALFABETO)
    resultado = ""
    for char in texto:
        indice = ALFABETO.index(char)
        nuevo_indice = (a * indice + b) % n
        resultado += ALFABETO[nuevo_indice]
    return resultado

def desencriptar_afin(texto, a, b):
    """
    Desencripta el texto cifrado con el cifrado afín.
    
    Fórmula: D(y) = a_inv * (y - b) mod m, donde a_inv es el inverso modular de a.
    """
    if not es_coprimo(a, len(ALFABETO)):
        raise ValueError(f"El valor de 'a' ({a}) no es coprimo con {len(ALFABETO)}, elige otro.")

    texto = limpiar_texto(texto)
    n = len(ALFABETO)
    a_inv = inverso_modular(a, n)
    resultado = ""
    for char in texto:
        indice = ALFABETO.index(char)
        indice_original = (a_inv * (indice - b)) % n
        resultado += ALFABETO[indice_original]
    return resultado


if __name__ == "__main__":
    ejemplos = [
        ("Hola Mundo", 5, 8),  
        ("Cifrado Afín", 7, 3), 
        ("Seguridad informática", 11, 6),  
        ("Python es genial", 4, 9), 
        ("Mensaje secreto", 19, 5), 
        ("Atacar al amanecer", 13, 7), 
        ("Clave de acceso", 25, 4) 
    ]

    print("=== Pruebas del Cifrado Afín ===")
    for texto, a, b in ejemplos:
        try:
            encriptado = encriptar_afin(texto, a, b)
            desencriptado = desencriptar_afin(encriptado, a, b)
            print("\n🔹 Ejemplo:")
            print(f"Texto original:   {texto}")
            print(f"Coeficiente a:    {a}")
            print(f"Coeficiente b:    {b}")
            print(f"Texto encriptado: {encriptado}")
            print(f"Texto desencriptado: {desencriptado}")
        except ValueError as e:
            print(f"\n⚠️ Error con texto '{texto}' (a={a}, b={b}): {e}")

#https://chatgpt.com/share/67a040a0-10c4-8009-8573-712f02f4fdef