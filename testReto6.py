from reto6 import Auto
# Crear un Toyota nuevo del año actual
nuevo_auto = Auto.toyota_actual("Corolla")
nuevo_auto.mostrar_informacion()

# Crear un auto clásico
clasico = Auto.auto_clasico("Ford", "Mustang")
clasico.mostrar_informacion()

# Comparar kilometrajes
auto1 = Auto("Kia", "Rio", 2019)
auto2 = Auto("Mazda", "CX-3", 2021)

auto1.actualizar_kilometraje(5000)
auto2.actualizar_kilometraje(5000)

print("¿Tienen el mismo kilometraje?", Auto.mismo_kilometraje(auto1, auto2))

# Verificar si un auto es antiguo
print("¿El Mustang es antiguo?", Auto.es_antiguo(clasico))
