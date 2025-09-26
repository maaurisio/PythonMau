from HerenciaDeClases import LaptopGaming
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = [] #crear una lista de laptops
        self.imagenes = [
            "D:\\KRAKEDEV\\M4\\PythonMau\\img\\img1.jpg",
            "D:\\KRAKEDEV\\M4\\PythonMau\\img\\img2.jpg",
            "D:\\KRAKEDEV\\M4\\PythonMau\\img\\img3.jpg"
        ]

        root.title("Ingresar Datos")

        self.setup_ui()
    
    def setup_ui(self):

        ttk.Label(self.root, text="Marca").grid(row=0, column=0)#placeholder
        self.marca = tk.StringVar()#tomar valor del dato
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)#ingresar dato y capturar

        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)#placeholder
        self.procesador = tk.StringVar()#tomar valor del dato
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)#ingresar dato y capturar

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)#placeholder
        self.memoria = tk.StringVar()#tomar valor del dato
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)#ingresar dato y capturar

        ttk.Label(self.root, text="Tarjeta Grafica").grid(row=3, column=0)#placeholder
        self.tarj_graf = tk.StringVar()#tomar valor del dato
        ttk.Entry(self.root, textvariable=self.tarj_graf).grid(row=3, column=1)#ingresar dato y capturar

        ttk.Label(self.root, text="Precio").grid(row=4, column=0)#placeholder
        self.precio = tk.StringVar()#tomar valor del dato
        ttk.Entry(self.root, textvariable=self.precio).grid(row=4, column=1)#ingresar dato y capturar

        ttk.Button (self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=5, column=0)

        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=6, column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=6)
        
    def agregar_laptop(self):
        #definir objeto
        nueva_laptop = LaptopGaming(self.marca.get(), self.procesador.get(), self.memoria.get(), self.tarj_graf.get(), self.precio.get())
        #añadir a la lista
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")
        self.mostrar_imagen_aleatorias()
        pass

    def mostrar_imagen_aleatorias(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize ((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0, 0, anchor=tk.NW, image = photo)
        self.canva.image = photo
        pass

root = tk.Tk()

app = App(root)
root.mainloop()


#pip install PILLOW - para imagenes