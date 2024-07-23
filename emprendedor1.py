import math

#Datos que proporciona el usuario
psuscripcion = float(input("Indique precio suscripcion:\n>"))
usuarios = float(input("Indique numero de usuarios:\n>"))
gastototal = float(input("Ingrese el gasto total:\n>"))

#Calculo

utilidades = psuscripcion * usuarios - gastototal

#resultado 

print(f"Las utilidades son : {utilidades}")