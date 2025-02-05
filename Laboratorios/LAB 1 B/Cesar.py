import string
from collections import Counter

# Leer el contenido del archivo ceasar.txt
with open("ceasar.txt", "r", encoding="utf-8") as file:
    ciphertext = file.read().strip()  # Eliminamos espacios en blanco al inicio y final

# Alfabeto español
alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Frecuencia de letras en español
spanish_freq = {
    'a': 11.525, 'b': 2.215, 'c': 4.019, 'd': 5.010, 'e': 12.181, 'f': 0.692,
    'g': 1.768, 'h': 0.703, 'i': 6.247, 'j': 0.493, 'k': 0.011, 'l': 4.967,
    'm': 3.157, 'n': 6.712, 'ñ': 0.311, 'o': 8.683, 'p': 2.510, 'q': 0.877,
    'r': 6.871, 's': 7.977, 't': 4.632, 'u': 2.927, 'v': 1.138, 'w': 0.017,
    'x': 0.215, 'y': 1.008, 'z': 0.467
}

# Función para descifrar César con un desplazamiento dado
def decrypt_caesar(text, shift):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            idx = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[idx]
        else:
            decrypted_text += char
    return decrypted_text

# Función para calcular la métrica de similitud de frecuencia
def frequency_score(text):
    text_freq = Counter(text)
    total_chars = sum(text_freq.values())
    
    score = 0
    for char in text_freq:
        if char in spanish_freq:
            observed_freq = (text_freq[char] / total_chars) * 100
            expected_freq = spanish_freq[char]
            score += abs(observed_freq - expected_freq)
    
    return score

# Realizar ataque de fuerza bruta probando todos los desplazamientos
results = []
for shift in range(1, 31):
    decrypted = decrypt_caesar(ciphertext, shift)
    score = frequency_score(decrypted)
    results.append((shift, decrypted, score))
    print(f"Clave: {shift}\nTexto descifrado:\n{decrypted}\nMétrica de similitud: {score}\n")

# Ordenar por la mejor métrica (menor diferencia de frecuencia)
results.sort(key=lambda x: x[2])
best_shift, best_text, best_score = results[0]

# Mostrar el mejor resultado encontrado
print(f"Mejor desplazamiento encontrado: {best_shift}")
print(f"Texto descifrado:\n{best_text}")
