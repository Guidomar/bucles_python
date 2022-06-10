# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Similar al ejercicio de "calificaciones":

Debe calcular el promedio de todas las notas que se encuentra
almacenadas en una lista llamada "notas" que ya
hemos definido al comienzo del archivo

Luego transformar la califiación en una letra
según la siguiente escala:
- Si el puntaje es mayor igual a 90 --> imprimir A
- Si el puntaje es mayor igual a 80 --> imprimir B
- Si el puntaje es mayor igual a 70 --> imprimir C
- Si el puntaje es mayor igual a 60 --> imprimir D
- Si el puntaje es menor a  60      --> imprimir F

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0

cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria

# Terminado el bucle calcule el promedio como
# promedio = sumatoria / cantidad_notas

# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

# Imprima en pantalla al cantidad de ausentes

notas_validas= []

for i in notas:
    if i >0:
        notas_validas.append(i)
        print("notas_validas:",notas_validas)
        sumatoria +=i
        print("La sumatoria de notas es: ", sumatoria)
        cantidad_notas += 1
        print("La cantidad de notas es:",cantidad_notas)
        promedio_notas = sumatoria/cantidad_notas
        print("El promedio de notas es:",promedio_notas)
    else:
        
        cantidad_ausentes+= 1
        print("La cantidad de ausentes es: ", cantidad_ausentes)
    
notas_letras = []
for puntaje in notas_validas:
    if puntaje >=90:
        letra = "A"
        print(letra)
    elif puntaje>=80:
        letra = "B"
        print(letra)
    elif puntaje>=70:
        letra = "C"
        print(letra)
    elif puntaje>=60:
        letra = "D"
        print(letra)
    else:
        letra ="E"
        print(letra)
    
    notas_letras.append(letra)
    print("notas por letras: ", notas_letras)