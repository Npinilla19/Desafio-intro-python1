#libreria
import math

# datos que debe ingresar el usuario
radio = float(input("Ingrese el radio en kilometros:\n>"))
gravedad = float(input("Ingrese la constante g:\n>"))

# calculo velocidad de escape

velocidad_escape = math.sqrt(2 * (radio * 1000) * gravedad)

#resultado que se muestra al usuario
print(f"la velocidad de escape es: {round(velocidad_escape,1)}")