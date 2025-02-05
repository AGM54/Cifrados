import string
from collections import Counter

# Lee el contenido del archivo cifrado "ceasar.txt"
with open("ceasar.txt", "r", encoding="utf-8") as file:
    ciphertext = file.read().strip()  # Elimina espacios en blanco al inicio y final

# Define el alfabeto en español con la letra 'ñ'
alphabet = "abcdefghijklmn\u00f1opqrstuvwxyz"

# Frecuencia de aparición de cada letra en español (porcentaje)
spanish_freq = {
    'a': 11.525, 'b': 2.215, 'c': 4.019, 'd': 5.010, 'e': 12.181, 'f': 0.692,
    'g': 1.768, 'h': 0.703, 'i': 6.247, 'j': 0.493, 'k': 0.011, 'l': 4.967,
    'm': 3.157, 'n': 6.712, 'ñ': 0.311, 'o': 8.683, 'p': 2.510, 'q': 0.877,
    'r': 6.871, 's': 7.977, 't': 4.632, 'u': 2.927, 'v': 1.138, 'w': 0.017,
    'x': 0.215, 'y': 1.008, 'z': 0.467
}


def decrypt_caesar(text, shift):
    """
    Descifra un texto cifrado con el cifrado César utilizando un desplazamiento dado.
    
    :param text: Texto cifrado
    :param shift: Número de posiciones a desplazar hacia la izquierda en el alfabeto
    :return: Texto descifrado
    """
    decrypted_text = ""
    for char in text:
        if char in alphabet:  # Solo se descifran caracteres que están en el alfabeto
            idx = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[idx]
        else:
            decrypted_text += char  # Conserva los caracteres que no son letras
    return decrypted_text


def frequency_score(text):
    """
    Calcula una métrica de similitud basada en la frecuencia de letras en español.
    Cuanto menor sea el puntaje, más similar es el texto al español natural.
    
    :param text: Texto a analizar
    :return: Puntaje de diferencia con respecto a la distribución esperada
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


# Prueba todos los desplazamientos posibles (de 1 a 30)
results = []
for shift in range(1, 31):
    decrypted = decrypt_caesar(ciphertext, shift)  # Descifra el texto con el desplazamiento
    score = frequency_score(decrypted)  # Evalúa la similitud con el español
    results.append((shift, decrypted, score))
    print(f"Clave: {shift}\nTexto descifrado:\n{decrypted}\nMétrica de similitud: {score}\n")

# Ordena los resultados por la mejor métrica de similitud
results.sort(key=lambda x: x[2])
best_shift, best_text, best_score = results[0]

# Muestra el mejor resultado encontrado
print(f"Mejor desplazamiento encontrado: {best_shift}")
print(f"Texto descifrado:\n{best_text}")
#https://chatgpt.com/share/67a2d06d-d460-8009-9957-41ca32f50d55