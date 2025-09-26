from clases import Laptop
import random

class LaptopGaming(Laptop):
    def __init__(self, marca, procesador, memoria, tarj_graf, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarj_graf = tarj_graf

    def realizar_diagnostico_sistema(self):
        # Llamamos al diagnóstico de la clase padre
        resultado_diagnostico = super().realizar_diagnostico_sistema()

        # Llamamos al diagnóstico de juegos
        resultado_juegos = self.realizar_diagnostico_juegos()

        # Combinamos ambos resultados
        resultado_diagnostico["Resultado juegos"] = resultado_juegos
        return resultado_diagnostico

    def __str__(self):
        #str: Sirve para definir cómo se mostrará un objeto cuando lo conviertas a texto.
        return f"Marca: {self.marca} \n Procesador: {self.procesador} \n Memoria: {self.memoria} \n Tarjeta Grafica: {self.tarj_graf} \n Costo: {self.costo} \n Impuesto: {self.impuesto}\n"
    
    def realizar_diagnostico_juegos(self):
        juegos = ["FORTNITE", "COD", "GTA"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarj_graf:
                fps = fps_base * 3
            elif "GTX" in self.tarj_graf:
                fps = fps_base * 2
            else:
                fps = fps_base
            resultados[juego] = f"{fps} FPS"
        return resultados


# 🔹 Nueva clase hija
class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria
        
    def __str__(self):
        return (f"Marca: {self.marca} | Procesador: {self.procesador} | Memoria: {self.memoria} | "
                f"Almacenamiento: {self.almacenamiento} | Batería: {self.duracion_bateria}h | "
                f"Costo: {self.costo} | Impuesto: {self.impuesto}\n")

    def realizar_diagnostico_sistema(self):
        # Traemos diagnóstico de la clase padre
        resultado_diagnostico = super().realizar_diagnostico_sistema()

        # Agregamos diagnósticos propios de laptops empresariales
        resultado_diagnostico["Almacenamiento"] = "OK" if self.almacenamiento > 256 else "Bajo espacio disponible"
        resultado_diagnostico["Duración Batería"] = "OK" if self.duracion_bateria > 5 else "Duración limitada"

        # Comprobaciones de conectividad
        resultado_diagnostico["Conectividad"] = self.verificar_conectividad_red()

        return resultado_diagnostico

    def verificar_conectividad_red(self):
        # Simulamos resultados aleatorios de red
        conectividad = {
            "Wi-Fi disponible": random.choice([True, False]),
            "Acceso a servidores empresariales": random.choice([True, False]),
            "Latencia baja": random.choice([True, False])
        }
        return conectividad
