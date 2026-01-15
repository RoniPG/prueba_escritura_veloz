import tkinter as tk

def main():

    # Crear ventana principal
    root = tk.Tk()
    root.title("Prueba de Escritura Veloz")
    root.geometry("600x300")

    # Etiqueta de bienvenida
    title_label = tk.Label(
        root,
        text="Prueba de Escritura Veloz",
        font=("Arial", 16, "bold")
    )
    title_label.pack(pady=20)

    '''
    TODO: Añadir widgets y lógica de la aplicación aquí
    - Mensaje descriptivo donde escribirá el usuario
    - Botón de salir
    etc.
    '''

    root.mainloop()

if __name__ == "__main__":
    main()