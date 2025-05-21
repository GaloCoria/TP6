#Ejercicio 1
'''def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
numero=int(input("Ingrese un numero:"))
for x in range(0,numero):
    print(factorial(x))'''
#Ejercicio 2
'''def fibonacci(n):
 if n == 0:
    return 0
 elif n == 1:
    return 1
 else:
    return fibonacci(n - 1) + fibonacci(n - 2)
 
posicion = int(input("Ingresá hasta qué posición de la serie de Fibonacci querés ver: "))

for i in range(posicion + 1):
    print(fibonacci(i))'''
#Ejercicio 3
'''def potencia(base, exponente):
    if exponente==0:
        return 1
    else:
         return base * potencia(base, exponente - 1)
    

base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")'''
#Ejercicio 4
'''def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


numero = int(input("Ingresá un número entero positivo: "))

if numero >= 0:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
else:
    print("Por favor, ingresá un número entero positivo.")'''
#Ejercicio 5

'''def es_palindromo(palabra):
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
    

palabra=str(input("Ingrese una palabra para ver si es palindromo:"))
if es_palindromo(palabra):
    print("Es palíndromo")
else:
    print("No es palíndromo")'''
#Ejercicio 6
'''def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + suma_digitos(numero // 10)
    
numero = int(input("Ingresá un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")'''
#Ejercicio 7
'''def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
print(contar_bloques(4))  '''
#Ejercicio 8
'''def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
        
print(contar_digito(12233421, 2))  
print(contar_digito(5555, 5))      '''