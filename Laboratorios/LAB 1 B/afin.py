import string
from collections import Counter
from math import gcd

# Lee el contenido del archivo cifrado "afines.txt"
with open("afines.txt", "r", encoding="utf-8") as file:
    ciphertext = file.read().strip()

# Define el alfabeto en español, incluyendo la letra 'ñ'
alphabet = "abcdefghijklmn\u00f1opqrstuvwxyz"
mod = len(alphabet)  # Longitud del alfabeto, utilizada en las operaciones modulares

# Frecuencia de aparición de cada letra en español (porcentaje)
spanish_freq = {
    'a': 11.525, 'b': 2.215, 'c': 4.019, 'd': 5.010, 'e': 12.181, 'f': 0.692,
    'g': 1.768, 'h': 0.703, 'i': 6.247, 'j': 0.493, 'k': 0.011, 'l': 4.967,
    'm': 3.157, 'n': 6.712, 'ñ': 0.311, 'o': 8.683, 'p': 2.510, 'q': 0.877,
    'r': 6.871, 's': 7.977, 't': 4.632, 'u': 2.927, 'v': 1.138, 'w': 0.017,
    'x': 0.215, 'y': 1.008, 'z': 0.467
}


def mod_inverse(a, m):
    """
    Calcula el inverso modular de `a` módulo `m`, necesario para descifrar el cifrado Afín.
    Retorna el inverso modular si existe, de lo contrario, retorna None.
    """
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def decrypt_affine(text, a, b):
    """
    Descifra un texto cifrado utilizando el cifrado Afín.
    
    :param text: Texto cifrado.
    :param a: Clave multiplicativa (debe ser coprima con `mod`).
    :param b: Clave aditiva (desplazamiento en el alfabeto).
    :return: Texto descifrado o None si `a` no tiene inverso modular.
    """
    decrypted_text = ""
    a_inv = mod_inverse(a, mod)
    if a_inv is None:
        return None  # Si `a` no tiene inverso modular, no se puede descifrar
    
    for char in text:
        if char in alphabet:  # Solo procesa caracteres dentro del alfabeto
            idx = (a_inv * (alphabet.index(char) - b)) % mod
            decrypted_text += alphabet[idx]
        else:
            decrypted_text += char  # Mantiene los caracteres no alfabéticos sin cambios
    return decrypted_text


def frequency_score(text):
    """
    Calcula una métrica de similitud basada en la frecuencia de letras en español.
    Un puntaje más bajo indica que el texto se asemeja más al español natural.
    
    :param text: Texto a analizar.
    :return: Puntaje de diferencia con respecto a la distribución esperada.
    """
    text_freq = Counter(text)  # Cuenta la frecuencia de cada letra en el texto
    total_chars = sum(text_freq.values())
    
    score = 0  # Puntaje de similitud
    for char in text_freq:
        if char in spanish_freq:
            observed_freq = (text_freq[char] / total_chars) * 100
            expected_freq = spanish_freq[char]
            score += abs(observed_freq - expected_freq)
    
    return score


# Lista para almacenar los resultados de las diferentes combinaciones de claves
results = []

# Itera sobre los posibles valores de `a` (debe ser coprimo con `mod`)
for a in range(1, 17):
    if gcd(a, mod) != 1:
        continue  # Si `a` no es coprimo con `mod`, se omite esta clave
    
    # Itera sobre los posibles valores de `b` (desplazamientos)
    for b in range(1, 17):
        decrypted = decrypt_affine(ciphertext, a, b)
        if decrypted:
            score = frequency_score(decrypted)  # Calcula la métrica de similitud
            results.append((a, b, decrypted, score))
            print(f"Clave a={a}, b={b}\nTexto descifrado:\n{decrypted}\nMétrica de similitud: {score}\n")

# Ordena los resultados por la mejor métrica de similitud
results.sort(key=lambda x: x[3])
best_a, best_b, best_text, best_score = results[0]

# Muestra la mejor clave encontrada y el texto descifrado
print(f"Mejor clave encontrada: a={best_a}, b={best_b}")
print(f"Texto descifrado:\n{best_text}")
