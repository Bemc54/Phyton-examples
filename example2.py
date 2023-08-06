'''
el programa le pedira al usuario que ingrese numeros hasta que el asi lo desee, una vez termine
el programa imprimira, el numero mayor dentro de la lista
'''
'''
lista = [1,2,3,4,5]
#agregar un elemento a la lista o arreglo
lista.append(6)
#imprimir el numero mayor de la lista
print(max(lista))
'''
def validate_integer(str_num):
    try:
        num = int(str_num)
        return num
    except:
        print("Eso no es un entero")
        return False

nums = []
res = "y"

while res == "y"  or res == "Y":
    num = (input("ingrese un numero: "))
    while validate_integer(num) == False:
        num = (input("ingrese un numero: "))
    else:
        nums.append(int(num))
        res = input("Quieres ingresar mas numeros? y/n: ")
else:
    num_max = nums[0]
    num_min = nums[0]
    for num in nums:
        if num > num_max:
            num_max = num
        if num < num_min:
            num_min = num
    print("numero maximo: ",num_max)
    print("numero minimo: ",num_min)
