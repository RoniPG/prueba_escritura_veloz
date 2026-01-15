import tkinter as tk


def main():

    # Crear ventana principal
    root = tk.Tk()
    root.title("Prueba de Escritura Veloz")
    root.geometry("600x300")

    # Etiqueta de bienvenida
    title_label = tk.Label(
        root, text="Prueba de Escritura Veloz", font=("Arial", 16, "bold")
    )
    title_label.pack(pady=20)

    # Mensaje descriptivo
    description_label = tk.Label(
        root,
        text=(
            "En esta aplicación verás una frase y tu reto será escribirla "
            "lo más rápido y preciso posible."
        ),
        wraplength=500,  # Ajusta el texto al ancho
        justify="center",  # Centra el texto
        font=("Arial", 12),
        fg="#555555",  # Color gris suave
    )
    description_label.pack(pady=10)

    # Botón de salir
    exit_button = tk.Button(root, text="Salir", command=root.destroy)
    exit_button.pack(pady=20)

    """
    TODO: Añadir widgets y lógica de la aplicación aquí
    - Mensaje descriptivo donde escribirá el usuario
    etc.
    """

    root.mainloop()


if __name__ == "__main__":
    main()
