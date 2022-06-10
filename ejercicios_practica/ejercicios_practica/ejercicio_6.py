# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuente cuantos números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

lista = []
fin_2 = fin+1
cantidad_numeros_negativos = 0
cantidad_numeros_positivos = 0  # Inicializo el contador en 0

# for ... in range(....)
for i in range (inicio,fin_2):
    lista.append(i)
    print("La lista de números es", lista)
    if(i<0):
        cantidad_numeros_negativos += 1
    elif (i==0):
        continue
    else:
        cantidad_numeros_positivos += 1
    
    print(f"La lista tierne {cantidad_numeros_negativos} numeros negativos y {cantidad_numeros_positivos} números positivos")
# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
