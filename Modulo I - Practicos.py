# Fundamentos de programación en Python

#  Ejercicio 1
# Dados 2 números enteros, imprimir por pantalla el producto.
# Si el producto de ambos numeros es mayor a 100, mostrar además la suma de los numeros.

# Como valor agregado, sumo la posibilidad que los numeros puedan ser ingresados desde teclado:
numero1 = int(input('Por favor ingrese el primer numero: '))
numero2 = int(input('Por favor ingrese el segundo numero: '))
productoA = numero1 * numero2

if productoA > 100:
    sumaA = numero1 + numero2
    print('El producto entre los numeros es: {}, entonces la suma de ambos valores es: {}'.format(productoA, sumaA))
else:
    print('El prducto entre ambos valores es: {}, no es mayor a 100, por lo tanto no se deben sumar'.format(productoA))


# Ejercicio 2
# Dada una lista de números, se pide iterar los elementos de la lista y almacenar en otra lista el resultado de sumar
# ese elemento con el anterior.
# Por ejemplo, dada la lista: `[1, 2, 3, 4]`, se espera que la salida sea una lista con los elementos `[3, 5, 7]`
listaA = [1, 2, 3, 4]
listaB = []

for x in range(0, 3):  # si lo hago en rango 0 al 4  me va a dar error porque no hay ningun valor asignado al indice 4
    if len(listaB) == 0:
        sumaListas = listaA[x + 1] + listaA[x]
        listaB.append(sumaListas)
    else:
        sumaListas = listaA[x + 1] + listaA[x]
        listaB.append(sumaListas)

print(listaB)

# Ejercicio 3
# Dado un string, mostrar por pantalla unicamente las vocales en formato Mayuscula
# Por ejemplo, el string `"Este es un string de prueba"` obtendra como output `['E', 'E', 'E', 'U', 'I', 'E', 'U', 'E',
# 'A']`
# Pistas:
# - Utilizar funciones propias de strings como `upper`, `lower`
palabra1 = 'Este es un string de prueba'
palabra1_mayus = palabra1.upper()

vocales1 = ['A','E','I','O','U']
vocalesMayusculas = []

for letra in palabra1_mayus:
    for x in vocales1:
        if letra == x :
            vocalesMayusculas.append(letra)

print(vocalesMayusculas)
# Ejercicio 4
# Dada una lista de numeros, mostrar por genere una lista con todos los múltiplos de 7.
# Por ejemplo, para la lista `[1, 2, 7, 10, 21]`, se muestran por pantalla los numeros `7` y `21`
listaC = [1,2,7,10,21]
listaD = []

for n in listaC:
    if n % 7 == 0:
        listaD.append(n)

print(listaD)

# Ejercicio 5
# Contar cuántos elementos de la lista cumple alguna de las siguientes condiciones:
# - El elemento es un carácter en minúscula
# - Es un número entero par
# ``` python
# lista = ['a', 2, 5, 'B', 9, 'd', 4, 'o', 7, '%', 3.1, '&']
# ```
listaE = ['a', 2, 5, 'B', 9, 'd', 4, 'o', 7, '%', 3.1, '&']
contTotal = 0
contParEntero = 0
contCarMinus = 0

for elemento in listaE:
    if type(elemento) == int and elemento % 2 == 0:
        contParEntero += 1
        contTotal += 1
    elif type(elemento) == str and elemento.islower() == True:
        contCarMinus += 1
        contTotal += 1

print(
    'Existe un total de {} elementos que poseen dichas condiciones, {} son caracteres en minusculas y {} son numeros '
    'enteros pares'.format(contTotal, contCarMinus, contParEntero))

# Ejercicio 6
# Obtener el módulo entre el máximo y el mínimo de la siguiente lista.
# ```
# lista = [893, 755, 708, 746, 801, 581, 187, 688, 492, 579, 469, 195, 918, 667, 7, 15, 212, 114, 635, 331]
# ```
# `result= 918%7 = 1`

