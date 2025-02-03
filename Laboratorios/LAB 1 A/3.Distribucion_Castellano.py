
ALFABETO = "abcdefghijklmnñopqrstuvwxyz"

def limpiar_texto(texto):
    return "".join([c for c in texto.lower() if c in ALFABETO])

def analisis_frecuencia(texto):
    texto_limpio = limpiar_texto(texto)
    total = len(texto_limpio)

    frecuencias = {letra: 0 for letra in ALFABETO}
    
    # Contamos las apariciones.
    for char in texto_limpio:
        if char in frecuencias:
            frecuencias[char] += 1
    
    if total > 0:
        frecuencias = {letra: (conteo / total) * 100 for letra, conteo in frecuencias.items()}
    else:
        frecuencias = {letra: 0 for letra in ALFABETO}
    
    return frecuencias

def comparar_distribucion(frecuencia_observada, frecuencia_teorica):
  
    print("{:<5} {:>15} {:>15} {:>15}".format("Letra", "Teórica (%)", "Observada (%)", "Diferencia"))
    print("-" * 60)
    for letra in ALFABETO:
        teorica = frecuencia_teorica.get(letra, 0)
        observada = frecuencia_observada.get(letra, 0)
        diferencia = abs(teorica - observada)
        print("{:<5} {:>15.2f} {:>15.2f} {:>15.2f}".format(letra.upper(), teorica, observada, diferencia))

def main():
    frecuencia_teorica = {
        'a': 12.53, 'b': 1.42,  'c': 4.68,  'd': 5.86,  'e': 13.68,
        'f': 0.69,  'g': 1.01,  'h': 0.70,  'i': 6.25,
        'j': 0.44,  'k': 0.02,  'l': 4.97,  'm': 3.15,  'n': 6.71,
        'ñ': 0.31,  'o': 8.68,  'p': 2.51,  'q': 0.88,
        'r': 6.87,  's': 7.98,  't': 4.63,  'u': 3.93,  'v': 0.90,
        'w': 0.01,  'x': 0.22,  'y': 0.90,  'z': 0.52
    }

    texto = (
        "Este es un ejemplo de texto para analizar la frecuencia de las letras. "
        "El propósito es comparar la distribución observada con la distribución teórica del castellano."
    )
    
    frecuencia_observada = analisis_frecuencia(texto)
    
    print("Comparación de Distribución Observada vs. Teórica:\n")
    comparar_distribucion(frecuencia_observada, frecuencia_teorica)

if __name__ == "__main__":
    main()
