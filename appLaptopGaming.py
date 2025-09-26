import tkinter as tk
from tkinter import ttk
from HerenciaDeClases import Laptop_Business  # importa tu clase

class AppBusiness:
    def __init__(self, root):
        self.root = root
        self.laptops = []  # lista para guardar laptops

        root.title("Laptops Business")

        self.setup_ui()

    def setup_ui(self):
        # Marca
        ttk.Label(self.root, text="Marca").grid(row=0, column=0, padx=5, pady=5)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1, padx=5, pady=5)

        # Procesador
        ttk.Label(self.root, text="Procesador").grid(row=1, column=0, padx=5, pady=5)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1, padx=5, pady=5)

        # Memoria
        ttk.Label(self.root, text="Memoria").grid(row=2, column=0, padx=5, pady=5)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1, padx=5, pady=5)

        # Almacenamiento
        ttk.Label(self.root, text="Almacenamiento").grid(row=3, column=0, padx=5, pady=5)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=3, column=1, padx=5, pady=5)

        # Duración batería
        ttk.Label(self.root, text="Duración Batería (h)").grid(row=4, column=0, padx=5, pady=5)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=4, column=1, padx=5, pady=5)

        # Botón
        ttk.Button(self.root, text="Agregar Laptop Business", command=self.agregar_laptop).grid(row=5, column=0, columnspan=2, pady=10)

        # Área de texto
        self.mostrar_laptops = tk.Text(self.root, height=10, width=70)
        self.mostrar_laptops.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def agregar_laptop(self):
        # Crear objeto
        nueva_laptop = Laptop_Business(
            self.marca.get(),
            self.procesador.get(),
            self.memoria.get(),
            self.almacenamiento.get(),
            self.duracion_bateria.get()
        )

        # Guardar en lista
        self.laptops.append(nueva_laptop)

        # Mostrar en el text
        self.mostrar_laptops.insert(tk.END, str(nueva_laptop))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppBusiness(root)
    root.mainloop()
