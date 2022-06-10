# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

numero_uno = int(input("Ingrese un número: "))

numero_dos = int (input("Ingrese otro número: "))




while True:
    operador = str(input(" Ingrese un operador: "))
  
    if (operador == "suma"):
        suma = numero_uno + numero_dos
        print(f"La suma de {numero_uno} y {numero_dos} es:", suma)
    elif (operador == "resta"):
     resta = numero_uno - numero_dos
     print(f"La resta de {numero_uno} y {numero_dos} es:", resta)
    elif (operador == "multiplicacion"):
     multiplicacion = numero_uno * numero_dos
     print(f"La multiplicacion de {numero_uno} y {numero_dos} es:", multiplicacion)
    elif (operador == "division"):
     division = numero_uno / numero_dos
     print(f"La division de {numero_uno} y {numero_dos} es:", division)
    elif(operador== "exponente"):
     exponente = numero_uno ** numero_dos
     print(f"el expoenente de {numero_uno} elevado a {numero_dos} es:",exponente)
    elif(operador == "fin"):
        print("hasta la próxima operación!")
        break
    else:
        print("Error!!. Ingrese un operador válido")

         


