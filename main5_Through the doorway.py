"""
Suppose you want to carry a box with dimensions A × B × C (length × width × height)
through the doorway with dimensions X × Y (width × height).
Write a program to check whether it is possible.

The input format:
The input comprises five strings with numbers in the following order:
A, B, C, X, Y.
If the size of the doorway is greater than or equal to any two dimensions of the box,
it is considered that the box can be carried.

The output format:
If the box can be carried through the doorway, output "The box can be carried".
If it cannot be carried, output "The box cannot be carried".
"""

a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())

medidas_ordenadas = [a, b, c]
medidas_ordenadas.sort()

if x >= medidas_ordenadas[0] and y >= medidas_ordenadas[1]:
    print("The box can be carried")
elif y >= medidas_ordenadas[0] and x >= medidas_ordenadas[1]:
    print("The box can be carried")
else:
    print("The box cannot be carried")
