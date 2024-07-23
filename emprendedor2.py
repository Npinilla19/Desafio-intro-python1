import math

#Datos que proporciona el usuario
psuscripcion = float(input("Indique precio suscripcion:\n>"))
usuarionormal = float(input("Indique numero de usuarios normales:\n>"))
usuariopremium = float(input("Indique numero de usuarios premium:\n>"))
gastototal = float(input("Ingrese el gasto total:\n>"))

#Calculo

utilidadesnormal = psuscripcion * usuarionormal - gastototal
utilidadespremium = (psuscripcion + psuscripcion/2) * usuariopremium - gastototal

#resultado 

print(f"la utilidad usuario normal son: {utilidadesnormal}")
print(f"La utilidad usuarios premium es {utilidadespremium}")