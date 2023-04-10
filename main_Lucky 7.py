"""
Read the first input – a number n.
Then read input n times. Each time you'll get an integer value.
If it's a multiple of 7 (can be divided by 7 without a remainder),
print its square on a new line.
Note that you don't need to perform any calculations on the first input (the n).
"""
print("Introduce un número para las repeticiones: ")
numero = int(input())
print("el número escojido ha sido el {}, a continuación introduce un número para cada pepetición: ".format(numero))


for i in range(numero):
    numero = int(input())
    if numero % 7 == 0:
        print(numero ** 2)