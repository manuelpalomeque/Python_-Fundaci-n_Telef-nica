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
listaF = [893, 755, 708, 746, 801, 581, 187, 688, 492, 579, 469, 195, 918, 667, 7, 15, 212, 114, 635, 331]

valorMax = max(listaF)
valorMin = min(listaF)

resultadoA = valorMax % valorMin
print('El modulo entre el valor maximo: {}, y el valor minimo: {}, es igual a: {}'.format(valorMax,valorMin,resultadoA))

# Ejercicio 7
# Pedir el ingreso por teclado de 3 valores numéricos entre 1 y 10 correspondientes a las notas de un alumno. En base
# al promedio final de las tres notas, mostrar un mensaje por pantalla que indique si el alumno promociona la materia
# (nota final 7,8,9 o 10), debe rendir final (nota final 4,5 o 6) o recursa (nota 1,2,3).

valor1 = float(input('Ingrese la primer nota del alumno: '))
valor2 = float(input('Ingrese la segunda nota del alumno: '))
valor3 = float(input('Ingrese la tercer nota del alumno: '))

suma1 = valor1 + valor2 + valor3
promedio1 = suma1/3

if promedio1 >= 7:
    print('El alumno promociona la materia, su promedio es de {}'.format(promedio1))
elif promedio1 >= 4 and promedio1 <= 6:
    print('El alumno debe rendir el final, su promedio es de {}'.format(promedio1))
else:
    print('El alumno debe recursar la materia, su promedio es {}'.format(promedio1))

# Ejercicio 8
# Pedir el ingreso por teclado de 3 valores numéricos entre 1 y 10 correspondientes a las notas de un alumno. En base al
# promedio final de las tres notas, mostrar un mensaje por pantalla que indique si el alumno promociona la materia
# (nota final 7,8,9 o 10), debe rendir final (nota final 4,5 o 6) o recursa (nota 1,2,3).

valor4 = float(input('Ingrese la primer nota del alumno: '))
valor5 = float(input('Ingrese la segunda nota del alumno: '))
valor6 = float(input('Ingrese la tercer nota del alumno: '))

sumaP = valor4 + valor5 + valor6
promedio1 = sumaP/3

if promedio1 >= 7:
    print('El alumno promociona la materia, su promedio es de {}'.format(promedio1))
elif promedio1 >= 4 and promedio1 <= 6:
    print('El alumno debe rendir el final, su promedio es de {}'.format(promedio1))
else:
    print('El alumno debe recursar la materia, su promedio es {}'.format(promedio1))

# Ejercicio 8
# Solicitar por teclado la cantidad de partidos ganados, empatados y perdidos de un determinado club de fútbol.
# Calcular y mostrar el puntaje final sabiendo que cada partido ganado le otorga 3 puntos, cada partido empatado 1
# punto y ningún punto por cada partido perdido.

cantidadGanados = int(input('Ingrese la cantidad de partidos ganados: '))
cantidadEmpatados = int(input('Ingrese la cantidad de partidos empatados: '))
cantidadPerdidos = int(input('Ingrese la cantidad de partidos perdidos: '))

puntajeGanado = cantidadGanados * 3
puntajeEmpatado = cantidadEmpatados
puntajeTotal = puntajeGanado + puntajeEmpatado

print('El puntaje total es de: {} puntos'.format(puntajeTotal))

# Ejercicio 9
# Solicitar por teclado el ingreso de un número entero. Asignar dicho número a una variable, transformarla a coma
# flotante y mostrarla por pantalla (valor y tipo de variable).

numeroEntero = int(input('Ingrese el numero entero: '))
numeroFlotante = float(numeroEntero)

print(numeroFlotante, type(numeroFlotante))

# Ejercicio 10
# Desarrollar un programa que solicite al usuario los lados de un rectángulo y calcule su perímetro y su superficie.
# Informar ambos resultados por pantalla

largoR = float(input('ingrese el largo del rectangulo en metros: '))
anchoR = float(input('ingrese el ancho del rectangulo en metros: '))

perimetroR = (largoR * 2) + (anchoR * 2)
superficieR = largoR * anchoR

print('El perimetro es de {} metros, y la superficie es de {} m2'.format(perimetroR,superficieR))

# Ejercicio 11
# Pedir al usuario que ingrese por teclado dos números reales y utilizarlos para realizar todas las operaciones
# aritméticas vistas (suma, resta, multiplicación, división, potencia, división entera y resto).
# Mostar todos los resultados por pantalla (un resultado por línea) con su respectiva leyenda aclarando de que
# operación se trata.

real1 = int(input('Ingrese el primer numero: '))
real2 = int(input('Ingrese el segundo numero: '))

suma_ = real1 + real2
resta_ = real1 - real2
multiplicacion_ = real1 * real2
division_ = real1 / real2
potencia_ = real1 ** real2
resto_ = real1 % real2

print('''El resultado de la suma es: {}
El resultado de la resta es: {}
El resultado de la multiplicacion es: {}
El resultado de la division es: {}
El resultado de la potencia es: {}
El resultado del resto es: {}
'''.format(suma_,resta_,multiplicacion_,division_,potencia_,resto_))

# Ejercicio 12
# Si creamos tres listas. La primera contiene 4 números, la segunda contiene 5 letras y en la tercera le cargamos como
# elementos las dos listas anteriores.
# ¿Cuántos elementos contendrá la tercera lista? Demostrar mediante un breve código.

lista_1 = [1,2,3,4]
lista_2 = ['a','b','c','d','e']
lista_3 = [lista_1,lista_2]

print('La cantidad de elementos de la lista 3 son: {} elementos, los cuales son las listas 1 y 2: {}'.format(len(lista_3),lista_3))

# Ejercicio 13
# Escribir un programa que pida ingresar un número entero mayor que cero por teclado.
# Verificar si el número ingresado es múltiplo de 2, 3, 4, 5, 6, 7,8 o 9.
# Armar una lista con los números encontrados (por ejemplo, si el número ingresado es múltiplo de 3,6 y 7, armamos una
# lista que contenga estos tres números).
# Mostrar la lista por pantalla, ordenada de mayor a menor.
# En caso de que el número ingresado no sea múltiplo de estos números, mostrar por pantalla el mensaje “No se
# encontraron divisores exactos”.

num_ = float(input('Ingrese un numero mayor que 0: '))
lista_divisores = []

for j in range(2, 10):
    if num_ % j == 0:
        lista_divisores.append(j)

if len(lista_divisores) == 0:
    print('No se encontraron divisores exactos')
else:
    lista_divisores.reverse()
    print('Los divisores son: {}'.format(lista_divisores))

# Ejercicio 14
# Pedirle al usuario que ingrese dos números enteros por teclado y contar cuantos números pares hay entre ambos valores
# ingresados.

num_entero1 = int(input('Ingrese el primer numero: '))
num_entero2 = int(input('Ingrese el segundo numero: '))
contPar = 0

if num_entero1 < num_entero2:
    numMenor_ = num_entero1
    numMayor_ = num_entero2
else:
    numMenor_ = num_entero2
    numMayor_ = num_entero1

for k in range(numMenor_, numMayor_ + 1):
    if k % 2 == 0:
        contPar += 1

print('Entre {} y {} se encontraron: {} números pares'.format(numMenor_, numMayor_, contPar))

# Ejercicio 15
# Escribir un programa que permita al usuario ingresar por teclado tantos números enteros como desee. Cuando no quiera
# ingresar más números, deberá ingresar el cero. A continuación, determinar cuál de los números ingresados es el mayor y
# cuál es el menor. Mostrar ambos por pantalla.

ingreso_ = int(input('Ingrese un los valores que desee, para finalizar ingrese 0 (cero): '))

num_menorB = ingreso_
num_mayorB = ingreso_

while ingreso_ != 0:
    if ingreso_ < num_menorB:
        num_menorB = ingreso_
    elif ingreso_ > num_mayorB:
        num_mayorB = ingreso_
    ingreso_ = int(input('Ingrese un los valores que desee, para finalizar ingrese 0 (cero): '))

print('El numero menor es: {} y el numero mayor es: {}'.format(num_menorB, num_mayorB))

# Ejercicio 16
# Escribir un programa que pida al usuario, que ingrese una frase por teclado. El programa deberá tener dos funciones,
# una que reciba la frase y devuelva solo las vocales de dicha frase y otra función que reciba la misma frase pero que
# devuelva solo las consonantes. Mostrar por pantalla la frase original ingresada por el usuario, las vocales y las
# consonantes devueltas por sus respectivas funciones.

frase_ = input('Ingrese la frase: ')

def vocalesFrase(frase_):
    frase_min = frase_.upper()
    vocales_T = ['A','E','I','O','U']
    vocales_f = []
    for let in frase_min:
        for e in vocales_T:
            if let == e:
                vocales_f.append(let)
    return vocales_f

def consonantesFrase(frase_):
    frase_min = frase_.upper()
    consonantes_T = ['B','C','D','F','G','H','J','K','L','M','N','Ñ','P','Q','R', 'S','T','V','X','Z','W','Y']
    consonantes_F = []
    for let in frase_min:
        for e in consonantes_T:
            if let == e:
                consonantes_F.append(let)
    return consonantes_F

voc = vocalesFrase(frase_)
cons =  consonantesFrase(frase_)

print('la frase ingresada fue: "{} ", donde las vocales son: {} , y las consonantes son: {}'.format(frase_,voc,cons))

# Ejercicio 17
# Escribir una función en Python para calcular el factorial de un número entero positivo. Basarse en la siguiente
# definición: El factorial de un número entero positivo n, se define como el producto de todos los números enteros
# positivos menores o iguales a n. El factorial de cero es 1. Por ejemplo, el factorial de 4 será 4x3x2x1 = 24. No
# utilizar ninguna función ni módulo matemático, solo lo visto en clase.

numFactorial = int(input('Ingrese un numero entero y positivo: '))

def calculadorFactorial(numFactorial):
    if numFactorial == 0 or numFactorial == 1:
        mostrar = 'El factorial es igual a: 1'
        return mostrar
    else:
        factorial = 1
        for n in range(1,numFactorial+1):
            factorial *= n
        return factorial

prueba = calculadorFactorial(numFactorial)
print('Para el valor ingresado: {} , el factorial es: {}'.format(numFactorial,prueba))

# Ejercicio 18
# Escribir una función para determinar si un número entero, ingresado por teclado es un número primo. Un número primo
# es aquel que solo tiene como divisores enteros (resto igual a cero) al número 1 y a sí mismo, por ejemplo,
# el número 5.

num_analizar = int(input('Ingrese un numero: '))

def esEntero(num_analizar):
    cant = 0
    g = 1
    while g <= num_analizar:
        if num_analizar % g == 0:
            cant += 1
        g += 1
    if cant == 2:
        primo_t = 'es primo '
        return primo_t
    else:
        primo_t = 'no es primo'
        return primo_t

prueba1 = esEntero(num_analizar)
print(prueba1)

# Ejercicio 19
# Escribir una función que encuentre los números primos comprendidos entre dos números enteros ingresados por teclado.

v1 = int(input('Ingrese el primer valor: '))
v2 = int(input('Ingrese el segundo valor: '))

def primosB(v1, v2):
    if v1 > v2:
        v_menor = v2
        v_mayor = v1
    else:
        v_menor = v1
        v_mayor = v2

    estosSonPrimos = []

    for u in range(v_menor, v_mayor + 1):
        cant = 0
        g = 1
        while g <= u:
            if u % g == 0:
                cant += 1
            g += 1
        if cant == 2:
            estosSonPrimos.append(u)

    return estosSonPrimos

prueba_1a = primosB(v1, v2)
print('Para los valores: {} y {}, los numeros primos son: {}'.format(v1, v2, prueba_1a))

# Ejercicio 20
# Escribir un programa que llene una lista con 50 números al azar y muestre por pantalla el número (o números) que
# más se repite

import random

listaAzar = []
b = 1

while b <= 50:
    rand = random.randrange(1, 50)
    listaAzar.append(rand)
    b += 1

listaRepeticiones = []

for v in listaAzar:
    repe_canti = listaAzar.count(v)
    listaRepeticiones.append(repe_canti)

cantRepeMax = max(listaRepeticiones)

cuanRepesVM = listaRepeticiones.count(cantRepeMax)
cuantosElementos = cuanRepesVM / cantRepeMax

if cuantosElementos == 1:

    indice12 = listaRepeticiones.index(cantRepeMax)
    numeroRepeMasVeces = listaAzar[indice12]
    print('El numero que mas se repite es: {}, el cual se repite: {} veces'.format(numeroRepeMasVeces, cantRepeMax))

elif cuantosElementos > 1:
    lista_indice = []
    lista_numerosMasRepetidos = []
    vueltaIndice = 0

    for re in listaRepeticiones:
        if re == cantRepeMax:
            lista_indice.append(vueltaIndice)
            vueltaIndice += 1
        else:
            vueltaIndice += 1

    for ind in lista_indice:
        num_ero = listaAzar[ind]
        lista_numerosMasRepetidos.append(num_ero)

    datosATrabajar = []
    for item in lista_numerosMasRepetidos:
        if item not in datosATrabajar:
            datosATrabajar.append(item)
    print('los numeros que mas se repiten son: {}, con un total de: {} repeticiones cada uno'.format(datosATrabajar,
    cantRepeMax))

# Ejercicio 21.
# Escribir un programa que le pregunte al usuario cuantas palabras desea ingresar, luego le permita ingresarlas todas y
# finalmente mostrarlas por pantalla.

cuantas_palabras = int(input('Cuantas palabras desea ingresar?: '))
lista_palIngresadas = []
cc = 0

while cc < cuantas_palabras:
    palabras_In = input('Ingrese la palabra: ')
    lista_palIngresadas. append(palabras_In)
    cc += 1

print('Se completo la cantidad de: {} palabras deseadas. Las cuales son: {}'.format(cuantas_palabras, lista_palIngresadas))

# Ejercicio 22.
# Escribir un programa que le solicite al usuario ingresar 10 palabras, luego le pida ingresar una más y le diga si esa
# última palabra ingresada se encuentra entre las 10 palabras ingresadas anteriormente.

ingreso_usuario = input('Ingrese una palabra: ')
lista_palUsuario = []
c_pal = 0

while c_pal < 10:
    if len(lista_palUsuario) == 0:
        lista_palUsuario.append(ingreso_usuario)
        c_pal += 1
    else:
        ingreso_usu1 = input('Ingrese una palabra: ')
        lista_palUsuario.append(ingreso_usu1)
        c_pal += 1

palabra11 = input('Ingrese la palabra que quiere ver si esta en el listado: ')
esta_lista = False

for pal in lista_palUsuario:
    if pal == palabra11:
        esta_lista = True

if esta_lista == True:
    print('La palabra {}, fue ingresada anteriormente'.format(palabra11))
else:
    print('La palabra {}, no fue ingresada a la lista'.format(palabra11))

# Ejercicio 23.
# Crear una lista con 10 números enteros y mostrarlos por pantalla.Luego reemplazar todos los números pares por la
# palabra PAR y volver a mostrar la lista por pantalla

import random

lista_numEnteR = []

while len(lista_numEnteR) < 10:
    lista_numEnteR.append(random.randrange(1, 150))

lista_conPares = []
for nrs in lista_numEnteR:
    lista_conPares.append(nrs)

cont_ind = 0

for nr in lista_numEnteR:
    if nr % 2 == 0:
        lista_numEnteR[cont_ind] = 'PAR'
        cont_ind += 1
    else:
        cont_ind += 1

print('''La lista  con los 10 numeros son: {}
La lista con la palabra PAR: {}'''.format(lista_conPares, lista_numEnteR))
