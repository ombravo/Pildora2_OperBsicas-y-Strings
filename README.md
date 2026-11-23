# 🐍 Fundamentos de Python: Operaciones Básicas y Strings

Este repositorio contiene el material teórico y práctico correspondiente a la **Píldora 2: Operaciones Básicas y Operaciones con Strings** (por Oscar Bravo). Está diseñado para aprender y reforzar los pilares básicos de la manipulación de datos numéricos, lógica booleana y cadenas de texto en Python.

---

## 📂 Contenido del Repositorio

El proyecto está organizado en tres recursos principales que combinan teoría visual, ejemplos ejecutables y ejercicios prácticos:

1. **`00 Presentacion_Pildora_2 OperBasicasStrings OscarBravo.pptx`** (Presentación)
   * Material teórico y visual con diagramas conceptuales sobre operadores aritméticos, comparación, lógica booleana y manipulación avanzada de strings.
2. **Cuaderno Interactivo (`.ipynb`)**
   * Jupyter Notebook con celdas de código ejecutables que ilustran paso a paso los conceptos de la presentación, incluyendo ejemplos de errores comunes (`ZeroDivisionError`, `TypeError`) y cómo resolverlos.
3. **`Soluciones.py`** (Script de Python)
   * Archivo con las soluciones comentadas a 4 ejercicios prácticos integradores que ponen a prueba todos los conceptos vistos en la sesión.

---

## 📚 Temario Cubierto

### 1. Operaciones Aritméticas y División
* **Operadores estándar:** Suma (`+`), resta (`-`), multiplicación (`*`), división tradicional (`/`, devuelve `float`) y potencia (`**`).
* **Disección de la división:**
  * División entera (`//`): Extrae únicamente el cociente entero.
  * Módulo (`%`): Extrae el resto de la división.
* **Manejo de errores:** Prevención de `ZeroDivisionError` al dividir por cero.

### 2. Operadores de Comparación y Lógicos
* **Comparación:** Igualdad (`==`), desigualdad (`!=`), menor que (`<`), mayor que (`>`), menor o igual (`<=`) y mayor o igual (`>=`), devolviendo valores booleanos (`True` / `False`).
* **Lógicos:** Combinación e inversión de condiciones mediante `and`, `or` y `not`.

### 3. Manipulación de Cadenas de Texto (`Strings`)
* **Inmutabilidad y Concatenación:** Unión de cadenas con `+` y conversión explícita de tipos con `str()` para evitar `TypeError`.
* **Indexación y Slicing:**
  * Acceso posicional mediante índices positivos (desde `0`) y negativos (desde `-1`).
  * Extracción de subcadenas mediante la sintaxis `[inicio:fin:paso]` (incluyendo inversión de texto con `[::-1]`).
* **Formateo Moderno (`f-strings`):** Inyección limpia y legible de variables y expresiones dentro de cadenas de texto (`f"Hola, {nombre}"`).
* **Métodos de Limpieza y Transformación:**
  * `.strip()`: Eliminación de espacios en blanco al inicio y al final.
  * `.replace(antiguo, nuevo)`: Sustitución de subcadenas.
  * `.split(delimitador)`: Fragmentación de un string en una lista de elementos.

---

## 🧪 Resumen de los Ejercicios (`Soluciones.py`)

El script `Soluciones.py` resuelve cuatro casos prácticos:
* **Ejercicio 1 (Logística):** Cálculo de camiones llenos, cajas sobrantes, porcentaje de ocupación y combinaciones posibles usando `//`, `%`, `/` y `**`.
* **Ejercicio 2 (Evaluación de riesgo):** Validación de requisitos financieros combinando operadores relacionales y lógicos (`and`, `not`, `!=`).
* **Ejercicio 3 (Limpieza de registros):** Normalización de una cadena de texto sucia encadenando `.strip()`, `.replace()` y `.split()`.
* **Ejercicio 4 (Procesamiento de códigos):** Extracción de número de serie y país mediante *slicing*, inversión de caracteres y formateo con `f-strings`.

---

## 🚀 Cómo usar este material

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Ejecuta el script de soluciones:**
   ```bash
   python Soluciones.py
   ```

3. **Explora el Jupyter Notebook:**
   Abre el archivo `.ipynb` utilizando **Jupyter Notebook**, **JupyterLab**, **Visual Studio Code** (con la extensión de Jupyter) o súbelo a **Google Colab** para ejecutar y modificar las celdas de prueba.

---

## 📋 Requisitos

* **Python 3.6 o superior** (necesario para el soporte de `f-strings`).
* No requiere librerías externas; todo el código utiliza la biblioteca estándar de Python.