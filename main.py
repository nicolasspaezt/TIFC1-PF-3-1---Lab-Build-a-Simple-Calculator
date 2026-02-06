
num1 = int(input("escribe el primer numero: "))
num2 = int(input("escribe el segundo numero: "))
print(num1 + num2)

print("escoge la operacion: ")
print("1. Restar")
print("2. Multiplicacion")
print("3. Dividir")
print("4. Modulo")

opcion = input()

if  opcion == "1":
    print(num1 - num2)

elif opcion == "2":
    print(num1 * num2)

elif opcion == "3":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error")

elif opcion == "4":
    print(num1 % num2)

else:
    print("opcion invalida") 

