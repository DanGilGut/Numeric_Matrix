"""Write a program that reads an integer from input and prints:

"negative" if the number is less than 0;
"positive" if the number is greater than 0;
"zero" if the number equals 0.
Do not output double quotes."""

numero = int(input())
resultado = ["negative", "positive", "zero"]

if numero < 0:
    print(resultado[0])
elif numero > 0:
    print(resultado[1])
else:
    print(resultado[2])