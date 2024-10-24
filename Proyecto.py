# Ejercicio 1: Par o Impar
# Escribe un programa que pida un número al usuario e imprima si el número es par o impar.

# Ejercicio 2: Mayor de Dos Números
# Escribe un programa que pida dos números al usuario e imprima cuál de ellos es el mayor.
# print("ingrese dos numeros")
# number_1 = int(input("primer numero"))
# number_2 = int(input("segundo numero"))
# if number_1 > number_2:
#     print(f"El numero {number_1} es mayor {number_2} ")
# elif number_1 == number_2:
#     print(f"El numero son iguales")
# else:
#     print(f"El numero {number_2} es mayor a {number_1}")

# Ejercicio 3: Positivo, Negativo o Cero
# Escribe un programa que pida un número al usuario e imprima si el número es positivo, negativo o cero.
print("ingrese un numero")
number = int(input())
if number > 0:
    print(f"{number}es mayor a 0 es positivo")
elif number < 0:
    print(f"{number} es menor a 0 es negativo")
else:
    print(f"es 0")


# Ejercicio 4: Calificación
# Escribe un programa que pida una calificación (0-100) al usuario e imprima la letra correspondiente: A, B, C, D o F.

# Ejercicio 5: Año Bisiesto
# Escribe un programa que pida un año al usuario e imprima si es un año bisiesto o no.

# Ejercicio 6: Número en Rango
# Escribe un programa que pida un número al usuario y verifique si está dentro
# del rango 1-100 (inclusive).
########################################################################
# print("Ingrese 1 numero")
# number_1 = int(input())
# print(f"Tipo de dato -> {type(number_1)}")

# if number_1 <= 100:
#     if number_1 > 0:
#         print(f"El numero {number_1} es mayor a 0 y menor a 100")

# if number_1 > 0:
#     if number_1 <= 100:
#         print(f"El numero {number_1} es mayor a 0 y menor a 100")

# if number_1 > 0 or number_1 <= 100:
#     print(f"El numero {number_1} es mayor a 0 y menor a 100")
########################################################################
# El usuario ingresa 3 numeros: debe decir cual es el numero mayor y cual es el menor
# print("Ingrese 3 numeros")
# numero_1 = int(input("Primer numero"))
# numero_2 = int(input("Segundo numero"))
# numero_3 = int(input("Tercer numero"))
# print(f"El primer numero {numero_1} y su tipo de dato es {type(numero_1)}")
# print(f"El segundo numero {numero_2} y su tipo de dato es {type(numero_2)}")
# print(f"El tercer numero {numero_3} y su tipo de dato es {type(numero_3)}")

# # list_1 = [numero_1, numero_2, numero_3]
# # print(f"El numero mayor es {max(list_1)}")
# # print(f"El numero menor es {min(list_1)}")
# if numero_1 > numero_2:
#     if numero_1 > numero_3:
#         pass
#     elif numero_1 == numero_3:
#         print(f"Los numeros 1 y 3 son iguales y son los mayores y su valor es {numero_1}")
#     else:


# if numero_1 > numero_2 and numero_1 > numero_3:
#     print(f"numero 1 -> {numero_1} es el mayor")
# else:
#     if numero_2 > (numero_1 and numero_3):
#         print(f"numero 2 -> {numero_2} es el mayor")


# print(f"El numero es {number_1}")
# C:\Users\usuario\Documents\Proyectos python\ejercicios_angie
# Ejercicio 7: Contraseña Correcta
# Escribe un programa que pida una contraseña al usuario y verifique si es correcta. La contraseña correcta debe estar predefinida en el programa.

# Ejercicio 8: Número Múltiplo
# Escribe un programa que pida un número al usuario e imprima si es múltiplo de 3, de 5 o de ambos.

# Ejercicio 9: Triángulo Válido
# Escribe un programa que pida tres lados de un triángulo al usuario e imprima si forman un triángulo válido.

# Ejercicio 10: Calculadora Básica
# Escribe un programa que pida dos números y una operación (suma, resta, multiplicación, división) al usuario y realice la operación correspondiente.


# juan = '7'
# angie = '27'

# if fabio is trabajo:
#     print(f"NO PUEDE VISITAR A LA FAMILIA, {fabio} DEBE TRABAJAR")
# if juan is futbol:
#     print(f"NO PUEDE SALIR, {juan} DEBE IR A JUGAR")
# elif angie is trabajo:
#     print(f"NO PUEDE SALIR, {angie} DEBE IR A TRABAJAR")
# elif angie is fabio:
#     print(f"NO PUEDE SALIR, {angie} DEBE IR A VISITAR A FABIO")
# else:
#     print(f"{juan} y {angie} VAN A SALIR DE PASEO")