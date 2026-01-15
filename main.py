import tkinter as tk

from typing_app import TypingSpeedApp


def main() -> None:

    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
