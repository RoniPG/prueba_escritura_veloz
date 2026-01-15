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

        # Botón de salir
        exit_button = tk.Button(self.root, text="Salir", command=self.root.destroy)
        exit_button.pack(pady=20)