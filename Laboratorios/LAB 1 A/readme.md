
# 🔐 Laboratorio 1 – Encriptado y Decriptado de Texto



## 📌 **Objetivos**
- Implementar funciones para encriptar y desencriptar un texto en castellano utilizando distintos cifrados.
- Desarrollar un análisis de frecuencia para evaluar la distribución de caracteres en un texto cifrado.
- Comparar la distribución de caracteres obtenida con la distribución teórica del castellano.

---

## 📝 **Estructura del Proyecto**
El laboratorio se ha dividido en tres partes principales:

### 📌 **1. Implementación de los Cifrados**
Se crearon scripts independientes para los siguientes cifrados clásicos:

1. `Cifrado_Cesar.py`  
   - Implementa el Cifrado César con un desplazamiento configurable.  
   - Incluye funciones de **encriptado** y **decriptado**.
   
2. `Cifrado_Afin.py`  
   - Implementa el Cifrado Afín basado en la ecuación matemática:  
     \[ C(x) = (ax + b) \mod m \]
   - Se valida que el coeficiente `a` tenga **inverso modular** en el espacio del alfabeto (27 letras).
   
3. `Cifrado_Vigenere.py`  
   - Implementa el Cifrado Vigenère con una clave repetitiva.  
   - Usa el alfabeto castellano (incluyendo la letra `ñ`).  

Cada script incluye ejemplos de **encriptado y decriptado** para verificar su funcionamiento.

---

### 📊 **2. Análisis de Frecuencia**
El archivo `Analisis_Frecuencia.py` contiene una implementación para calcular la distribución de letras en un texto dado.  



### 📈 **3. Comparación con la Distribución del Castellano**
El script `Distribucion_Castellano.py` compara la frecuencia observada en el análisis de frecuencia con la **distribución teórica** del castellano.  


```
/LAB_1_A
│── Cifrado_Cesar.py
│── Cifrado_Afin.py
│── Cifrado_Vigenere.py
│── Analisis_Frecuencia.py
│── Distribucion_Castellano.py
│── README.md
```

---


