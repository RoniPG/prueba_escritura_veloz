# Prueba de Escritura Veloz

Programa en Python que evalúa tu **velocidad y precisión de escritura** a partir de una frase aleatoria.
Incluye una interfaz gráfica sencilla creada con **tkinter**, ideal para entender lo basico de las GUI.

#### El programa mostrará una frase aleatoria y medirá:

- ⏱️ Tiempo que tardas en escribirla

- 🎯 Precisión del texto

- ⌨️ Velocidad de escritura (WPM – palabras por minuto)

## 📦 Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/typing-speed-test.git
cd typing-speed-test
```

### 2️⃣ (Opcional) Crear un entorno virtual con conda

```
conda create -n escritura_veloz_env python=3.11
conda activate escritura_veloz_env
```

## Uso

Para ejecutar la aplicación, simplemente lanza el script principal:

```bash
python main.py
````

## 🛠️ Tecnologías a usar

- Python 3.11
 
- tkinter → interfaz gráfica

- time / timeit → medir el tiempo

- random → seleccionar frases aleatorias

## 📂 Estructura inicial del proyecto

```
typing-speed-test/
│
├── main.py
├── phrases.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 🧪 Flujo del programa

1. Mostrar frase aleatoria

2. Usuario pulsa Iniciar

3. Empieza el cronómetro

4. Usuario escribe la frase

5. Se detiene el tiempo

6. Se muestran:

   - ⏱️ Tiempo

   - ⌨️ WPM

   - 🎯 Precisión %

## 📈 Posibles mejoras (futuras versiones)

- Resaltar errores en rojo

- Contador de errores

- Reiniciar prueba

- Modo oscuro

- Exportar resultados

## 🏁 Objetivo del MVP


✔️ Interfaz funcional

✔️ Medición de tiempo

✔️ Cálculo de velocidad y precisión

✔️ Código claro y modular
