#Manejo de excepciones

try:
    num= float(input("Ingresa un numero: "))
    print(num*num)
except (ValueError,FileNotFoundError):
    print("Valor incorrecto!")