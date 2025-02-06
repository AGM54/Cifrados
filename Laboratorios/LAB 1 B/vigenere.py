import string
from collections import Counter
from itertools import product

# Leer el contenido del archivo vigenere.txt
with open("vigenere.txt", "r", encoding="utf-8") as file:
    ciphertext = file.read().strip().lower()

# Alfabeto español
alphabet = "abcdefghijklmnñopqrstuvwxyz"
mod = len(alphabet)

# Frecuencia de letras en español
spanish_freq = {
    'a': 11.525, 'b': 2.215, 'c': 4.019, 'd': 5.010, 'e': 12.181, 'f': 0.692,
    'g': 1.768, 'h': 0.703, 'i': 6.247, 'j': 0.493, 'k': 0.011, 'l': 4.967,
    'm': 3.157, 'n': 6.712, 'ñ': 0.311, 'o': 8.683, 'p': 2.510, 'q': 0.877,
    'r': 6.871, 's': 7.977, 't': 4.632, 'u': 2.927, 'v': 1.138, 'w': 0.017,
    'x': 0.215, 'y': 1.008, 'z': 0.467
}

# Bigrama y trigramas frecuentes en español
common_bigrams = ["de", "la", "el", "en", "es", "un", "se", "al", "lo", "le"]
common_trigrams = ["que", "los", "del", "las", "por", "con", "una", "sus", "mas"]

# Función para descifrar el cifrado Vigenère
def decrypt_vigenere(text, key):
    decrypted_text = ""
    key = key.lower()
    key_length = len(key)
    
    if not all(k in alphabet for k in key):
        return None  
    
    key_indices = [alphabet.index(k) for k in key]
    
    for i, char in enumerate(text):
        if char in alphabet:
            idx = (alphabet.index(char) - key_indices[i % key_length]) % mod
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

# Función para evaluar cuántos bigramas y trigramas comunes tiene el texto
def bigram_trigram_score(text):
    bigram_count = sum(text.count(bigram) for bigram in common_bigrams)
    trigram_count = sum(text.count(trigram) for trigram in common_trigrams)
    return bigram_count + trigram_count  

# Generar todas las posibles claves de 6 caracteres, comenzando con "pa"
possible_keys = ["pa" + "".join(p) for p in product(alphabet, repeat=4)]

# Realizar ataque de fuerza bruta probando todas las claves posibles
results = []
for key in possible_keys:
    decrypted = decrypt_vigenere(ciphertext, key)
    if decrypted:
        freq_score = frequency_score(decrypted)  
        structure_score = bigram_trigram_score(decrypted)  
        results.append((key, decrypted, freq_score, structure_score))


results.sort(key=lambda x: (-x[3], x[2]))  

# Mostrar el Top 10 mejores resultados encontrados
top_n = 10
print(f"\nTop {top_n} mejores claves encontradas:")

for i, (key, text, freq_score, struct_score) in enumerate(results[:top_n], start=1):
    print(f"\n {i}. Clave: {key}")
    print(f"Puntuación de estructuras comunes en español: {struct_score}")
    print(f" Métrica de similitud: {freq_score:.3f}")
    print(f" Texto descifrado :\n{text[:300]}...\n")

best_key, best_text, best_freq_score, best_struct_score = results[0]

print(f"\n Mejor clave según estructura en español: {best_key}")
print(f"Puntuación de estructuras comunes en español: {best_struct_score}")
print(f"Métrica de similitud: {best_freq_score:.3f}")
print(f"Texto descifrado :\n{best_text[:300]}...\n")
