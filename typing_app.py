import time
import tkinter as tk

from phrases import get_random_phrase


class TypingSpeedApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Prueba de Escritura Veloz")
        self.root.geometry("600x300")

        # Guardaremos referencias para usarlas más adelante
        self.phrase_label: tk.Label | None = None
        self.typing_entry: tk.Entry | None = None
        self.result_label: tk.Label | None = None

        # Estado de la prueba
        self.start_time: float | None = None

        self._build_widgets()

    def _build_widgets(self) -> None:
        # Etiqueta de bienvenida
        title_label = tk.Label(
            self.root, text="Prueba de Escritura Veloz", font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)

        # Mensaje descriptivo
        description_label = tk.Label(
            self.root,
            text=(
                "En esta aplicación verás una frase y tu reto será escribirla "
                "lo más rápido y preciso posible."
            ),
            wraplength=500,
            justify="center",
            font=("Arial", 12),
            fg="#555555",
        )
        description_label.pack(pady=10)

        # Frase aleatoria (solo visualización)
        random_phrase = get_random_phrase()
        self.phrase_label = tk.Label(
            self.root,
            text=random_phrase,
            wraplength=500,
            justify="center",
            font=("Arial", 12, "italic"),
            fg="#333333",
        )
        self.phrase_label.pack(pady=10)

        # Campo de texto donde el usuario escribirá la frase
        self.typing_entry = tk.Entry(
            self.root,
            width=70,
            font=("Arial", 12),
        )
        self.typing_entry.pack(pady=10)
        self.typing_entry.insert(0, "Escribe aquí la frase mostrada arriba...")
        self.typing_entry.config(fg="#888888")

        # Botón para iniciar la prueba
        start_button = tk.Button(
            self.root,
            text="Iniciar Prueba",
            command=self.start_test,
        )
        start_button.pack(pady=5)

        # Botón para finalizar la prueba
        finish_button = tk.Button(
            self.root,
            text="Finalizar Prueba",
            command=self.finish_test,
        )
        finish_button.pack(pady=5)

        # Etiqueta de resultados(inicialmente vacía)
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
            fg="#222222"
        )
        self.result_label.pack(pady=5)

        # Botón de salir
        exit_button = tk.Button(self.root, text="Salir", command=self.root.destroy)
        exit_button.pack(pady=20)

    def start_test(self) -> None:
        """Prepara la prueba y guarda el tiempo de inicio."""
        # Limpiar el campo de texto
        if self.typing_entry is not None:
            self.typing_entry.delete(0, tk.END)
            self.typing_entry.config(fg="#000000")
            self.typing_entry.focus()

        # (Opcional) cambiar la frase al iniciar cada test
        if self.phrase_label is not None:
            new_phrase = get_random_phrase()
            self.phrase_label.config(text=new_phrase)

        # Guardar tiempo de inicio
        self.start_time = time.time()
        print(f"Test started at: {self.start_time}")  # debug en consola
    def finish_test(self) -> None:
        """Calcula el tiempo total de la prueba y lo muestra en pantalla."""
        if self.start_time is None:
            # No se ha iniciado la prueba todavía
            if self.result_label is not None:
                self.result_label.config(
                    text="Primero debes iniciar la prueba.",
                    fg="red",
                )
            return

        end_time = time.time()
        elapsed_seconds = end_time - self.start_time

        if self.result_label is not None:
            self.result_label.config(
                text=f"Tiempo total: {elapsed_seconds:.2f} segundos",
                fg="#222222",
            )

        # Reseteamos start_time para evitar reutilizarlo sin nuevo inicio
        self.start_time = None