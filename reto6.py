from datetime import datetime

class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje} km")

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
            print(f"Kilometraje actualizado a {self.kilometraje} km")
        else:
            print("❌ No se puede reducir el kilometraje")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"🚘 Viajaste {kilometros} km. Kilometraje actual: {self.kilometraje} km")
        else:
            print("❌ La cantidad de kilómetros debe ser positiva")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo 😎")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado 😅")
        else:
            print("¡Ya déjame descansar por favor! 😵")

    # 🔹 MÉTODO DE CLASE → Crear Toyota del año actual
    @classmethod
    def toyota_actual(cls, modelo):
        año_actual = datetime.now().year
        return cls("Toyota", modelo, año_actual)

    # 🔹 MÉTODO ESTÁTICO → Validar kilometraje igual
    @staticmethod
    def mismo_kilometraje(auto1, auto2):
        return auto1.kilometraje == auto2.kilometraje

    # 🔹 MÉTODO DE CLASE ADICIONAL → Crear auto clásico
    @classmethod
    def auto_clasico(cls, marca, modelo):
        return cls(marca, modelo, 1980)

    # 🔹 MÉTODO ESTÁTICO ADICIONAL → Verificar si un auto es antiguo
    @staticmethod
    def es_antiguo(auto):
        return auto.año < 1990
