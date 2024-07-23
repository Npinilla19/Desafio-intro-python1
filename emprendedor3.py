import math

#Datos que proporciona el usuario
psuscripcion = float(input("Indique precio suscripcion:\n>"))
usuarios = float(input("Indique numero de usuarios:\n>"))
gastototal = float(input("Ingrese el gasto total:\n>"))
Utilidadesanterior = float(input("Ingrese las utilidades del año anterior:\n>"))

#Calculo

utilidades = psuscripcion * usuarios - gastototal
razon = utilidades / Utilidadesanterior

#resultado 

print(f"Las utilidades actuales son : {utilidades}")
print(f"La razon ente la utilidad anterior y la actual es {round(razon,2)}")