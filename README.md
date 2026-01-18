# 🎲 Bingo_P – Asistente del Concursante

## 📌 Descripción general

**Bingo_P** es una aplicación diseñada como **asistente para el concursante de un bingo de palabras**.  
Su objetivo es ayudar a una persona que juega con **muchos cartones simultáneamente**, permitiéndole verificar de forma **rápida, confiable y en tiempo real** si las palabras anunciadas corresponden a alguno de sus cartones.

La aplicación **NO administra el bingo**, **NO genera palabras**, ni **controla a otros jugadores**.  
Únicamente actúa como **herramienta de soporte para un solo concursante**.

---

## 🧠 Estrategia algorítmica

La solución combina varias estrategias de diseño de algoritmos, según la naturaleza de cada tarea:

- **Fuerza Bruta**  
  - Lectura de vocabularios
  - Carga de cartones
  - Comparación directa de palabras  
  (el tamaño del problema está acotado)

- **Divide y Vencerás**  
  - Organización lógica por idioma
  - Cada ronda procesa solo un subconjunto independiente

- **Estrategia Voraz**  
  - Marcado inmediato de palabras
  - Verificación instantánea de bingo
  - Finalización temprana de la ronda al detectar ganador

Estas decisiones permiten un sistema **eficiente, claro y fácil de mantener**, sin sobreingeniería.

---

## 🖥️ Interfaz Gráfica (UI)

La interfaz gráfica está implementada en **Python con Tkinter + ttkbootstrap**, manteniendo una **separación total entre lógica y presentación**.

### 🔹 Características clave de la UI

- Una **única ventana**
- **Zona dinámica superior** (contenido de la ronda)
- **Log fijo en la parte inferior**, siempre visible
- Flujo guiado, sin entradas por consola
- Autocompletado de palabras por idioma
- Manejo completo de errores de entrada

---

## 🔁 Flujo de funcionamiento de la UI

### 1️⃣ Inicio automático de ronda

- Al iniciar la aplicación, **NO se solicita al usuario elegir idioma**.
- El sistema selecciona **automáticamente** un idioma para la ronda.
- El idioma:
  - No se repite dos veces seguidas
  - Recorre los cuatro idiomas disponibles (SP, EN, PT, DT)
  - Se reordena aleatoriamente cada ciclo completo

El idioma actual se muestra como **título principal** de la ventana.

---

### 2️⃣ Carga de cartones

Una vez iniciado el idioma de la ronda, se habilita la sección **Carga de cartones**, con dos opciones:

#### 📄 Carga por archivo TXT
- Cada línea del archivo representa un cartón
- Formato:
```

ID palabra1 palabra2 palabra3 ...

```
- Validaciones:
- El número de palabras debe coincidir con el idioma
- Las tablas inválidas se ignoran
- Se informa en el log:
  - Total procesadas
  - Cuántas válidas
  - Cuántas inválidas y por qué

#### ✍️ Ingreso manual
- Se generan automáticamente **N campos de texto**, según el idioma
- El usuario debe completar **todos los campos**
- No se permite avanzar si falta alguna palabra
- Al confirmar, el cartón queda cargado y listo

Una vez cargados los cartones:
- La sección de carga se **oculta**
- Se habilita automáticamente la sección de ronda

---

### 3️⃣ Ronda de bingo (anuncio de palabras)

Durante la ronda:

- Se muestra un campo de texto con botón **“Anunciar”**
- El usuario ingresa las palabras que van siendo anunciadas en el bingo real
- Existe **autocompletado por idioma**, usando el vocabulario completo
- Al seleccionar una sugerencia, se completa el campo automáticamente

Cada palabra anunciada:
- Se marca de forma inmediata en los cartones
- Se verifica si alguno ha completado todas sus palabras

El sistema **NO muestra mensajes innecesarios** por cada palabra.  
Solo reacciona cuando ocurre un evento relevante.

---

### 4️⃣ Detección de Bingo

Cuando uno o más cartones completan todas sus palabras:

- Se detecta el **BINGO de forma inmediata**
- Se muestra una vista de resultado con:
- Mensaje de bingo
- Identificador del cartón ganador
- Aparece el botón:
**“Otra siguiente ronda”**

---

### 5️⃣ Nueva ronda

Al presionar **“Otra siguiente ronda”**:

- El panel de resultado se oculta
- Se reinicia el estado de la ronda
- Se selecciona automáticamente un **nuevo idioma**
- El flujo vuelve al paso de carga de cartones

La aplicación puede ejecutarse de forma continua durante múltiples rondas.

---

## 📋 Log del sistema

En la parte inferior de la ventana existe un **log fijo**, que nunca desaparece.

El log informa:
- Idioma seleccionado automáticamente
- Estado de carga de cartones
- Errores de validación
- Palabras anunciadas
- Detección de bingo

Para fines de prueba, el log también puede mostrar las **palabras ganadoras de la ronda**, marcadas como información de depuración.

---

## 📂 Estructura del proyecto

```

bingo_p/
├── core/              # Lógica del sistema (algoritmos)
│   ├── carton.py
│   ├── ronda_bingo.py
│   ├── lector_txt.py
│   ├── vocabulario.py
│   ├── normalizador.py
│   └── datos_prueba.py
│
├── ui/                # Interfaz gráfica
│   ├── app.py
│   ├── estado.py
│   ├── panel_carga.py
│   ├── panel_ronda.py
│   └── panel_resultado.py
│
├── data/
│   └── vocabularios/
│       ├── SP.txt
│       ├── EN.txt
│       ├── PT.txt
│       └── DT.txt
│
└── README.md

````

---

## 🚀 Ejecución

### Requisitos
- Python 3.10+
- ttkbootstrap

Instalación:
```bash
pip install ttkbootstrap
````

Ejecución:

```bash
python ui/app.py
```

---

## 🎓 Nota académica

La interfaz gráfica **no altera la lógica del sistema**.
Todo el procesamiento sigue siendo realizado por el core, respetando las estrategias de diseño de algoritmos analizadas:

* Fuerza Bruta
* Divide y Vencerás
* Estrategia Voraz

La UI actúa únicamente como **capa de presentación**, validación y experiencia de usuario.

---

## 👥 Autores

**Grupo 6**

* Steven Lino I.
* Erick Murillo
* Juan Pablo Plúas
* Leonel Cabrera

```