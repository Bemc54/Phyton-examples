#Usuario ingresa dos números 
#El segundo número tiene que ser mayor al primero
#Los números dentro de este rango serán evaluados:
#Si son divisibles entre 3 imprimirá #Fizz
#Si esdivisible entre 5 #Buzz
#Entre ambos #FizzBuzz
#Entre ninguno de los dos imprimirá el número
first_number = int(input("ingresa un numero: "))
second_number = int(input("ingresa un numero mayor al primero: "))
while second_number<first_number:
    print("El segundo numero tiene que ser mayor al primero para avanzar\n")
    
    second_number:int(input("Ingresa un numero mayor al primero:"))
    for i in range(first_number, second_number + 1):
        divisible3 = i % 3 == 0
        divisible5 = i % 5 == 0
        if divisible3 and divisible5:
            print("FizzBuzz")
        elif divisible3:
            print("Fizz")
        elif divisible5:
            print("Buzz")
        else:
            print(i)