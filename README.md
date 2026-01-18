# 🎯 Bingo_P – Asistente del Concursante

**Mini Proyecto Final – Análisis de Algoritmos**

---

## 📌 Descripción general del proyecto

**Bingo_P** es una aplicación diseñada como **asistente personal del concursante** en partidas de bingo con palabras, inspirado en los bingos masivos realizados durante la pandemia, donde un jugador puede tener **decenas o cientos de cartones simultáneamente**.

El sistema permite al usuario:

* Cargar uno o varios cartones (manual o por archivo `.txt`)
* Seleccionar el idioma de la ronda
* Ingresar manualmente las palabras anunciadas por el locutor
* Marcar automáticamente coincidencias
* Detectar de forma inmediata si uno o más cartones han completado todas sus palabras (**bingo**)

El proyecto prioriza **eficiencia**, **robustez** y **claridad algorítmica**, alineándose con los objetivos del curso de **Análisis de Algoritmos**.

---

## 🧠 Estrategias de diseño de algoritmos utilizadas

La solución **no depende de una sola estrategia**, sino de la combinación de varias, aplicadas según la naturaleza de cada tarea:

* **Fuerza Bruta**:
  Para lectura, validación y recorrido de datos con tamaño acotado.
* **Divide y Vencerás**:
  Para separar y procesar únicamente los cartones del idioma activo en cada ronda.
* **Estrategia Voraz**:
  Para el marcado inmediato de palabras y detección temprana del bingo sin recorridos innecesarios.

Estas decisiones permiten un procesamiento eficiente incluso con **más de 200 cartones**.

---

## 📂 Estructura del proyecto

```
Bingo_P/
│
├── main.py
│
├── core/
│   ├── carton.py
│   ├── ronda_bingo.py
│   ├── normalizador.py
│   ├── datos_prueba.py
│   ├── lector_txt.py
│   ├── carga_cartones.py
│   └── flujo_ronda.py
│
└── data/
    └── vocabularios/
```

---

## 🧩 Rol y estrategia de cada archivo

### 🔹 `main.py` – Orquestador del sistema

* **Responsabilidad**: coordinar el flujo general del programa.
* **NO implementa lógica de negocio**.
* Llama a funciones del core para:

  * Seleccionar idioma
  * Cargar cartones
  * Iniciar la ronda

**Estrategia**:
No aplica una estrategia algorítmica directa, actúa como controlador.

---

### 🔹 `core/carton.py` – Modelo de cartón

* Representa un cartón de bingo.
* Almacena palabras como `set` para búsqueda O(1).
* Mantiene un contador de palabras pendientes.

**Estrategia**:

* **Voraz**: cada palabra marcada es definitiva.
* **Optimización de tiempo**: evita recorrer el cartón completo.

---

### 🔹 `core/ronda_bingo.py` – Lógica de la ronda

* Procesa únicamente los cartones del idioma activo.
* Marca palabras y verifica ganadores inmediatamente.

**Estrategias**:

* **Divide y vencerás**: reduce el conjunto de cartones por idioma.
* **Voraz**: termina la ronda tan pronto se detecta bingo.

---

### 🔹 `core/lector_txt.py` – Lectura de archivos por lote

* Lee archivos `.txt` donde cada línea representa un cartón.
* Valida cantidad exacta de palabras por idioma.
* Ignora líneas inválidas y registra errores.

**Estrategia**:

* **Fuerza bruta**: recorrido lineal del archivo.
* Manejo robusto de errores sin abortar el programa.

---

### 🔹 `core/carga_cartones.py` – Gestión de entrada de cartones

* Permite elegir entre:

  * Ingreso manual
  * Carga por lote
* Implementa reintentos hasta obtener al menos un cartón válido.

**Estrategia**:

* **Fuerza bruta** + validación.
* Control de flujo y robustez ante errores de usuario.

---

### 🔹 `core/flujo_ronda.py` – Ejecución interactiva de la ronda

* Recibe palabras anunciadas por el usuario.
* Normaliza la entrada.
* Llama a la lógica de la ronda y detecta bingo.

**Estrategia**:

* **Voraz**: cada palabra se procesa inmediatamente.
* UX realista: solo se notifica cuando hay bingo.

---

### 🔹 `core/normalizador.py` – Normalización lingüística

* Convierte palabras a minúsculas.
* Elimina tildes y acentos.
* Garantiza comparaciones correctas entre idiomas.

**Estrategia**:

* Preprocesamiento eficiente.
* Mejora robustez sin afectar complejidad.

---

### 🔹 `core/datos_prueba.py` – Configuración y pruebas

* Define:

  * Cantidad de palabras por idioma
  * Palabras ganadoras de prueba
* Facilita pruebas controladas y reproducibles.

---

## ⚙️ Robustez y manejo de errores

El sistema garantiza que:

* ❌ No se cae ante errores de entrada
* 🔁 Reintenta cuando el archivo no es válido
* ⚠️ Informa errores al usuario sin abortar
* ✅ Solo inicia una ronda si existe al menos un cartón válido

Esto simula condiciones reales de uso y mejora la experiencia del usuario.

---

## 🚀 Siguientes pasos: migración a interfaz gráfica (GUI)

La arquitectura actual **ya está preparada** para una interfaz gráfica.
No es necesario modificar la lógica del core.

### 🔜 Paso 1 – Crear módulo `ui/`

```
ui/
└── interfaz.py
```

### 🔜 Paso 2 – Reemplazar `input()` por componentes gráficos

* Selección de idioma → `RadioButton` o `OptionMenu`
* Carga de archivos → `FileDialog`
* Ingreso de palabras → `Entry`
* Mensajes → `Label` / `MessageBox`

### 🔜 Paso 3 – Reutilizar el core sin cambios

La UI solo debe llamar a:

* `cargar_cartones()`
* `ejecutar_ronda()`
* Métodos de `RondaBingo` y `Carton`

### 🔜 Paso 4 – Mostrar cartones ganadores

* Usar un `Grid` para representar las palabras
* Cambiar color de palabras marcadas
* Navegar entre múltiples cartones ganadores si existen

---

## ✅ Conclusión

La solución implementada para **Bingo_P**:

* Cumple completamente con las especificaciones del proyecto
* Aplica correctamente las estrategias de diseño de algoritmos analizadas
* Es eficiente en tiempo y memoria
* Es robusta ante errores de entrada
* Está lista para evolucionar a una interfaz gráfica

El enfoque modular facilita la comprensión, mantenimiento y defensa académica del proyecto.