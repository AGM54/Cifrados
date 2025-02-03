
ALFABETO = "abcdefghijklmnñopqrstuvwxyz"

def limpiar_texto(texto):
    return "".join([c for c in texto.lower() if c in ALFABETO])

def analisis_frecuencia(texto):
    """
    Calcula la distribución de frecuencia (probabilidades) de cada letra en el texto.
    
    La función:
      - Limpia el texto usando 'limpiar_texto'.
      - Cuenta la cantidad de veces que aparece cada letra.
      - Divide el conteo de cada letra entre el total de caracteres para obtener la probabilidad.
      - Asegura que todas las letras del alfabeto estén en el resultado, asignando 0 a las que no aparezcan.
    
    Parámetros:
      texto: cadena de texto a analizar.
    
    Retorna:
      Un diccionario donde la clave es la letra y el valor es la probabilidad (frecuencia relativa).
    """
    texto_limpio = limpiar_texto(texto)
    total = len(texto_limpio)
    
 
    frecuencias = {letra: 0 for letra in ALFABETO}
    
    # Contamos las apariciones de cada letra en el texto limpio
    for char in texto_limpio:
        if char in frecuencias:
            frecuencias[char] += 1
    
    if total > 0:
        frecuencias = {letra: (conteo / total) for letra, conteo in frecuencias.items()}
    else:
        frecuencias = {letra: 0 for letra in ALFABETO}
    
    return frecuencias


if __name__ == "__main__":
    texto = (
        "Este es un ejemplo de análisis de frecuencia. "
        "Se calcularán las probabilidades de cada letra en el texto, "
        "incluso aquellas que no aparezcan tendrán probabilidad 0."
    )
    
    frecuencias = analisis_frecuencia(texto)
    
    print("Análisis de Frecuencia (probabilidades):")
    for letra in sorted(frecuencias.keys()):
        print(f"{letra}: {frecuencias[letra]:.4f}")
