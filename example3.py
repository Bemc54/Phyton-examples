#pass: sirve para saltar un error en el que debe de ir codigo y se skipea el error
def validate_integer(str_num):
    try:
        num = int(str_num)
        return num
    except:
        print("Eso no es un entero")
        return False

inicio = input("ingresa el inicio: ")
while validate_integer(inicio) == False:
    inicio = input("Ingresa el inicio: ")
else:
    print("Eso si es un numero entero")



'''
try:
    inicio = int(input("ingresa el inicio: "))
    fin = int(input("ingresa el final: "))
except:
    print("Eso no es un entero")
'''


'''
while fin<=inicio:
    print("el fin tiene que ser mayor al inicio")
    fin = int(print("ingresa el final: "))
else:
    for num in range(inicio, fin):
        if num%3 == 0 and num%5 == 0:
            print("fizzBuzz")
        elif num%5 == 0:
            print("Buzz")
        elif num%3 ==0:
            print("fizz")
        else:
            print(num)
'''