from src.entrega1.Almacen import Almacen
from src.entrega1.Transporte import Transporte, Periodicidad
from src.entrega1.Envio import Envio
from datetime import datetime

print("\nTestAlmacen.py")

# of()
a1 = Almacen.of(101, "Prendas", "Sevilla", 37.3891, -5.9845)
print("Creación de un almacén con of():")
print(str(a1))

# parse()
a2 = Almacen.parse("202,Electrodomésticos,Madrid,40.4168,-3.7038")
print("\nCreación de un almacén con parse():")
print(str(a2))

# random()
a3 = Almacen.random()
print("\nCreación de un almacén aleatorio con random():")
print(str(a3))


print("\nTestTransporte.py")

# of()
fecha1 = datetime.strptime("2025-09-29 10:30", "%Y-%m-%d %H:%M")
t1 = Transporte.of(1, 2, fecha1, 15, 120, Periodicidad.DAILY)
print("Creación de transporte con of():")
print(str(t1))

# parse()
t2 = Transporte.parse("3,4,2025-09-29 14:45,20,180,WEEKLY,2")
print("\nCreación de transporte con parse():")
print(str(t2))

# random()
t3 = Transporte.random()
print("\nCreación de transporte aleatorio con random():")
print(str(t3))

# siguiente_fecha_disponible()
fecha_ref = datetime.strptime("2025-09-28 10:00", "%Y-%m-%d %H:%M")
salida, llegada = t1.siguiente_fecha_disponible(fecha_ref)
print("\nPrueba de siguiente_fecha_disponible:")
print(f"Salida: {salida.strftime('%Y-%m-%d %H:%M:%S')} | Llegada: {llegada.strftime('%Y-%m-%d %H:%M:%S')}")


print("\nTestEnvio.py")

# Crear envío completo con transporte y fechas
fecha_peticion = datetime.strptime("2025-09-29 10:00", "%Y-%m-%d %H:%M")
salida_e1, llegada_e1 = t1.siguiente_fecha_disponible(fecha_peticion)
e_completo = Envio.of(fecha_peticion, 1, 2, transporte=t1, salida=salida_e1, llegada=llegada_e1)

print("Creación de un envío con of():")
print(f"Fecha petición: {e_completo.fecha_peticion}")
print(f"Almacén origen: {e_completo.al1}")
print(f"Almacén destino: {e_completo.al2}")
print(f"Transporte asociado: {e_completo.transporte}")
print(f"Fecha de salida: {e_completo.fecha_de_salida}")
print(f"Fecha de llegada: {e_completo.fecha_de_llegada}")

# Crear cadena de envíos con transporte y fechas
almacenes = [1, 2, 3, 4]
print("\nCreación de una cadena de envíos con envios():")
print(f"La lista de almacenes es: {almacenes} y la fecha de petición es la misma para todos los envíos.\n")

envios = []
for i in range(len(almacenes) - 1):
    al1 = almacenes[i]
    al2 = almacenes[i + 1]
    fecha_peticion = fecha_ref  # ✅ siempre con fecha válida
    transporte = Transporte.random()
    salida, llegada = transporte.siguiente_fecha_disponible(fecha_peticion)
    envio = Envio.of(fecha_peticion, al1, al2, transporte=transporte, salida=salida, llegada=llegada)
    envios.append(envio)

for i, envio in enumerate(envios, start=1):
    print(f"Envio {i}: al1 = {envio.al1}, al2 = {envio.al2}, fecha_peticion = {envio.fecha_peticion}, salida = {envio.fecha_de_salida}, llegada = {envio.fecha_de_llegada}")