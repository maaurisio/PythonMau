import random

class Laptop:
    def __init__ (self, marca, procesador, memoria, costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento (self, descuento):
        return (self.costo * descuento)/100
    
    def realizar_diagnostico_sistema(self):
        resultado = {
            "MARCA": f"{self.marca}",
            "PROCESADOR": f"{self.procesador}",
            "MEMORIA RAM": "OK" if self.memoria >= 8 else "Aumentar la memoria ram",
            "BATERIA": "OK" if random.choice([True, False]) else "Cambiar de bateria"
        }
        return resultado

    #metodos estaticos
    @staticmethod
    def comparar_costo(Laptop1, Laptop2):
        if Laptop1.costo == Laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"
    
    @classmethod
    def asus_laptop (cls):
        marca = "asus"
        procesador = "i7"
        memoria = 16
        return cls(marca, procesador, memoria)